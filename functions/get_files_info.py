def get_files_info(working_directory, directory=None):
    if !os.path.abspath(directory).startswith(working_directory):
        raise Exception(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    if !os.path.isdir(directory):
        raise Exception(f'Error: "{directory}" is not a directory')

    paths = os.listdir(directory)

    for path in paths:
        