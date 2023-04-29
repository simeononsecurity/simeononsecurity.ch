const { google } = require('googleapis');
const fs = require('fs');
const path = require('path');

// Set the folder path to search for .md files
const folderPath = 'C:\\Users\\Simeon\\Documents\\GitHub\\1-simeononsecurity.ch\\content';

// Set the language codes for each localization
const languageCodes = {
  ar: 'arabic',
  de: 'german',
  en: 'english',
  fr: 'french',
  hi: 'hindi',
  es: 'spanish'
  // Add more language codes as needed
};

// Set the Google Translate API credentials
const auth = new google.auth.GoogleAuth({
  keyFile: './.env.google',
  scopes: ['https://www.googleapis.com/auth/cloud-platform']
});

// Create a function to translate the frontmatter values for a file
async function translateFrontmatter(filePath, languageCode) {
  const fileName = path.basename(filePath);
  const index = fileName.indexOf('.');
  const prefix = fileName.slice(0, index + 1);
  const suffix = fileName.slice(index + 1);

  // Check if the file matches the language code
  if (suffix === `${prefix}${languageCode}.md`) {
    const fileContent = fs.readFileSync(filePath, 'utf8');
    const lines = fileContent.split('\n');

    // Find the frontmatter section
    let i = 0;
    for (; i < lines.length; i++) {
      if (lines[i] === '---') break;
    }
    i++; // Skip the opening '---'

    // Translate each frontmatter value
    while (i < lines.length && lines[i] !== '---') {
      const keyValue = lines[i].split(':');
      if (keyValue.length === 2) {
        const key = keyValue[0].trim();
        const value = keyValue[1].trim();
        const translation = await translateText(value, languageCode);
        lines[i] = `${key}: ${translation}`;
      }
      i++;
    }

    // Write the updated file content
    const updatedContent = lines.join('\n');
    fs.writeFileSync(filePath, updatedContent, 'utf8');
  }
}

// Create a function to translate text using the Google Translate API
async function translateText(text, targetLanguage) {
  const translate = google.translate({ version: 'v2', auth });
  const res = await translate.translate(text, targetLanguage);
  return res.data.translations[0].translatedText;
}

// Recursively search for .md files and translate their frontmatter values
async function translateFrontmatterInFolder(folderPath) {
  const files = fs.readdirSync(folderPath, { withFileTypes: true });

  for (const file of files) {
    const filePath = path.join(folderPath, file.name);
    if (file.isDirectory()) {
      await translateFrontmatterInFolder(filePath);
    } else if (file.name.endsWith('.md')) {
      for (const languageCode in languageCodes) {
        await translateFrontmatter(filePath, languageCode);
      }
    }
  }
}

// Call the main function
translateFrontmatterInFolder(folderPath);
