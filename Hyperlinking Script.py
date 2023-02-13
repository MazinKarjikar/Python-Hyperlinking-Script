import os

def replace_string_with_latex_link(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()

    contents = contents.replace("hamming distance", '\\href{https://google.com/search?q=hamming+distance}{hamming distance}')

    with open(file_path, 'w') as file:
        file.write(contents)

for root, dirs, files in os.walk("."):
    for filename in files:
        if filename.endswith('.yaml'):
            replace_string_with_latex_link(os.path.join(root, filename))