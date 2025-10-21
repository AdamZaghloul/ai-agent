import os, subprocess

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
        
        cmd = ["python", file_path] + args

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