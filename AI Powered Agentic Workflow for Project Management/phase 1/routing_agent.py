
# TODO: 1 - Import the KnowledgeAugmentedPromptAgent and RoutingAgent
import os
from dotenv import load_dotenv
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent, RoutingAgent

# Load environment variables from .env file
load_dotenv()

openai_api_key = "voc-97561288115987454309396ab798c52482a5.88417845"

persona = "You are a college professor"

texasKnowledge = "You know everything about Texas"
texas_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, texasKnowledge)
# TODO: 2 - Define the Texas Knowledge Augmented Prompt Agent

europe_knowledge = "You know everything about Europe"
europe_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, europe_knowledge)
# TODO: 3 - Define the Europe Knowledge Augmented Prompt Agent

persona = "You are a college math professor"
math_knowledge = "You know everything about math, you take prompts with numbers, extract math formulas, and show the answer without explanation"
math_knowledge_agent = KnowledgeAugmentedPromptAgent(openai_api_key, persona, math_knowledge)
# TODO: 4 - Define the Math Knowledge Augmented Prompt Agent

routing_agent = RoutingAgent(openai_api_key, {})
agents = [
    {
        "name": "texas agent",
        "description": "Answer a question about Texas",
        "func": lambda x: texas_agent.respond(x)
    },
    {
        "name": "europe agent",
        "description": "Answer a question about Europe",
        "func": lambda x: europe_agent.respond(x)
    },
    {
        "name": "math agent",
        "description": "When a prompt contains numbers, respond with a math formula",
        "func": lambda x: math_knowledge_agent.respond(x)
    }
]

routing_agent.agents = agents

# TODO: 8 - Print the RoutingAgent responses to the following prompts:
#           - "Tell me about the history of Rome, Texas"
#           - "Tell me about the history of Rome, Italy"
#           - "One story takes 2 days, and there are 20 stories"
prompts = [
    "Tell me about the history of Rome, Texas",
    "Tell me about the history of Rome, Italy",
    "One story takes 2 days, and there are 20 stories"
]

for prompt in prompts:
    print(f"\nPrompt: {prompt}")
    response = routing_agent.route_prompt(prompt)
    print(f"Response: {response}")