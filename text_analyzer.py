import re
import os

def text_reader(file_path):
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Count sentences (split by . ! ? ...)
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        sentence_count = len(sentences)
        
        # Count words (split by space and punctuation)
        words = re.findall(r'\b\w+\b', text)
        word_count = len(words)
        
        return {
            'word_count': word_count,
            'sentence_count': sentence_count
        }

    except FileNotFoundError:
        print(f"Помилка: '{file_path}' - файл не знадено.")
        return None

def list_available_files():
    files_dir = "files"
    if not os.path.exists(files_dir):
        print("Помилка: директорія 'files' не існує.")
        return []
    
    txt_files = [f for f in os.listdir(files_dir) if f.endswith('.txt')]
    return txt_files

def main():
    available_files = list_available_files()
    
    if not available_files:
        print("У директорії 'files' немає .txt файлів.")
        return
    
    print("\nДоступні файли:")
    for i, file in enumerate(available_files, 1):
        print(f"{i}. {file}")

    choice = input("\nВиберіть номер файлу для аналізу: ")
    choice = int(choice)

    if 1 <= choice <= len(available_files):
        selected_file = available_files[choice - 1]
        file_path = os.path.join("files", selected_file)

    result = text_reader(file_path)
    
    if result:
        print(f"\nРезультат аналізу '{selected_file}':")
        print(f"Кількість слів: {result['word_count']}")
        print(f"Кількість речень: {result['sentence_count']}")

if __name__ == "__main__":
    main() 