from abc import ABC
from json import dumps

class BaseMessage(ABC):
    def to_dict(self)->dict[str,str]:
        return {
            'role': self.role,
            'content': f'''{self.content}'''
        }
    def __repr__(self):
        class_name = self.__class__.__name__
        attributes = ", ".join(f"{key}={value}" for key, value in self.__dict__.items())
        return f"{class_name}({attributes})"

class HumanMessage(BaseMessage):
    def __init__(self,content):
        self.role='user'
        self.content=content

class AIMessage(BaseMessage):
    def __init__(self,content):
        self.role='assistant'
        self.content=content
        
class SystemMessage(BaseMessage):
    def __init__(self,content):
        self.role='system'
        self.content=content

class ToolMessage(BaseMessage):
    def __init__(self,content:str,tool_call:str,tool_args:dict):
        self.role='assistant'
        self.content=content
        self.tool_call=tool_call
        self.tool_args=tool_args