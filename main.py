import os
import shutil
import argparse

#Парсер, що приймає на вхід два аргументи "source" та "destination"
def parse_args():
    parser = argparse.ArgumentParser(description="Recursively copy files and sort them by extension.")
    parser.add_argument("source", help="Path to the source directory")
    parser.add_argument("destination", nargs='?', default="dist", help="Path to the destination directory (default: 'dist')")
    return parser.parse_args()

#Функція, яка перевіряє чи є шляхи (якщо ні, то створює відповідну папку)
def recursive_copy(src, dist):
    if not os.path.exists(dist):
        os.makedirs(dist)

#Функція повертає список усіх файлів та піддиректорій у директорії "src"
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dist, item)
        
#Функція стає рекурсивною, якщо файл -- це папка, функція створюється наново всередині тієї папки        
        if os.path.isdir(s):
            recursive_copy(s, d)
        else:
            ext = os.path.splitext(item)[1][1:]
            target_dir = os.path.join(dist, ext)
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            shutil.copy2(s, target_dir)

#Головна програма
def main():
    args = parse_args()
    source_dir = args.source
    destination_dir = args.destination
    
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return
    
    try:
        recursive_copy(source_dir, destination_dir)
        print(f"Files copied and sorted successfully to '{destination_dir}'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
