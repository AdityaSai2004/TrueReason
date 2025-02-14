# TrueReason

Note : This project is a work in progress and will be updated continously. PRs are welcome.Special thanks to Chatgpt.

## Recursive Reasoning Framework

This project aims to build a framework for recursive and truly reasoning models. Instead of generating text responses to logical or mathematical questions, the model generates executable code. The code is then executed, and the results are sent back to the model for further explanation based on the generated answer.

## Prerequisites

- Python 3.11.5
- Jupyter Notebook
- OpenAI Python client library

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/AdityaSai2004/TrueReason.git
   cd TrueReason
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```sh
   pip install openai jupyter python-dotenv
   ```

## Usage

1. Open the Jupyter Notebook:

   ```sh
   jupyter notebook mk1.ipynb
   ```

2. Create your .env file and add your API key in it.

   ```sh
   OPEN_ROUTER_API=your-api-key-here
   ```

3. Add your OpenAI API key in the `client` initialization section:

   ```python
   client = OpenAI(
     base_url="https://openrouter.ai/api/v1",
     api_key=os.getenv("OPEN_ROUTER_API"),
   )
   ```

4. Run the cells in the notebook to interact with the OpenAI API.

## Project Structure

- [mk1.ipynb]: The main Jupyter Notebook containing the code to interact with the OpenAI API and execute generated code.

## Workflow

1. **Prompt Submission**: The user submits a prompt to the OpenAI API.
2. **Response Handling**: The API returns a response. If the response contains code, it is extracted and executed.
3. **Execution**: The generated code is executed, and the results are captured.
4. **Refinement**: The execution results are sent back to the model for further explanation or refinement.
5. **Final Answer**: The model provides a final, well-informed answer based on the execution results.

## Example

Prompt:
How many Rs in the word Strawberry?

Generated Code:
word = "Strawberry"
count = word.lower().count('r')
print(count)

Execution Result:
3

Final Answer:
The word "Strawberry" contains 3 "R"s (or "r"s). This is because the code correctly converts the word to lowercase ("strawberry") and then counts the occurrences of 'r', finding three instances.
