const summaryInclude = 180;
const resultsPerPage = 10; // Set the number of search results to show per page

const fuseOptions = {
  shouldSort: true,
  includeMatches: true,
  includeScore: true,
  tokenize: true,
  location: 0,
  distance: 100,
  minMatchCharLength: 1,
  keys: [
    {name: "title", weight: 0.45},
    {name: "contents", weight: 0.6},
    {name: "tags", weight: 0.1},
    {name: "categories", weight: 0.05}
  ]
};

// =============================
// Search
// =============================

const inputBox = document.getElementById('search-query');
if (inputBox !== null) {
  const searchQuery = param("q");
  if (searchQuery) {
    inputBox.value = searchQuery || "";
    const page = parseInt(param("page")) || 1; // Get the page number from the URL query string
    executeSearch(searchQuery, page);
  } else {
    document.getElementById('search-results').innerHTML = '<p class="search-results-empty">Please enter a word or phrase above, or see <a href="/tags/">all tags</a>.</p>';
  }
}

async function executeSearch(searchQuery, page) {

  show(document.querySelector('.search-loading'));

  try {
    const response = await fetch('/index.json');
    if (response.status !== 200) {
      console.log(`Looks like there was a problem. Status Code: ${response.status}`);
      return;
    }
    const pages = await response.json();
    const fuse = new Fuse(pages, fuseOptions);
    const result = fuse.search(searchQuery);
    populateResults(result, page);
  } catch (err) {
    console.log('Fetch Error :-S', err);
  } finally {
    hide(document.querySelector('.search-loading'));
  }
}

function populateResults(results, page) {
  const searchQuery = document.getElementById("search-query").value;
  const searchResults = document.getElementById("search-results");
  const templateDefinition = document.getElementById("search-result-template").innerHTML;
  const start = (page - 1) * resultsPerPage;
  const end = start + resultsPerPage;
  const paginatedResults = results.slice(start, end);
  searchResults.innerHTML = "";
  paginatedResults.forEach((value, key) => {
    const contents = value.item.contents;
    let snippet = "";
    const snippetHighlights = [];
    snippetHighlights.push(searchQuery);
    snippet = `${contents.substring(0, summaryInclude * 2)}&hellip;`;
    let tags = "";
    value.item.tags?.forEach(element => {
      tags = `${tags}<a href='/tags/${element}'>#${element}</a> `;
    });
    const output = render(templateDefinition, {
      key,
      title: value.item.title,
      link: value.item.permalink,
      tags,
      categories: value.item.categories,
      snippet
    });
    searchResults.innerHTML += output;
    snippetHighlights.forEach((snipvalue, snipkey) => {
      try {
        const instance = new Mark(document.getElementById(`summary-${key}`));
        instance.mark(snipvalue);
      } catch (e) {
        console.error(e);
      }
    });
  });
  const totalPages = Math.ceil(results.length / resultsPerPage);
  const paginationContainer = document.getElementById("search-pagination");
  if (totalPages > 1) {
    paginationContainer.innerHTML = "";
    for (let i = 1; i <= totalPages; i++) {
      const link = document.createElement("a");
      link.href = `?q=${searchQuery}&page=${i}`;
      link.innerHTML = i;
      if (i === page) {
        link.classList.add("active");
      }
      paginationContainer.appendChild(link);
    }
  } else {
    paginationContainer.innerHTML = "";
  }

  const remainingResults = results.slice(end);
  if (remainingResults.length > 0) {
    const remainingResultsContainer = document.createElement("div");
    remainingResultsContainer.classList.add("search-results-remaining");
    remainingResultsContainer.innerHTML = `<p>Showing the first ${resultsPerPage * totalPages} results. ${remainingResults.length} additional results are available. <a href="?q=${searchQuery}&page=${page + 1}">View them</a>.</p>`;
    searchResults.appendChild(remainingResultsContainer);
  }
}

function render(templateString, data) {
  let copy = templateString;
  const conditionalPattern = /\$\{\s*isset ([a-zA-Z]*) \s*\}(.*)\$\{\s*end\s*}/g;
  while ((match = conditionalPattern.exec(templateString)) !== null) {
    if (data[match[1]]) {
      copy = copy.replace(match[0], match[2]);
    } else {
      copy = copy.replace(match[0], '');
    }
  }
  for (const [key, value] of Object.entries(data)) {
    const find = `\\$\\{\\s*${key}\\s*\\}`;
    const re = new RegExp(find, 'g');
    copy = copy.replace(re, value);
  }
  return copy;
}

// Helper Functions
function show(elem) {
  elem.style.display = 'block';
}

function hide(elem) {
  elem.style.display = 'none';
}

function param(name) {
  return decodeURIComponent((location.search.split(name + '=')[1] || '').split('&')[0]).replace(/\+/g, ' ');
}
