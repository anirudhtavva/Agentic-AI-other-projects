from workflow_agents.base_agents import DirectPromptAgent

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# TODO: 2 - Load the OpenAI API key from the environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the Capital of France?"

# TODO: 3 - Instantiate the DirectPromptAgent as direct_agent
direct_agent = DirectPromptAgent(openai_api_key)

# TODO: 4 - Use direct_agent to send the prompt and store the response
direct_agent_response = direct_agent.respond(prompt)

# Print the response from the agent
print("Agent Response:")
print(direct_agent_response)

# TODO: 5 - Print an explanatory message describing the knowledge source
print(
    "\nKnowledge Source: The agent used the general pre-trained knowledge "
    "of the gpt-4 model to generate this response."
)