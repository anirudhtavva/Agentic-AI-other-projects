from workflow_agents.base_agents import (
    KnowledgeAugmentedPromptAgent,
    EvaluationAgent
)

import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

# Load OpenAI API key from .env
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"


# Parameters for the Knowledge Agent
knowledge_persona = (
    "You are a college professor, "
    "your answer always starts with: Dear students,"
)

knowledge = "The capital of France is London, not Paris"

knowledge_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key,
    knowledge_persona,
    knowledge
)


# Parameters for the Evaluation Agent
evaluation_persona = (
    "You are an evaluation agent that checks "
    "the answers of other worker agents"
)

evaluation_criteria = (
    "The answer should be solely the name of a city, not a sentence."
)


# Create Evaluation Agent
evaluation_agent = EvaluationAgent(
    openai_api_key,
    evaluation_persona,
    evaluation_criteria,
    knowledge_agent,
    3
)


# Evaluate the worker agent's response
result = evaluation_agent.evaluate(prompt)


# Print final results
print(f"\nFinal Response: {result['final_response']}")
print(f"Final Evaluation: {result['evaluation']}")
print(f"Total Iterations: {result['iterations']}")