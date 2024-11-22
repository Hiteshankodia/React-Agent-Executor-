from dotenv import load_dotenv 
from langchain import hub 
from langchain.agents import create_react_agent 
#This will take a prompt and LLM and the tool and return us a runnable object. 
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import tool 
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI

load_dotenv()


#It will take the tool names the tool descriptions and it will take the input for the user. and it will deduce, 
#if we need to execute a tool or if we have the answer ready, or if we can't do anything

react_prompt: PromptTemplate = hub.pull("hwchase17/react")


@tool
def triple(num: float) -> float:
    """
    :param num: a number to triple
    :return: the number tripled ->  multiplied by 3
    """
    return 3 * float(num)


tools = [TavilySearchResults(max_results=1), triple]



llm = ChatGoogleGenerativeAI(model = 'gemini-1.5-flash')

react_agent_runnable = create_react_agent(llm, tools, react_prompt)


