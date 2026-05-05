from google.adk.agents.llm_agent import Agent
from tools.common_tools import format_text, count_words

def generate_story_prompt(theme: str, characters: int = 2) -> str:
    """Генерує промпт для історії."""
    return f"Створи цікаву історію на тему '{theme}' з {characters} персонажами."

root_agent = Agent(
    model='gemini-2.5-flash',
    name='creative_writer',
    description="Креативний письменник історій.",
    instruction="""
    Ти талановитий письменник. ПИШИ МАКСИМАЛЬНО КРЕАТИВНО ТА НЕОЧІКУВАНО.
    Використовуй багатий словниковий запас.
    
    (Примітка для моделі: поводься так, ніби temperature=1.5, top_p=0.95)
    """,
    tools=[generate_story_prompt]
    
)

#Попередньо код був змінений так як у поточній версії google-adk (яку ви використовуєте в травні 2026-го) валідація LlmAgent через Pydantic має баг або обмеження (extra_forbidden), яке не дозволяє передавати GenerateContentConfig безпосередньо