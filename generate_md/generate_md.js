const fs = require('fs');
const axios = require('axios');
const xml2js = require('xml2js');

async function fetchRssFeed(url) {
  const response = await axios.get(url);
  return response.data;
}

async function parseRssFeed(rssXml) {
  const parser = new xml2js.Parser();
  const parsedData = await parser.parseStringPromise(rssXml);
  return parsedData.rss.channel[0].item;
}

function generateMarkdown(items) {
  const markdownContent = items.map(item => {
    const title = item.title[0];
    const url = item.link[0];
    return `- [${title}](${url})`;
  }).join('\n');

  fs.writeFileSync('rss_links.md', markdownContent);
}

async function run() {
  const rssUrl = 'https://simeononsecurity.com/rssall.xml';
  const rssXml = await fetchRssFeed(rssUrl);
  const parsedItems = await parseRssFeed(rssXml);
  generateMarkdown(parsedItems);
}

run().catch(error => {
  console.error(error);
  process.exit(1);
});
