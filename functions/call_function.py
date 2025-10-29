import os, subprocess, functions.get_file_content, functions.get_files_info, functions.run_python_file, functions.write_file
from google.genai import types
from config import *

def call_function(function_call_part, verbose=False):
    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")


    result = ""
    args = function_call_part.args
    args["working_directory"] = WORKING_DIRECTORY
    print(function_call_part)

    match function_call_part.name:
        case "get_file_content":
            result = functions.get_file_content.get_file_content(**args)
        case "get_files_info":
            result = functions.get_files_info.get_files_info(**args)
        case "run_python_file":
            result = functions.run_python_file.run_python_file(**args)
        case "write_file":
            result = functions.write_file.write_file(**args)
        case _:
            return types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=function_call_part.name,
                        response={"error": f"Unknown function: {function_call_part.name}"},
                    )
                ],
            )
    
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": result},
            )
        ],
    )