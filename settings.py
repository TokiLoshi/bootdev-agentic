from google.genai import types

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

# File info Schema 
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

# File content Schema 
schema_get_file_content = types.FunctionDeclaration(
  name="get_file_content",
  description="returns the contents of the file text truncated to ten thousand characters, constrained to the working directory.",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "file_path": types.Schema(
        type=types.Type.STRING,
        description="The file path to list content from, relative to the working directory. If not provided it returns an error string"
      )
    }
  )
)

# Run File Schema 
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs the function at the specified file path and returns a formatted standard in and standard out. If the extension is not a python file or the file is not in the designated working directory a string error is returned.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to run the function relative to the working directory. If not provided it returns an error string.",
            ),
        },
    ),
)

# Overwrite file schema 
schema_overwrite_file = types.FunctionDeclaration(
    name="overwrite_file",
    description="Replaces the content at the provided file path with the content in the parameters, relative to the working directory. If the file is not within the designated working directory an error string is returned. If the file path does not exist the directory is created.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to run the function relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The file content to write into the file as new text or to replace any existing text.",
            ),
        },
    ),
)

# Available functions
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_overwrite_file
    ]
)