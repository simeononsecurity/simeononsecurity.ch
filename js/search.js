// =============================
// Configuration
// =============================
const SUMMARY_RADIUS = 160;      // characters of context shown on each side of a match
const RESULTS_PER_PAGE = 10;
const MIN_QUERY_LENGTH = 2;      // queries shorter than this are not searched
const TYPE_DEBOUNCE_MS = 220;    // delay before live-search fires while typing

const fuseOptions = {
  shouldSort: true,
  includeMatches: true,
  includeScore: true,
  ignoreLocation: true,   // 'contents' is full page body text; a match far from
                           // position 0 is still a perfect match, not a mismatch.
  minMatchCharLength: 2,
  threshold: 0.35,
  keys: [
    { name: "title", weight: 0.45 },
    { name: "contents", weight: 0.6 },
    { name: "tags", weight: 0.1 },
    { name: "categories", weight: 0.05 }
  ]
};

// =============================
// State
// =============================
let fuseIndex = null;          // Fuse instance, built once the index JSON is fetched
let fetchPromise = null;       // in-flight/completed fetch of /index.json, shared & cached
let lastResults = [];          // full (unpaginated) result set from the most recent search
let lastQuery = "";
let debounceTimer = null;

// =============================
// Bootstrapping
// =============================
const inputBox = document.getElementById("search-query");

if (inputBox !== null) {
  const params = new URLSearchParams(location.search);
  const initialQuery = params.get("q") || "";
  const initialPage = parseInt(params.get("page"), 10) || 1;

  if (initialQuery) {
    inputBox.value = initialQuery;
    runSearch(initialQuery, initialPage, { updateUrl: false });
  } else {
    renderEmptyState();
  }

  // Live-as-you-type search. The surrounding <form> still submits normally
  // (GET /search?q=...) for no-JS clients and for the schema.org SearchAction
  // markup, so this is purely a progressive enhancement.
  inputBox.addEventListener("input", function () {
    const query = inputBox.value.trim();
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(function () {
      runSearch(query, 1, { updateUrl: true });
    }, TYPE_DEBOUNCE_MS);
  });

  const form = inputBox.closest("form");
  if (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      clearTimeout(debounceTimer);
      runSearch(inputBox.value.trim(), 1, { updateUrl: true });
    });
  }
}

// Delegated click handler for pagination links: intercepts same-page
// (?q=...&page=N) clicks so paging through results reuses the already
// fetched/indexed data instead of reloading the page and re-fetching
// /index.json (~9MB) from scratch for every page click.
const paginationContainer = document.getElementById("search-pagination");
if (paginationContainer) {
  paginationContainer.addEventListener("click", function (event) {
    const link = event.target.closest("a[data-page]");
    if (!link) return;
    event.preventDefault();
    const page = parseInt(link.dataset.page, 10) || 1;
    renderPage(page, { updateUrl: true });
  });
}

// =============================
// Search execution
// =============================

/** Loads (once) and returns the Fuse index, fetching /index.json only the first time. */
function loadIndex() {
  if (fetchPromise) return fetchPromise;
  fetchPromise = fetch("/index.json")
    .then(function (response) {
      if (!response.ok) {
        throw new Error("Search index request failed with status " + response.status);
      }
      return response.json();
    })
    .then(function (pages) {
      fuseIndex = new Fuse(pages, fuseOptions);
      return fuseIndex;
    })
    .catch(function (err) {
      // Clear the cached promise on failure so the next search attempt
      // retries the fetch instead of being permanently stuck replaying the
      // same rejection for the rest of the page's lifetime.
      fetchPromise = null;
      throw err;
    });
  return fetchPromise;
}

async function runSearch(query, page, opts) {
  opts = opts || {};
  lastQuery = query;

  if (!query || query.length < MIN_QUERY_LENGTH) {
    lastResults = [];
    renderEmptyState();
    if (opts.updateUrl) updateUrl(query, 1);
    return;
  }

  show(document.querySelector(".search-loading"));
  hideError();

  try {
    const fuse = await loadIndex();
    lastResults = fuse.search(query);
    renderPage(page, { updateUrl: opts.updateUrl });
  } catch (err) {
    console.error("Search error:", err);
    showError();
  } finally {
    hide(document.querySelector(".search-loading"));
  }
}

// =============================
// Rendering
// =============================

/** Renders one page of `lastResults` (1-indexed) and updates pagination/URL. */
function renderPage(page, opts) {
  opts = opts || {};
  const totalPages = Math.max(1, Math.ceil(lastResults.length / RESULTS_PER_PAGE));
  page = Math.min(Math.max(1, page), totalPages);

  const start = (page - 1) * RESULTS_PER_PAGE;
  const end = start + RESULTS_PER_PAGE;
  const pageResults = lastResults.slice(start, end);

  renderResults(pageResults);
  renderPagination(page, totalPages);

  if (opts.updateUrl) updateUrl(lastQuery, page);
}

