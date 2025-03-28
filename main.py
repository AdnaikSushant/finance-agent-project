from phi.agent import Agent
from phi.model.groq import Groq
import os

os.environ["GROQ_API_KEY"] = "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"

agent=Agent(
    model = Groq(id='llama3-8b-8192',api_key=os.environ["GROQ_API_KEY"]))

agent.print_response("write 2 lines of poem for Rose.")

