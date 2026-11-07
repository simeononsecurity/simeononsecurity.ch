// Run in a browser on the rendered career article at a 320px CSS viewport.
(() => {
  const viewport = document.documentElement.clientWidth;
  const article = document.querySelector('.post-content');
  const grid = document.querySelector('#related-section .related-posts-list');
  const tables = [...article.querySelectorAll('table')];
  const result = {
    viewport,
    documentWidth: document.documentElement.scrollWidth,
    articleWidth: article.clientWidth,
    articleScrollWidth: article.scrollWidth,
    relatedColumns: getComputedStyle(grid).gridTemplateColumns,
    relatedRight: Math.round(grid.firstElementChild.getBoundingClientRect().right),
    tocOverflow: [...document.querySelectorAll('#TableOfContents a')]
      .filter((link) => link.getBoundingClientRect().right > viewport)
      .map((link) => link.textContent.trim()),
    tables: tables.map((table) => ({
      clientWidth: table.clientWidth,
      scrollWidth: table.scrollWidth,
      overflowX: getComputedStyle(table).overflowX,
    })),
    code: [...article.querySelectorAll('pre')].map((pre) => ({
      clientWidth: pre.clientWidth,
      scrollWidth: pre.scrollWidth,
      overflowX: getComputedStyle(pre).overflowX,
    })),
  };
  if (viewport !== 320) throw Error(`Expected 320px viewport: ${JSON.stringify(result)}`);
  if (result.documentWidth > viewport || result.relatedRight > viewport || result.articleScrollWidth > result.articleWidth || result.tocOverflow.length) {
    throw Error(`Page overflows horizontally: ${JSON.stringify(result)}`);
  }
  if (!result.tables.length || result.tables.some((table) => table.overflowX !== 'auto' || table.scrollWidth <= table.clientWidth)) {
    throw Error(`Wide tables must remain horizontally scrollable: ${JSON.stringify(result)}`);
  }
  if (document.documentElement.lang === 'en' && !result.code.some((pre) => pre.scrollWidth > pre.clientWidth && pre.overflowX === 'auto')) {
    throw Error(`Wide code must remain horizontally scrollable: ${JSON.stringify(result)}`);
  }
  return result;
})()