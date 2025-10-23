import os
from google.genai import types

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

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to the file in the specified directory, constrained to the working directory. Any existing content in the file is overwritten and the file is created if it does not exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write to or overwrite, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the specified file.",
            ),
        },
    ),
)