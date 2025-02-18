import json
import re
import subprocess
from openai import OpenAI
from dotenv import load_dotenv
import os

def initialize_openai_client():
    load_dotenv()
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPEN_ROUTER_API"),
    )
    return client

def create_completion(client, prompt):
    completion = client.chat.completions.create(
        model="google/gemini-2.0-pro-exp-02-05:free",
        messages=[
            {
                "role": "developer",
                "content": """You are an assistant with access to a Python execution environment.
                Your response **must** always be in JSON format.  
                - If the question can be solved with code, return:  
                  ```json
                  {"type": "code", "code": "<generated Python code>"}
                  ```  
                - If it does not require code, return:  
                  ```json
                  {"type": "text", "answer": "<natural language response>"}
                  ```  
                - If multiple questions with different types are asked, return 
                the non code response also in the code as a print statement.
                Prefer to generate code whenever possible.""",
            },
            {
                "role": "user",
                "content": prompt,
            }
        ]
    )
    return completion

def parse_response(raw_response):
    if raw_response.startswith("```json") and raw_response.endswith("```"):
        raw_response = re.sub(r"^```json|\n```$", "", raw_response).strip()
    return json.loads(raw_response)

def execute_code(generated_code):
    result = subprocess.run(
        ["python", "-c", generated_code], capture_output=True, text=True, timeout=5
    )
    return result.stdout.strip() if result.stdout else result.stderr.strip()

def refine_answer(client, prompt, generated_code, execution_result):
    refinement_prompt = {
        "role": "user",
        "content": f"""You were asked a question :
        {prompt}
        You generated the following Python code to solve it:
        ```python
        {generated_code}
        ```
        The execution result was:
        ```
        {execution_result}
        ```
        Now, based on this, provide a final, well-informed answer to the user's original question.
        """
    }
    refined_completion = client.chat.completions.create(
        model="google/gemini-2.0-pro-exp-02-05:free",
        messages=[refinement_prompt]
    )
    return refined_completion.choices[0].message.content.strip()

def main():
    prompt = """How many Rs in the word Strrawberry?"""
    client = _clientinitialize_openai()
    completion = create_completion(client, prompt)
    raw_response = completion.choices[0].message.content
    response_data = parse_response(raw_response)

    if response_data.get("type") == "code":
        generated_code = response_data.get("code", "")
        print("Generated Code:\n", generated_code)
        execution_result = execute_code(generated_code)
        print("Execution Result:\n", execution_result)
        final_answer = refine_answer(client, prompt, generated_code, execution_result)
        print("\nFinal Answer:\n", final_answer)
    elif response_data.get("type") == "text":
        answer = response_data.get("answer", "")
        print("Answer:\n", answer)
    else:
        print("Unexpected response format:", response_data)

if __name__ == "__main__":
    main()