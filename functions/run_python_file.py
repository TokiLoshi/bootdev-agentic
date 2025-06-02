import os 

def run_python_file(working_directory, file_path):
  # If the file path is outside of the working directory 
  abs_working_dir = os.path.abspath(working_directory)
  abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
 
  
  if not abs_file_path.startswith(abs_working_dir):
    return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

  # If the file doesn't exist return an error
  target_file = abs_file_path  
  if not os.path.exists(target_file):
    return f'Error: File "{file_path}" not found.'
  
  # if the file doesn't have a .py extension return error 
  extension = target_file[:-2]
  if extension != ".py":
    f'Error: "{file_path}" is not a Python file.'

  # Use subprocess.run 
  # Set a 30 second time out to prevent infinite execution
  # Capture both stdout and stderr 
  # Set the working directory properly 

  # Format output to include stdout (prefixed with STDout)
  # Stderr prefixed with STDERR
  # if process exits with non-zer include "Process exited with code X"
  # If no proces produced return "No output produced"
  # for any errors: f"Error: executing Python file: {e}" 