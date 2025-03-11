from dotenv import load_dotenv
from crewai import Crew
from agent import researcher, writer, webscraper
from tasks import task1, task2, task3

load_dotenv()

crew= Crew(
    agents=[researcher, writer, webscraper],
    tasks=[task1, task2, task3],
    verbose=1,
)

result = crew.kickoff()
print (result)