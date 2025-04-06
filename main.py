from phi.agent import Agent
from phi.model.groq import Groq
import os

os.environ["GROQ_API_KEY"] = ""

agent=Agent(
    model = Groq(id='llama3-8b-8192',api_key=os.environ["GROQ_API_KEY"]))

agent.print_response("write 2 lines of poem for Rose.")

