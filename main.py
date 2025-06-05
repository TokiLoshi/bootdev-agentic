import os 
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
import settings 
from functions.call_function import call_function

def main():
  print("=========== Agentic boot ==============\n")

  # Load environment 
  load_dotenv()
  
  # Get arguments and check prompt formatting is correct 
  args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

  if not args:
    print("\nUsage: python main.py 'your prompt here'")
    print("Example: python main.py 'Why is bootdev the best?'")
    print(f"No argument provided ")
    sys.exit(1) 

  key = os.environ.get("GEMINI_API_KEY")
  if not key:
    print("Error: GEMINI_API_KEY not loaded into environment variables")
    sys.exit(1)

  client = genai.Client(api_key=key)

  # Format user prompt 
  user_prompt = " ".join(args)
  verbose = "--verbose" in sys.argv 
  if verbose:
    print(f"User prompt: {user_prompt}\n")


  messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
  ]

  model_name = "gemini-2.0-flash-001"
  model_config=types.GenerateContentConfig(
    tools=[settings.available_functions], system_instruction=settings.system_prompt
  )
  
  # Create a loop that iterates 20 times 
  MAX_ITERATIONS=20 

  for i in range(MAX_ITERATIONS):
    response = client.models.generate_content(
      model=model_name, 
      contents=messages,
      config=model_config
    )

    if verbose:
      print(f"Iteration: {i + 1}")
      print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}\n")
      print(f"Response tokens: {response.usage_metadata.candidates_token_count}\n")


    if response.candidates:
      if verbose: 
        print(f"Adding {len(response.candidates)} to conversation")

      for candidate in response.candidates:
        messages.append(candidate.content)

    # Check if there are functions to execute
    if not response.function_calls:
      print("Agent completed. Final Response: \n")
      print(response.text)
      return response.text

    function_responses = []
    
    for function_call_part in response.function_calls:
      function_name = function_call_part.name
      function_args = function_call_part.args
      print(f"Calling function: {function_name}, with args: {function_args}\n")

      function_call_result = call_function(function_call_part, verbose)
      if (not function_call_result.parts or not function_call_result.parts[0].function_response):
        raise Exception("empty function call result")
      
      if verbose:
         print(f"->{function_call_result.parts[0].function_response.response}")
      
      function_responses.append(function_call_result.parts[0])
    
    if not function_responses:
      raise Exception("no function responses generated")
    

    for function_result in function_responses:
      messages.append(types.Content(
        role="tool", 
        parts=[function_result]
        ))
      if verbose:
        print(f"Added {len(function_responses)} function results to conversation\n")

  print("Max iterations reached - agent may not have competed the task")
  return None


 
  return

if __name__ == "__main__":
  main()
