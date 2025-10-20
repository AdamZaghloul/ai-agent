import os

def write_file(working_directory, file_path, content):
    contents = ""
    try:
        full_path = os.path.join(working_directory, file_path)
        if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
            contents += f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
            return contents
        
        if not os.path.exists(os.path.dirname(full_path)):
            os.makedirs(os.path.dirname(full_path))

        with open(full_path, "w") as f:
            f.write(content)
        
        contents += f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        
    except Exception as e:
        contents += f'Error: {e}'

    return contents.strip()