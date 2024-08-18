import os
import difflib

def rename_files_in_directory_with_match(directory, new_names):
    existing_files = os.listdir(directory)
    
    existing_bases = [os.path.splitext(f)[0] for f in existing_files]
    
    for new_name_base in new_names:
        closest_match = difflib.get_close_matches(new_name_base, existing_bases, n=1, cutoff=0.3)
        
        if closest_match:
            original_file = next(f for f in existing_files if os.path.splitext(f)[0] == closest_match[0])
            
            _, extension = os.path.splitext(original_file)
            
            new_filename = new_name_base + extension
            
            old_file_path = os.path.join(directory, original_file)
            new_file_path = os.path.join(directory, new_filename)
            
            if os.path.exists(old_file_path):
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {original_file} -> {new_filename}")
            else:
                print(f"File '{original_file}' not found in {directory}")
        else:
            print(f"No close match found for '{new_name_base}' in {directory}")

directory_path = 'C:/Users/example/example'

new_filenames = ['example_example', 'example_1', 'example3', 'example_example4']

rename_files_in_directory_with_match(directory_path, new_filenames)

