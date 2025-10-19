import os

def get_files_info(working_directory, directory=None):

    displayPath = ""

    if directory == ".":
            displayPath = "current"
    else:
        displayPath = f"'{directory}'"

    contents = f"Result for {displayPath} directory:\n"

    try:
        full_path = os.path.join(working_directory, directory)
        if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
            contents += f'    Error: Cannot list "{directory}" as it is outside the permitted working directory'
            return contents
        if not os.path.isdir(full_path):
            contents += f'    Error: "{directory}" is not a directory'
            return contents

        paths = os.listdir(full_path)

        for path in paths:
            contents += f'  - {os.path.basename(os.path.join(full_path, path))}: file_size={os.path.getsize(os.path.join(full_path, path))} bytes, is_dir={os.path.isdir(os.path.join(full_path, path))}\n'
    
    except Exception as e:
        contents += f'Error: {e}'

    return contents.strip()