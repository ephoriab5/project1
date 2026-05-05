import logging
from google.adk.agents.llm_agent import Agent
from tools.common_tools import format_text, count_words

# 1. Налаштування логування: встановлюємо рівень INFO для виведення в консоль
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 2. Створення інструменту з логуванням
def logging_tool(param: str) -> dict:
    """Інструмент з логуванням подій"""
    # Це повідомлення з'явиться в терміналі, коли агент викличе функцію
    logger.info(f"Виклик інструменту logging_tool з параметром: {param}")
    return {"result": "success", "processed_param": param}

# 3. Ініціалізація агента
root_agent = Agent(
    model='gemini-2.5-flash',
    name='logging_agent',
    description="Агент з логуванням.",
    instruction="Використовуй інструмент logging_tool та логуй всі дії.",
    tools=[logging_tool],
)