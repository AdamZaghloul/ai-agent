import os, subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    contents = ""

    try:
        full_path = os.path.join(working_directory, file_path)
        if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
            contents += f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
            return contents
        
        if not os.path.isfile(full_path):
            contents += f'Error: File "{file_path}" not found.'
            return contents
        
        if not full_path.endswith(".py"):
            contents += f'Error: "{file_path}" is not a Python file.'
            return contents
        
        cmd = ["python3", file_path] + args

        process = subprocess.run(cmd, timeout=30, capture_output=True, text=True, cwd=working_directory)

        if process.returncode != 0:
            contents = f'Process exited with code {process.returncode}'
            return contents
        
        if process is None:
            contents = 'No output produced.'
            return contents
        
        contents += f'STDOUT:{process.stdout} STDERR:{process.stderr}'

    except Exception as e:
        contents += f"Error: executing Python file: {e}"

    return contents.strip()

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the python code in the file in the specified directory, constrained to the working directory. The file must exist and be a python (.py) file. Includes optional arguments but If none are provided omit the arguments and run anyway. Do not ask for arguments.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Any optional arguments required to run the python file. If none are provided omit the arguments and run anyway. Do not ask for arguments.",
                items=types.Schema(
                    type=types.Type.OBJECT,
                    properties={
                        "item": types.Schema(
                            type=types.Type.STRING,
                            description="Each argument passed to the funcion. If none are provided omit the arguments and run anyway. Do not ask for arguments.",
                        ),
                    },
                )
            ),
        },
    ),
)