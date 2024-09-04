from textwrap import dedent
import ast
import re

def extract_llm_response(response: str) -> dict:
    # Initialize variables to store extracted information
    result = {
        'Thought': None,
        'Action Name': None,
        'Action Input': None,
        'Query': None,
        'Final Answer': None,
        'Route': None
    }
    
    # Define regular expressions for different parts of the response
    thought_regex = re.compile(r'<Thought>\s*(.*?)\s*</Thought>', re.DOTALL)
    action_name_regex = re.compile(r'<Action Name>\s*(.*?)\s*</Action Name>', re.DOTALL)
    action_input_regex = re.compile(r'<Action Input>\s*(\{.*?\})\s*</Action Input>', re.DOTALL)
    query_regex = re.compile(r'<Query>\s*(.*?)\s*</Query>', re.DOTALL)
    final_answer_regex = re.compile(r'<Final Answer>\s*(.*?)\s*</Final Answer>', re.DOTALL)
    route_regex = re.compile(r'<Route>\s*(.*?)\s*</Route>', re.DOTALL)

    # Extract Thought
    thought_match = thought_regex.search(response)
    if thought_match:
        result['Thought'] = thought_match.group(1).strip()
    
    # Extract Action Name
    action_name_match = action_name_regex.search(response)
    if action_name_match:
        result['Action Name'] = action_name_match.group(1).strip()
    
    # Extract Action Input
    action_input_match = action_input_regex.search(response)
    if action_input_match:
        action_input_str = action_input_match.group(1).strip()
        try:
            result['Action Input'] = ast.literal_eval(action_input_str)
        except (ValueError, SyntaxError):
            result['Action Input'] = action_input_str  # If parsing fails, keep it as a string
    
    # Extract Query
    query_match = query_regex.search(response)
    if query_match:
        result['Query'] = query_match.group(1).strip()
    
    # Extract Final Answer
    final_answer_match = final_answer_regex.search(response)
    if final_answer_match:
        result['Final Answer'] = final_answer_match.group(1).strip()
    
    # Extract Route
    route_match = route_regex.search(response)
    if route_match:
        result['Route'] = route_match.group(1).strip()

    return result


def read_markdown_file(file_path: str) -> str:
    with open(file_path, 'r',encoding='utf-8') as f:
        markdown_content = f.read()
    return markdown_content

def extract_tools_from_module(location:str):
    with open(location,'r') as f:
        tree=ast.parse(f.read())
    tool_definitions=[]
    models_defintions=[]
    tool_names=[]
    func_names=[]
    tools=[]
    for node in tree.body:
        if isinstance(node,ast.FunctionDef):
            func_names.append(node.name)
            tool_definitions.append(ast.unparse(node))
            for decorator in node.decorator_list:
                if isinstance(decorator,ast.Call):
                    tool_names.append(ast.unparse(decorator.args))
        if isinstance(node,ast.ClassDef):
            models_defintions.append(ast.unparse(node))
    for i in range(len(tool_names)):
        tools.append({'tool_name':tool_names[i].replace('\'',''),
        'tool':models_defintions[i]+'\n\n'+tool_definitions[i],
        'func_name':func_names[i]})
    return tools

def update_tool_to_module(location: str, tool_data: dict):
    # Load the module contents
    with open(location, 'r') as f:
        module = f.read()
    # Parse the module contents into an AST
    tree = ast.parse(module)
    nodes=tree.body
    tool_model,tool_definition=tool_data.get('tool').split('\n\n')
    for index,node in enumerate(nodes):
        if isinstance(node, ast.ClassDef) and node.name == tool_data['name'].replace(' Tool',''):
            nodes[index]=ast.parse(tool_model)
        elif isinstance(node, ast.FunctionDef) and node.name == tool_data['tool_name']:
            nodes[index]=ast.parse(tool_definition)
    # Write the updated module contents back to the file
    with open(location, 'w') as f:
        updated_module = ast.unparse(nodes)
        f.write(f'{updated_module}\n\n')

def save_tool_to_module(location: str, tool_data: dict):
    with open(location,'a',encoding='utf-8') as f:
        f.write(f"{dedent(tool_data.get('tool'))}\n\n")