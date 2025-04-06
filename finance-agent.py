from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools

import os


os.environ["GROQ_API_KEY"] = "GROQ_API_KEY"

agent=Agent(
    model = Groq(id='llama3-8b-8192',api_key=os.environ["GROQ_API_KEY"]),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    markdown=True,
    instructions=['Use Tables to Display Data.']
    )
   

agent.print_response('Summarize and compare analyst recommendations and fundamentals for TSLA and NVDA')
