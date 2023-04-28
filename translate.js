// Imports the Google Cloud client library
const {
    Translate
} = require('@google-cloud/translate').v2;

const program = require('commander');
const fs = require('fs');
const path = require('path');

program
    .version('0.1.0')
    .option('-s, --source [path]', 'Add in the source file or directory.')
    .option('-t, --target [lang]', 'Add target language.')
    .parse(process.argv);

// Creates a client
const translate = new Translate({
    // credentials: {
    //     api_key: process.env.GOOGLE_APPLICATION_CREDENTIALS
    // },
    projectId: 'translate'
});

const options = {
    to: program.target,
};

async function translateLines(text) {
    if (text === ' ') return ' ';
    const output = [];
    let results = await translate.translate(text, options);

    let translations = results[0];
    translations = Array.isArray(translations) ?
        translations : [translations];

    translations.forEach((translation, i) => {
        output.push(translation)
    });

    return output.join('\n');
};

async function translateFile(filePath) {

    const text = fs.readFileSync(filePath, 'utf8');

    const lines = text.split('\n');
    let translateBlock = [];
    const output = [];

    let inHeader = false;
    let inCode = false;
    let inQuote = false;
    for (const line of lines) {
        // Don't translate preampble
        if (line.startsWith('---') && inHeader) {
            inHeader = false;
            output.push(line);
            continue;
        }
        if (line.startsWith('---')) {
            inHeader = true;
            output.push(line);
            continue;
        }
        if (inHeader) {
            output.push(line);
            continue;
        }

        // Don't translate code
        if (line.startsWith('```') && inCode) {
            inCode = false;
            output.push(line);
            continue;
        }
        if (line.startsWith('```')) {
            inCode = true;
            translateBlock = [await translateLines(translateBlock.join(' '))];
            output.push(line);
            continue;
        }
        if (inCode) {
            output.push(line);
            continue;
        }

        // Don't translate quotes
        if (inQuote && line.startsWith('>') === false) {
            inQuote = false;
        }
        if (line.startsWith('>')) {
            inQuote = true;
            translateBlock = [await translateLines(translateBlock.join(' '))];
            output.push(line);
        }
        if (inQuote) {
            output.push(line);
            continue;
        }

        if (line.charAt(0) === '\n' || line.length === 0) {
            translateBlock = [await translateLines(translateBlock.join(' '))];
            output.push(line);
            continue;
        }

        translateBlock.push(line);
    }

    if (translateBlock.length > 0) output.push(await translateLines(translateBlock.join(' ')))

    const newFileName = path.parse(filePath);
    const targetPath = path.join(path.dirname(filePath), `${newFileName.name}.${options.to}${newFileName.lang}${newFileName.ext}`);
    fs.writeFileSync(targetPath, output.join('\n'));
}


async function translateDirectory(dirPath) {
    const files = fs.readdirSync(dirPath);
    for (const file of files) {
        const filePath = path.join(dirPath, file);
        const stats = fs.statSync(filePath);
        if (stats.isDirectory()) {
            await translateDirectory(filePath);
        } else if (stats.isFile() && filePath.endsWith('index.en.md')) {
            await translateFile(filePath);
        }
    }
}

(async function () {
    const sourcePath = program.source;
    const stats = fs.statSync(sourcePath);

    if (stats.isDirectory()) {
        await translateDirectory(sourcePath);
    } else if (stats.isFile() && sourcePath.endsWith('index.en.md')) {
        await translateFile(sourcePath);
    } else {
        console.error('Invalid source file or directory.');
        program.outputHelp();
    }
})();