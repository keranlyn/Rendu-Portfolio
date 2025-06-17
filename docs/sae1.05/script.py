import os
from pathlib import Path
import json
def build_file_list(base_directory):
    file_list = []
    base_path = Path(base_directory)

    for file in base_path.rglob('*'):
        if file.is_file():
            try:
                file_list.append([str(file.absolute()), file.stat().st_size])
            except (OSError, PermissionError):
                continue
    return file_list
def sort_file_list(file_list):
    return sorted(file_list, key=lambda x: x[1], reverse=True)
def get_top_100_files(file_list):
    return file_list[:100]
def save_to_json(file_list, output_file):
    for file in file_list:
        file[0] = file[0].replace('\\', '\\\\')

    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(file_list, json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    base_directory = input("Veuillez entrer le chemin du répertoire à analyser : ").strip()

    if not os.path.isdir(base_directory):
        print("Le répertoire spécifié n'existe pas.")
        exit()

    output_json = "top_100_files.json"
    file_list = build_file_list(base_directory)
    sorted_list = sort_file_list(file_list)
    top_100_files = get_top_100_files(sorted_list)
    save_to_json(top_100_files, output_json)

    print(f"Les 100 plus gros fichiers du répertoire '{base_directory}' ont été enregistrés dans '{output_json}'.")

