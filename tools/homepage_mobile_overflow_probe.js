// Evaluate on a rendered homepage after setting a CSS viewport (320, 375, 480, 768).
(() => {
  const viewport = document.documentElement.clientWidth;
  const form = document.querySelector('.search-form form');
  const input = form.querySelector('#search-query');
  const button = form.querySelector('button[type="submit"]');
  const copyright = document.querySelector('.footer__copyright');
  const copyrightLink = copyright.querySelector('a[href]');
  const result = {
    viewport,
    documentWidth: document.documentElement.scrollWidth,
    formRight: form.getBoundingClientRect().right,
    inputWidth: input.getBoundingClientRect().width,
    buttonRight: button.getBoundingClientRect().right,
    copyrightRight: copyright.getBoundingClientRect().right,
    titleOverflow: [...document.querySelectorAll('.posts .post-title a')]
      .filter((link) => link.getBoundingClientRect().right > viewport)
      .map((link) => link.textContent.trim().slice(0, 80)),
    searchAction: form.getAttribute('action'),
    copyrightLink: copyrightLink?.getAttribute('href'),
  };
  if (result.documentWidth > viewport || result.formRight > viewport || result.buttonRight > viewport || result.copyrightRight > viewport || result.titleOverflow.length) {
    throw Error(`Homepage overflows horizontally: ${JSON.stringify(result)}`);
  }
  if (result.inputWidth < 180 || new URL(result.searchAction, document.baseURI).pathname !== '/search' || !result.copyrightLink) {
    throw Error(`Homepage search/footer feature changed: ${JSON.stringify(result)}`);
  }
  return result;
})()