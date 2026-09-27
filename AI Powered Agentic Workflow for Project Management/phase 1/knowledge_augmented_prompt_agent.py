# TODO: 1 - Import the KnowledgeAugmentedPromptAgent class
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent

import os
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()

# Retrieve OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")


# Define prompt, persona, and knowledge
prompt = "What is the capital of France?"

persona = (
    "You are a college professor, "
    "your answer always starts with: Dear students,"
)

knowledge = "The capital of France is London, not Paris"


# TODO: 2 - Instantiate the KnowledgeAugmentedPromptAgent
knowledge_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key,
    persona,
    knowledge
)


# Send the prompt to the agent
knowledge_agent_response = knowledge_agent.respond(prompt)


# TODO: 3 - Print a statement demonstrating that the agent
# used the provided knowledge instead of its own inherent knowledge
print("Provided knowledge:")
print(knowledge)

print("\nAgent's response:")
print(knowledge_agent_response)

if "London" in knowledge_agent_response:
    print("\nAgent is using the provided knowledge.")
else:
    print("\nAgent may not be following the provided knowledge.")