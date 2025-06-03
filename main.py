import os 
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
import settings
 
# use client.models.generate content () method to get a response from gemin-2.0-flash-001 model
# parameters: model name (gemini-2.0-flash-001), contents (string)
# content prompt: "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
# generate_content metho returns GenerateContentReponse object 
# print the .text propery of the response to get the model's answer 

def main():
  print("=========== Agentic boot ==============\n")

  # Load environment 
  load_dotenv()
  key = os.environ.get("GEMINI_API_KEY")
  if not key:
    print("Error: GEMINI_API_KEY not loaded into environment variables")
    sys.exit(1)

  client = genai.Client(api_key=key)
  
  # Get arguments 
  args = sys.argv[1:]

  if not args:
    print("\nUsage: python main.py 'your prompt here'")
    print("Example: python main.py 'Why is bootdev the best?'")
    print(f"No argument provided ")
    sys.exit(1) 

  question =  "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
  user_prompt = " ".join(args)

  messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
  ]
  model_name = "gemini-2.0-flash-001"
  model_config=types.GenerateContentConfig(
    tools=[settings.available_functions], system_instruction=settings.system_prompt
)
  
  response = client.models.generate_content(
    model=model_name, contents=messages,
    config=model_config
  )

  functions_called = response.function_calls
  print(f"Functions called: {functions_called}")
  if functions_called:
    for function_details in functions_called:
      function_name = function_details.name
      function_args = function_details.args
      print(f"Calling function: {function_name}({function_args})")
    return 
  
  if "--verbose" in args:
    print(f"Working on: {user_prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

  print(f"{response.text}")

 
  return

if __name__ == "__main__":
  main()
