import os

def rename_files_in_directory(directory, old_names, new_names):
    if len(old_names) != len(new_names):
        print("Erro: As listas de nomes antigos e novos devem ter o mesmo tamanho.")
        return
    
    for old_name, new_name in zip(old_names, new_names):
        old_file_path = os.path.join(directory, old_name)
        new_file_path = os.path.join(directory, new_name)
        
        if os.path.exists(old_file_path):
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {old_name} -> {new_name}")
        else:
            print(f"File '{old_name}' not found in {directory}")

directory_path = 'C:/Users/henri/Downloads/i-mixed-up-scythe-and-sickle-lol-wmano/i_mixed_up_scythe_and_sickle_lol_wmano/assets/minecraft/textures/item'

old_filenames = ['example_example_old.png']
new_filenames = ['example_example_new.png']

rename_files_in_directory(directory_path, old_filenames, new_filenames)