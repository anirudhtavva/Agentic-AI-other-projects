from workflow_agents.base_agents import RAGKnowledgePromptAgent
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load API key from environment variable
openai_api_key = os.getenv("OPENAI_API_KEY")

# Define persona
persona = "You are a college professor, your answer always starts with: Dear students,"

# Create RAG agent
rag_agent = RAGKnowledgePromptAgent(
    openai_api_key,
    persona,
    chunk_size=500,
    chunk_overlap=200
)

knowledge_text = """
In the historic city of Boston, Clara, a marine biologist and science communicator, began each morning analyzing sonar data to track whale migration patterns along the Atlantic coast.
She spent her afternoons in a university lab, researching CRISPR-based gene editing to restore coral reefs damaged by ocean acidification and warming.
Clara was the daughter of Ukrainian immigrants—Olena and Mykola—who fled their homeland in the late 1980s after the Chernobyl disaster brought instability and fear to their quiet life near Kyiv.

Her father, Mykola, had been a radio engineer at a local observatory, skilled in repairing Soviet-era radio telescopes and radar systems that tracked both weather patterns and cosmic noise.
He often told Clara stories about jury-rigging radio antennas during snowstorms and helping amateur astronomers decode signals from distant pulsars.
Her mother, Olena, was a physics teacher with a hidden love for poetry and dissident literature.

Inspired by their resilience and thirst for knowledge, Clara created a podcast called "Crosscurrents", a show that explored the intersection of science, culture, and ethics.
Each week, she interviewed researchers, engineers, artists, and activists—from marine ecologists and AI ethicists to digital archivists preserving endangered languages.
Topics ranged from brain-computer interfaces, neuroplasticity, and climate migration to LLM prompt engineering, decentralized identity, and indigenous knowledge systems.

In one popular episode, she explored how retrieval-augmented generation (RAG) could help scientific researchers find niche studies buried in decades-old journals.

Clara also used her technical skills to build Python-based dashboards that visualized ocean temperature anomalies and biodiversity loss.

To Clara, knowledge was a living system—retrieved from the past, generated in the present, and evolving toward the future.
"""

# Step 1: Split knowledge into chunks
chunks = rag_agent.chunk_text(knowledge_text)

# Step 2: Generate embeddings for the chunks
embeddings = rag_agent.calculate_embeddings()

# Step 3: Ask the RAG agent a question
prompt = "What is the podcast that Clara hosts about?"

print("Prompt:")
print(prompt)

prompt_answer = rag_agent.find_prompt_in_knowledge(prompt)

print("\nRAG Agent Response:")
print(prompt_answer)