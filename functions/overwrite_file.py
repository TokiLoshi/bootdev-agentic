import os

def overwrite_file(working_directory, file_path, content):
  # If the file path is outside of the working directory 
  abs_working_dir = os.path.abspath(working_directory)
  abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
 
  
  if not abs_file_path.startswith(abs_working_dir):
    return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

  target_file = abs_file_path  

  try:
    target_dir = os.path.dirname(target_file)
    file_exists = os.path.exists(target_dir)
    
    if not file_exists:
      os.makedirs(target_dir, exist_ok=True)
    file_exists = os.path.exists(file_path)
    print(f"After making dir File exists? {file_exists}")
    
    with open(target_file, "w") as f:
      f.write(content)
    return f'Successfully wrote to "{target_file}" ({len(content)} bytes written)'
  except Exception as e:
    return f"Error creating / writing to file: {e}"