from google.genai import types
from functions.get_file_content import get_file_content 
from functions.get_files_info import get_files_info 
from functions.overwrite_file import overwrite_file
from functions.run_python_file import run_python_file

def call_function(function_call_part, verbose=False):
  
  if verbose:
    print(f"Calling function: {function_call_part.name}({function_call_part.args})")
  else:
    print(f" - Calling function: {function_call_part.name}")

  FUNCTIONS = {
    "get_file_content": get_file_content,
    "get_files_info": get_files_info, 
    "overwrite_file": overwrite_file, 
    "run_python_file": run_python_file,
  }


  func = FUNCTIONS.get(function_call_part.name)
  if func is None: 
      return types.Content(
      role="tool",
      parts=[
          types.Part.from_function_response(
              name=function_call_part.name,
              response={"error": f"Unknown function: {function_call_part.name}"},
          )
        ],
      )
  else:
    function_args = dict(function_call_part.args)
    function_args["working_directory"] = "./calculator"
    result = func(** function_args)
    return types.Content(
      role="tool",
      parts=[
          types.Part.from_function_response(
              name=function_call_part.name,
              response={"result": result},
          )
      ],
  )