function renderResults(pageResults) {
  const searchResults = document.getElementById("search-results");
  const templateDefinition = document.getElementById("search-result-template").innerHTML;
  searchResults.innerHTML = "";

  if (lastResults.length === 0) {
    renderEmptyState();
    return;
  }

  pageResults.forEach((result, key) => {
    const item = result.item;
    const snippet = buildSnippet(item.contents, result.matches);
    let tags = "";
    (item.tags || []).forEach(function (tag) {
      tags += `<a href="/tags/${escapeHtml(encodeURIComponent(tag))}">#${escapeHtml(tag)}</a> `;
    });

    const output = render(templateDefinition, {
      key,
      title: escapeHtml(item.title),
      link: escapeAttribute(item.permalink),
      tags,
      categories: item.categories,
      snippet
    });
    searchResults.insertAdjacentHTML("beforeend", output);

    try {
      const instance = new Mark(document.getElementById(`summary-${key}`));
      instance.mark(lastQuery, { separateWordSearch: true, accuracy: "partially" });
    } catch (e) {
      console.error("Highlighting error:", e);
    }
  });
}

/**
 * Builds a snippet centered on the best available Fuse match inside
 * `contents`, instead of always showing the first N characters (which,
 * for a long article, usually shows the intro paragraph with nothing to
 * highlight when the actual match is much further down the page).
 */
function buildSnippet(contents, matches) {
  if (!contents) return "";

  let matchStart = 0;
  const contentsMatch = (matches || []).find(function (m) { return m.key === "contents"; });
  if (contentsMatch && contentsMatch.indices && contentsMatch.indices.length > 0) {
    matchStart = contentsMatch.indices[0][0];
  }

  const start = Math.max(0, matchStart - SUMMARY_RADIUS);
  const end = Math.min(contents.length, matchStart + SUMMARY_RADIUS);
  const prefix = start > 0 ? "&hellip;" : "";
  const suffix = end < contents.length ? "&hellip;" : "";

  return prefix + escapeHtml(contents.substring(start, end)) + suffix;
}

function renderPagination(page, totalPages) {
  const paginationContainer = document.getElementById("search-pagination");
  if (!paginationContainer) return;
  paginationContainer.innerHTML = "";
  if (totalPages <= 1) return;

  const encodedQuery = encodeURIComponent(lastQuery);
  for (let i = 1; i <= totalPages; i++) {
    const link = document.createElement("a");
    link.href = `?q=${encodedQuery}&page=${i}`;
    link.dataset.page = String(i);
    link.textContent = String(i);
    if (i === page) link.classList.add("active");
    paginationContainer.appendChild(link);
  }
}

function renderEmptyState() {
  const searchResults = document.getElementById("search-results");
  if (!searchResults) return;
  const paginationContainer = document.getElementById("search-pagination");
  if (paginationContainer) paginationContainer.innerHTML = "";

  if (lastQuery && lastQuery.length >= MIN_QUERY_LENGTH) {
    searchResults.innerHTML = `<p class="search-results-empty">No results found for "${escapeHtml(lastQuery)}". Try a different word or phrase, or see <a href="/tags/">all tags</a>.</p>`;
  } else {
    searchResults.innerHTML = '<p class="search-results-empty">Please enter a word or phrase above, or see <a href="/tags/">all tags</a>.</p>';
  }
}

function showError() {
  const searchResults = document.getElementById("search-results");
  if (!searchResults) return;
  searchResults.innerHTML = '<p class="search-results-error">Something went wrong while searching. Please try again in a moment.</p>';
}

function hideError() {
  const errorNode = document.querySelector(".search-results-error");
  if (errorNode) errorNode.remove();
}

/** Reflects the current query/page into the URL bar without a page reload. */
function updateUrl(query, page) {
  const params = new URLSearchParams();
  if (query) params.set("q", query);
  if (page && page > 1) params.set("page", String(page));
  const query_string = params.toString();
  const newUrl = location.pathname + (query_string ? `?${query_string}` : "");
  history.replaceState(null, "", newUrl);
}

/** Minimal template engine: ${key} substitution and ${isset key}...${end} blocks. */
function render(templateString, data) {
  let copy = templateString;
  const conditionalPattern = /\$\{\s*isset ([a-zA-Z]*)\s*\}([\s\S]*?)\$\{\s*end\s*\}/g;
  let match;
  while ((match = conditionalPattern.exec(templateString)) !== null) {
    copy = copy.replace(match[0], data[match[1]] ? match[2] : "");
  }
  for (const [key, value] of Object.entries(data)) {
    const find = `\\$\\{\\s*${key}\\s*\\}`;
    const re = new RegExp(find, "g");
    copy = copy.replace(re, value == null ? "" : value);
  }
  return copy;
}

// =============================
// Helpers
// =============================
function show(elem) {
  if (elem) elem.style.display = "block";
}

function hide(elem) {
  if (elem) elem.style.display = "none";
}

/** Escapes text for safe insertion as HTML content (between tags). */
function escapeHtml(str) {
  if (str == null) return "";
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

/** Escapes text for safe insertion inside an HTML attribute value (e.g. href="..."). */
function escapeAttribute(str) {
  return escapeHtml(str);
}
