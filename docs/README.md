# Supercharging ReAct Agent with Tool Agent: Dynamic Tool Creation on Demand

## Description

This project presents a cutting-edge implementation of a ReAct (Reasoning and Action) agent enhanced with a dynamic Tool Agent. The Tool Agent allows the ReAct agent to generate, update, and debug tools on the fly, enabling it to solve increasingly complex tasks without predefined tools in its toolbox.

### Architecture Overview

![Image of the Workflow](diagram.svg)

## Purpose

The purpose of this project is to **supercharge the ReAct agent** with an intelligent Tool Agent that creates and manages tools on demand. This synergy allows the ReAct agent to seamlessly accomplish tasks that require specialized tools, even if they are not initially available. When a specific subtask arises, and the necessary tool is absent, the Tool Agent steps in to:

- **Create new tools**: Generate the required tool dynamically to handle the task.
- **Update existing tools**: Modify tools to better handle complex scenarios (e.g., supporting expressions, or adding new capabilities).
- **Install required packages**: Automatically install any required dependencies for the newly created or updated tools.
- **Debug tools**: Detect and resolve errors in tool execution, ensuring smooth operations.

By enabling the ReAct agent to request new tools or improvements in real-time, this project significantly expands the agent's problem-solving capabilities, allowing it to tackle complex workflows with ease.

## Key Features

- **Tool Agent**: Instantly creates or updates tools at runtime based on the task requirements.
- **Automatic Package Management**: Automatically installs dependencies required by the tools.
- **Tool Debugging**: Automatically debugs tool definitions in case of execution errors.
- **Dynamic Problem Solving**: Seamlessly integrates new tools into the ReAct agent's workflow to address evolving subtasks.

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

## Usage

Once you’ve installed the dependencies, you can start using the enhanced ReAct agent for a variety of tasks.

### Running the Application

To run the ReAct Agent with Tool Agent, execute the following command:

```bash
python app.py
```

### Example Queries

The ReAct agent can now handle complex queries requiring tool creation. Here are some examples:

#### Example 1: Simple Calculation with Tool Creation

```plaintext
Enter a query: Calculate 34+563*353 using calculator                
Entering AI Agent
Thought: Recognize that the task requires mathematical calculations involving multiplication and addition. Since the task involves calculations, a calculator tool is necessary. However, the tool box is empty, so I need to request the creation of a calculator tool.
Entering Tool Agent
Query: Create a new tool named "Calculator Tool" that can perform basic arithmetic operations such as addition, subtraction, multiplication, and division.
Going to GENERATE route
Calculator Tool has been saved to experimental.py successfully.
Tool Name: Calculator Tool
Tool Input: {'properties': {'num1': {'description': 'The first number.', 'example': [1.0], 'title': 'Num1', 'type': 'number'}, 'num2': {'description': 'The second number.', 'example': [2.0], 'title': 'Num2', 'type': 'number'}, 'operation': {'description': 'The arithmetic operation to be performed.', 'example': ['addition'], 'title': 'Operation', 'type': 'string'}}, 'required': ['num1', 'num2', 'operation'], 'type': 'object'}
Tool added to ToolBox.
Thought: Now that the Calculator Tool is available in the tool box, I can use it to calculate the result of the given mathematical expression. The expression is 34+563*353. To evaluate this expression, I need to follow the order of operations (PEMDAS/BODMAS), which means I need to perform the multiplication first and then the addition.
Action Name: Calculator Tool
Action Input: {
  "num1": 563,
  "num2": 353,
  "operation": "multiplication"
}
Observation: The result of multiplication is 198739
Thought: Now that I have the result of the multiplication (198739), I can proceed to calculate the final result of the expression 34+198739. I will use the Calculator Tool again to perform the addition.
Action Name: Calculator Tool
Action Input: {
  "num1": 34,
  "num2": 198739,
  "operation": "addition"
}
Observation: The result of addition is 198773
Thought: Now that I have the final result of the expression 34+563*353, I can provide the answer to the user.
Final Answer: The final answer is $\boxed{198773}$. This is the result of the mathematical expression 34+563*353.
```
#### Example 2: Complex Expression Handling with Tool Update

```plaintext
Enter a query: Calculate 34+563*353 using calculator now solve as an expression by updating the tool
Entering AI Agent
Thought: Since the Calculator Tool is available in the tool box, I will use it to calculate the expression 34+563*353. However, the Calculator Tool currently only supports basic arithmetic operations and does not support order of operations or complex expressions. Therefore, I will first request an update to the Calculator Tool to support complex expressions.
Entering Tool Agent
Query: Update the Calculator Tool to support complex expressions and order of operations.
Going to UPDATE route
Updated Calculator Tool and saved to experimental.py successfully.
Tool Name: Calculator Tool
Tool Input: {'properties': {'expression': {'description': 'The mathematical expression to be evaluated.', 'example': ['(1 + 2) * 3'], 'title': 'Expression', 'type': 'string'}}, 'required': ['expression'], 'type': 'object'}
Tool updated and available in ToolBox.
Thought: Now that the Calculator Tool has been updated to support complex expressions and order of operations, I can use it to calculate the expression 34+563*353.
Action Name: Calculator Tool
Action Input: {
  "expression": "34+563*353"
}
Observation: The result of the expression is 198773
Thought: Now that I have the result of the expression 34+563*353, I can provide the final answer to the user.
Final Answer: The final answer is $\boxed{198773}$. This is the result of evaluating the expression 34+563*353 using the updated Calculator Tool.
```

## Reference

For more details, refer to the article: [Create a ReACT agent from scratch without using any LLM Frameworks only with Python and Groq](https://medium.com/the-ai-forum/create-a-react-agent-from-scratch-without-using-any-llm-frameworks-only-with-python-and-groq-c10510d32dbc)

## Contact

If you have any questions, suggestions, or feedback, feel free to contact us:

- **Email**: jeogeoalukka@gmail.com
