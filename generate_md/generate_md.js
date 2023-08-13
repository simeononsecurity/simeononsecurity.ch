const fs = require('fs');
const axios = require('axios');
const xml2js = require('xml2js');

async function fetchSitemap(url) {
  const response = await axios.get(url);
  return response.data;
}

async function parseSitemap(sitemapXml) {
  const parser = new xml2js.Parser();
  const parsedData = await parser.parseStringPromise(sitemapXml);
  return parsedData.urlset.url;
}

function generateMarkdown(urls) {
  const markdownContent = urls.map(urlData => {
    const title = urlData['news:title'][0];
    const url = urlData.loc[0];
    return `- [${title}](${url})`;
  }).join('\n');

  fs.writeFileSync('sitemap_links.md', markdownContent);
}

async function run() {
  const sitemapUrl = 'https://simeononsecurity.ch/sitemap.xml';
  const sitemapXml = await fetchSitemap(sitemapUrl);
  const parsedUrls = await parseSitemap(sitemapXml);
  generateMarkdown(parsedUrls);
}

run().catch(error => {
  console.error(error);
  process.exit(1);
});
