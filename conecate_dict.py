import os

PATH_FOLDER = "/content/OCRDataGenerator/dicts"

# Concatenate all the dictionary files into one
dicts_filename = os.listdir(PATH_FOLDER)
output_path = os.path.join(os.getcwd(), "all_dict.txt")
count = 0
with open(output_path, "w") as file_out:
    for dict_filename in dicts_filename:
        dict_path = os.path.join(PATH_FOLDER, dict_filename)
        with open(dict_path, "r") as file_input:
            for line in file_input:
                count += 1
                file_out.writelines(line.rstrip() + "\n")

print(count)
