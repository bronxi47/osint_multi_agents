from crewai import Agent
from crewai_tools import SerperDevTool, WebsiteSearchTool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

search_tool = SerperDevTool()
scrap = WebsiteSearchTool()

researcher = Agent(
    role="OSINT-Researcher",
    goal='Gathers the intelligence from the search engine',
    backstory="""OSINT Researcher expert in performing google dorking and
            finding juicy information from the internet.""",
    verbose=False,
    allow_delegation=True,
    tools=[search_tool],
    llm=ChatOpenAI(model_name="gpt-3.5-turbo-0125", temperature=0.3),
)
webscraper = Agent (
    role="Gather Website Data and related information",
    goal='Dig deep into the website and gather the information.',
    backstory="Scrap the website information",
    verbose=True,
    allow_delegation=True,
    llm=ChatOpenAI (model_name="gpt-3.5-turbo-0125", temperature=0.3)
)
writer = Agent (
    role="Data organizer",
    goal='Write about the gathered data in a clean format',
    backstory="Expert in data organisation",
    verbose=True,
    allow_delegation=True,
    llm=ChatOpenAI (model_name="gpt-3.5-turbo-0125", temperature=0.3),
)