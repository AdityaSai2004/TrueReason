# Recursive Reasoning Framework

This project aims to build a framework for recursive and truly reasoning models. Instead of generating text responses to logical or mathematical questions, the model generates executable code. The code is then executed, and the results are sent back to the model for further explanation based on the generated answer.

## Prerequisites

- Python 3.11.5
- Jupyter Notebook
- OpenAI Python client library

## Installation

1. Clone the repository:

   ```sh
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```sh
   pip install openai jupyter
   ```

## Usage

1. Open the Jupyter Notebook:

   ```sh
   jupyter notebook mk1.ipynb
   ```

2. Add your OpenAI API key in the `client` initialization section:

   ```python
   client = OpenAI(
     base_url="https://openrouter.ai/api/v1",
     api_key="your-api-key-here",
   )
   ```

3. Run the cells in the notebook to interact with the OpenAI API.

## Project Structure

- [mk1.ipynb](http://_vscodecontentref_/0): The main Jupyter Notebook containing the code to interact with the OpenAI API and execute generated code.

## Workflow

1. **Prompt Submission**: The user submits a prompt to the OpenAI API.
2. **Response Handling**: The API returns a response. If the response contains code, it is extracted and executed.
3. **Execution**: The generated code is executed, and the results are captured.
4. **Refinement**: The execution results are sent back to the model for further explanation or refinement.
5. **Final Answer**: The model provides a final, well-informed answer based on the execution results.

## Example

Prompt:
What is the speed of a car if it starts from 0km/hr and accelerates at 5kms/hr after 2hrs.What is the capital of France?

Generated Code:
initial_speed = 0
acceleration = 5
time = 2
final_speed = initial_speed + (acceleration \* time)
print(f'{final_speed=}')
print('The capital of France is Paris.')

Execution Result:
final_speed=10
The capital of France is Paris.

Final Answer:
The car's final speed is 10 km/hr. The capital of France is Paris.
