import os
from config import *

def get_file_content(working_directory, file_path):
    contents = ""

    try:
        full_path = os.path.join(working_directory, file_path)
        if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
            contents += f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
            return contents
        if not os.path.isfile(full_path):
            contents += f'Error: File not found or is not a regular file: "{file_path}"'
            return contents

        with open(full_path, "r") as f:
            contents = f.read(MAX_CHARS)

    except Exception as e:
        contents += f'Error: {e}'

    return contents.strip()