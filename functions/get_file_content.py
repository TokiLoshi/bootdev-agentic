import os 

def get_file_content(working_directory, file_path):
  abs_working_dir = os.path.abspath(working_directory)
  target_dir = abs_working_dir 
  if file_path:
    target_dir = os.path.abspath(os.join(working_directory, file_path))
  if not target_dir.startswith(abs_working_dir):
    return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
  if not os.path.isfile(target_dir):
    return f'Error: File not found or is not a regular file: "{file_path}"'
  
  # read the file and contents as a string 
  # if the file is longer than 10000 characters trucate it to 10000 
  # append this message: [...File "{file_path}" truncated at 10000 characters]
  MAX_CHARS = 10000
  try:
    with open(file_path,  "r") as f:
      file_content_string = f.read(MAX_CHARS)
      if len(f) > MAX_CHARS:
        file_content_string += f"[...File '{file_path}' truncated at 10000 characters]"
  except Exception as e:
    return f"Error reading {file_path}: {e}"    
  
  return file_content_string

