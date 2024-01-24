import os

def find_siblings_with_dist_index(directory='.'):
    # Get sibling folder names
    sibling_folders = [folder for folder in os.listdir(directory) if os.path.isdir(os.path.join(directory, folder))]

    # Filter folders with 'dist' subfolder containing 'index.html'
    filtered_folders = []
    for folder in sibling_folders:
        dist_path = os.path.join(directory, folder, 'dist')
        index_html_path = os.path.join(dist_path, 'index.html')
        if os.path.exists(dist_path) and os.path.isdir(dist_path) and os.path.exists(index_html_path):
            filtered_folders.append(folder)

    return filtered_folders

def generate_readme(directory='.'):
    # Get sibling folders with 'dist' and 'index.html'
    filtered_folders = find_siblings_with_dist_index(directory)
    # print(filtered_folders)

    # Create README content with folder names and links to 'dist' in a table
    readme_content = "# Sibling Folders with dist/index.html\n\n"
    readme_content += "| Repo | Live preview |\n"
    readme_content += "|-------------|-----------|\n"
    for folder in filtered_folders:
        # dist_link = f"[Live Preview ]({os.path.join(folder, 'dist')})"
        dist_link = f"[Live Preview ](https://sharif-22.github.io/cyberdude-challenges/javascript/02-javascript-dom/{folder}/dist)"
# https://sharif-22.github.io/cyberdude-challenges/javascript/02-javascript-dom/11-split-calculator-app/dist/
        repoLink = f"https://github.com/sharif-22/cyberdude-challenges/tree/main/javascript/02-javascript-dom/{folder}"
        readme_content += f"| [{folder}]({repoLink}) | {dist_link} |\n"

    # Write content to README.md
    with open(os.path.join(directory, "README.md"), "w") as readme_file:
        readme_file.write(readme_content)

if __name__ == "__main__":
    # Get user input for directory
    user_directory = input("Enter the directory path (press Enter for current directory): ").strip()

    # Use current directory if no input is provided
    directory_path = user_directory if user_directory else '.'

    # Generate README in the specified directory
    generate_readme(directory_path)

    print(f"README.md generated in {directory_path}.")
