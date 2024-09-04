from typing import TypedDict,Annotated
from src.message import BaseMessage
import operator

class AgentState(TypedDict):
    input:str
    messages:Annotated[list[BaseMessage],operator.add]
    output:str