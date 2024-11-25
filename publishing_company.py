from crewai import Agent, Task, Crew, Process
from langchain_community.document_loaders import TwitterTweetLoader
import os
os.environ["OPENAI_API_KEY"] = ""

marketer= Agent(
    role="Market Research Analyst",
    goal="Find out how and why specified tweet threads from the documents do better than others and suggest how to reach the widest possible customer base",
    backstory="""You are an expert at understanding the market demand, target audience, and competition. This is crucial
    for validating whether an idea fulfills a market need and has the potential to attract a wide audience. You are good 
    at coming up with ideas on how to appeal to the widest possible customer base. You are also good at understanding
    the competition and how to differentiate from them. You are good at understanding the market demand and how to
    approach the target audience.""",
    verbose=True,
    allow_delegation=False
)

technologist = Agent(
    role="Technology Expert",
    goal="Make assessment on how to appeal to the customer base emotions explain what the content of the thread needs to adopt in order to succeed",
    backstory="""You are a visionary in the realm of social media and marketing psychology, with a deep understanding of both current and emerging marketing trends. Your 
		expertise lies not just in knowing the marketing but in foreseeing how it can be leveraged to solve real-world problems and drive business innovation.
		You have a knack for identifying which marketing solutions best fit different business models and needs, ensuring that companies stay ahead of 
		the curve. Your insights are crucial in aligning technology with business strategies, ensuring that the technological adoption not only enhances 
		operational efficiency but also provides a competitive edge in the market.""",
    verbose=True,  # enable more detailed or extensive output
    allow_delegation=True,  # enable collaboration between agent
    #   llm=llm # to load gemini
)

business_consultant = Agent(
    role="Business Development Consultant",
    goal="Evaluate and advise on the tweet thread model, scalability, and potential revenue streams to ensure long-term sustainability and profitability",
    backstory="""You are a seasoned professional with expertise in shaping business strategies. Your insight is essential for turning innovative ideas 
		into viable business models. You have a keen understanding of various industries and are adept at identifying and developing potential revenue streams. 
		Your experience in scalability ensures that a business can grow without compromising its values or operational efficiency. Your advice is not just
		about immediate gains but about building a resilient and adaptable business that can thrive in a changing market.""",
    verbose=True,  # enable more detailed or extensive output
    allow_delegation=True,  # enable collaboration between agent
    #   llm=llm # to load gemini
)

task1 = Task(
    description="""Analyze tweets from the documents of tweets using the loader. 
		Write a detailed report with description of what the ideal customer might look like, and how to reach the widest possible audience. The report has to 
		be concise with at least 10 bullet points and it has to address the most important areas when it comes to marketing this type of business.
    """,
    agent=marketer,
)

task2 = Task(
    description="""Analyze how to produce tweet thread content that resonates with the personas of this product so that it is iconic and popular.. Write a detailed report 
		with description of tweet threads the business needs to use in order to make High marketing content. The report has to be concise with 
		at least 10  bullet points and it has to address the most important areas when it comes to manufacturing this type of content. 
    """,
    agent=technologist,
)

task3 = Task(
    description="""Analyze and summarize marketing and technological report and write a detailed business plan with 
		description of how to make a sustainable and popular twitter feed. 
		The business plan has to be concise with 
		at least 10  bullet points, 5 goals and it has to contain a time schedule for which goal should be achieved and when.
    """,
    agent=business_consultant,
)

loader = TwitterTweetLoader.from_secrets(
    access_token='1281380815188963328-hWzlbxAnoF1WCnsYS9znFhWhnz1xMH',
    access_token_secret='8l2uYhtaOqAhdEDTrkBHJaBcCfHxVCQ9jNxq8vG5kLdA2',
    consumer_key='CTcqMGYZ1WVOejUyzR4IGukCD',
    consumer_secret='M0tODYQj936VCfBtFPM9wYt1norJ4EXdcF4wxQcdvOPZJYLRzR',
    twitter_users=['elonmusk'],
    number_tweets=50,
    
)

documents = loader.load()
documents[:5]

crew = Crew(
    agents=[marketer, technologist, business_consultant],
    tasks=[task1, task2, task3],
    verbose=2,
    process=Process.sequential,  # Sequential process will have tasks executed one after the other and the outcome of the previous one is passed as extra content into this next.
)

result = crew.kickoff()