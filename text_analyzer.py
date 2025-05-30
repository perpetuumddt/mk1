import re

def text_reader(file_path):
    try:
        # Read the file
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        # Count sentences (split by . ! ? ...)
        sentences = re.split(r'[.!?]+', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        sentence_count = len(sentences)
        
        # Count words (split by space , : ;)
        words = re.split(r'[,\s:;]+', text)
        words = [w.strip() for w in words if w.strip()]
        word_count = len(words)
        
        return {
            'word_count': word_count,
            'sentence_count': sentence_count
        }

    except FileNotFoundError:
        print(f"Помилка: '{file_path}' - файл не знадено.")
        return None

def main():
    # Get file path from user
    file_path = input("Enter the path to your .txt file: ")

    if not file_path.lower().endswith('.txt'):
        print("Помилка: файл має мати .txt розширення")
        return

    result = text_reader(file_path)
    
    if result:
        print(f"\nРезультат аналізу '{file_path}':")
        print(f"Кількість слів: {result['word_count']}")
        print(f"Кількість речень: {result['sentence_count']}")

if __name__ == "__main__":
    main() 