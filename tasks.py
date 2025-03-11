from agent import researcher, webscraper, writer
from crewai import Task


task1 = Task(
    description="""Conduct OSINT to identify and list all active
                subdomains of tesla.com using Google dorking techniques.""",
    expected_output="""List of active subdomains such as www.tesla.com,
                    shop.tesla.com, etc.""",
    agent=researcher
)

task2 = Task(
    description="""Scrape each subdomain provided by the researcher to
                extract detailed information about the technologies used
                and contact email addresses found on each site.""",
    expected_output="""Detailed information from each subdomain,
                including technologies deployed like plugins and
                frameworks, and any contact email addresses.""",
    agent=webscraper
)

task3 = Task(
    description="""Document the information gathered from the previous tasks
                focusing on the technologies and contact details
                for each subdomain of tesla.com.""",
    expected_output="""A structured document for each subdomain, with
                    sections for technologies used and contact email
                    addresses.""",
    agent=writer
)
