from crewai import Agent, Task, Crew, Process
import os
os.environ["OPENAI_API_KEY"] = ""

researcher = Agent(
    role="Researcher",
    goal="Research new AI insights",
    backstory="You are an AI research assistant.",
    verbose=True,
    allow_delegation=False
)

writer = Agent(
    role="Writer",
    goal="Write compelling and engaging blog posts about AI trends and insights.",
    backstory="You are an AI blog post writer who specializes in making complex AI topics easy to understand.",
    verbose=True,
    allow_delegation=False
)

task1 = Task(description="Investigate the latest AI trends and insights.", agent=researcher)
task2 = Task(description="Write a compelling blog post about the latest AI trends and insights.", agent=writer)

crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=2,
    process=Process.sequential
)

result = crew.kickoff()