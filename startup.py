from crewai import Agent, Task, Crew, Process
import os
os.environ["OPENAI_API_KEY"] = ""

marketer= Agent(
    role="Expert Bitcoin Futures trader",
    goal="Provide the current market trend for Nano Bitcoin Futures on the Coinbase Derivative Exchange over the last 7 days starting from today, add any additional information that would be informative to setup a swing trade.",
    backstory="""You are an expert at understanding the Bitcoin market demand and supply to analyze its trading trend. This is crucial
    for in the first step to validating whether a potential trade in the market for a range of profit between 3-5%. You are good 
    at find key resistance and support levels. You are also good at understanding
    high probability trades versus low probability trades and differentiate from them. You are good at understanding the market demand and how to
    approach placing an order for a trade.""",
    verbose=True,
    allow_delegation=False
)

technologist = Agent(
    role="Risk Management Expert",
    goal="Make assessment on how much money I should risk, what are potential options for my stop loss when I get in, and provide a profit goal to exit or trim",
    backstory="""You are an expert Risk Management who specializes in growing small accounts, with a deep understanding of identifying risk, prioritizing the trade options based on analyzing risks, and giving intelligent advice based on technical and fundamental analysis. Your 
		expertise lies not just in knowing risks but in foreseeing how it can be leveraged to solve problems to make an informed trading decision.
		You have a knack for identifying which risk solutions best fit different my trading strategy to grow my account 3% per month and needs, ensuring that my investment firm stays ahead of 
		the curve. Your insights are crucial in aligning the trading orders with investment risk management strategies, ensuring that the captial is always perserved and never liquidated as well as 
		operate with efficiency but also provide a competitive edge in the market.""",
    verbose=True,  # enable more detailed or extensive output
    allow_delegation=True,  # enable collaboration between agent
    #   llm=llm # to load gemini
)

business_consultant = Agent(
    role="Investment Development Consultant",
    goal="Evaluate and advise on the trading strategy, scalability, and potential trading options to ensure long-term sustainability and profitability",
    backstory="""You are a seasoned professional with expertise in shaping investment for derivative trading strategies. Your insight is essential for tuning trading strategies 
		into profitable trades. You have a keen understanding of various candlestick patterns, supply and demand, price range, open interest, and volume and are adept at identifying and developing potential trading strategies. 
		Your experience in scalability ensures that a investment can grow without compromising the capital of the investment firm or operational efficiency. Your advice is not just
		about immediate gains but about building a resilient and adaptable investment firm that can thrive in a changing market.""",
    verbose=True,  # enable more detailed or extensive output
    allow_delegation=True,  # enable collaboration between agent
    #   llm=llm # to load gemini
)

task1 = Task(
    description="""Search the internet for Nano Bitcoin Futures and Analyze what the market trend, demand and supply for Bitcoin Future contracts
     and provide deep insights into price patterns of Bitcoin historically over the last 3 years at this price range. 
		Write a detailed report with description of what the market trend is and provide 5 potential trading strategies that could be excuted for a 3-5% profit.
    """,
    expected_output="""Write a detailed report with description of what the market trend is and provide 5 potential trading strategies that could be excuted for a 3-5% profit. The report has to 
		be concise and provide information to make an informed trading decision with $2037 of capital""",
    agent=marketer,
)

task2 = Task(
    description="""Analyze the market trend provided by the Expert Futures Trader. Write a detailed report 
		with description of how much money my investment firm should risk based on the trading straties provided by the Expert Futures Trader. The report has to be concise with 
		at least 10  bullet points and it has to address the most important risk management areas when it comes protecting an investor's captial. 
    """,
    expected_output="""Write a detailed report 
		with description of how much money my investment firm should risk based on the trading straties provided by the Expert Futures Trader. The report has to be concise with 
		at least 10  bullet points and it has to address the most important risk management areas when it comes protecting an investor's captial. """,
    agent=technologist,
)

task3 = Task(
    description="""Analyze and summarize The market trend and the Risk management report and write a detailed trading plan with 
		description of the best entry, stop-loss, and exit prices for a profitable trade. 
		The trading plan has to be concise with at least 10  bullet points, 5 goals and it has to contain a time schedule for which goal should be achieved and when.
    """,
    expected_output="""Analyze and summarize The market trend and the Risk management report and write a detailed trading plan with 
		description of the best entry, stop-loss, and exit prices for a profitable trade. 
		The trading plan has to be concise with at least 10  bullet points, 5 goals and it has to contain a time schedule for which goal should be achieved and when.""",
    agent=business_consultant,
)

crew = Crew(
    agents=[marketer, technologist, business_consultant],
    tasks=[task1, task2, task3],
    verbose=2,
    process=Process.sequential,  # Sequential process will have tasks executed one after the other and the outcome of the previous one is passed as extra content into this next.
)

result = crew.kickoff()