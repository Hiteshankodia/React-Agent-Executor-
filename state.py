import operator 
from typing import Annotated, TypedDict, Union 

from langchain_core.agents import AgentAction, AgentFinish 
#The agent action is going to contain the function that we need to run with its input and with the prove why did we choose it 
# and the agent finish result the final output

class AgentState(TypedDict) : 
    input : str 
    agent_outcome : Union[AgentAction, AgentFinish, None]
    #this agent_outcome has the information helps out agent decide wheather it needs to continue and to perform some action, to execute the tool or to finish and to reutn the result to the user. 
    #in first he agent_outcome will be none. 
    intermediate_steps : Annotated[list[tuple[AgentAction, str]], operator.add]
