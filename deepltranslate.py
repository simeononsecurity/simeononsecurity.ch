import os
import argparse
import deepl
from dotenv import load_dotenv

load_dotenv()

DEEPL_API_KEY = os.environ.get('deeplapikey')

def translate_text(text, target_lang):
    # Send the API request and handle the response
    response = deepl.translate.translate(text, target_lang, DEEPL_API_KEY)
    if response[0]['error'] is None:
        return response[0]['text']
    else:
        raise ValueError(response[0]['error']['message'])

def translate_file(file_path, target_lang):
    with open(file_path, 'r') as f:
        content = f.read()
    translated_content = translate_text(content, target_lang)
    return translated_content

def translate_files_in_directory(dir_path, target_lang):
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for filename in filenames:
            if filename == 'index.en.md':
                source_file_path = os.path.join(dirpath, filename)
                target_file_path = os.path.join(dirpath, f'index.{target_lang}.md')
                translated_content = translate_file(source_file_path, target_lang)
                with open(target_file_path, 'w') as f:
                    f.write(translated_content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dir_path', help='The path to the directory containing the files to be translated.')
    parser.add_argument('target_lang', help='The target language code (e.g., ES for Spanish).')
    args = parser.parse_args()

    translate_files_in_directory(args.dir_path, args.target_lang)
