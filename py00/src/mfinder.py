import re

def check_m_pattern(filename):
    try:
        with open(filename, 'r') as file:
            # Считываем содержимое файла
            content = file.read()
            
            # Определяем регулярное выражение для шаблона "M"
            m_pattern = r"^\*[^*][^*][^*]\*\n\*\*[^*]\*\*\n\*[^*]\*[^*]\*$"
            
            # Проверяем соответствие содержимого файла регулярному выражению
            if re.match(m_pattern, content):
                print("True")
            else:
                print("False")
    except FileNotFoundError:
        print("Error: File not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_m_pattern("m.txt")

