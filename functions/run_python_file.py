import os 
import subprocess

def run_python_file(working_directory, file_path, args=None):
  # If the file path is outside of the working directory 
  abs_working_dir = os.path.abspath(working_directory)
  abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
 
  
  if not abs_file_path.startswith(abs_working_dir):
    return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

  # If the file doesn't exist return an error
  target_file = abs_file_path  
  if not os.path.exists(target_file):
    return f'Error: File "{file_path}" not found.'
  
  # if the file doesn't have a .py extension return error 
  extension = target_file[-3:]
  print("extension: ", extension)
  if extension != ".py":
    return f'Error: "{file_path}" is not a Python file.'

  # Use subprocess.run 
    # Set a 30 second time out to prevent infinite execution
  try:
    result = subprocess.run(["python", target_file] + (args or []), capture_output=True, timeout=30, text=True)
    print(f"Ran: {result}")
    
    # Capture both stdout and stderr 
    if result.stdout is None:
      return "No output produced"
    
    output = f"STDOUT: {result.stdout}" 
    print(f"Output: {output}")
    
    if result.stderr != "":
      return f"process exited with {result.stderr}"
      
    std_error = f"STDERR: {result.stderr}" 
    return f"Ran {output}, {std_error}"
  
  except Exception as e:
    return f"Error: executing Python file: {e}"
  
