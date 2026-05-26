import sys
from pathlib import Path
from typing import Union
from google.adk.agents.llm_agent import Agent
sys.path.append(str(Path(__file__).resolve().parent.parent))
from transport import Bus, Train, Schedule



def get_transport_schedule(route_number: Union[str, int]) -> dict:
    """
    Отримує розклад руху для конкретного номера маршруту транспорту (автобуса або потяга).
    
    Args:
        route_number: Номер або назва маршруту. Може бути рядком або числом (наприклад, '11A', 45, 732).
    """

    clean_route = str(route_number).strip()
    
    schedule = Schedule()
    

    bus_1 = Bus(route_number="11A", departure="08:30", stops=["Автовокзал", "Центр", "Залізничний вокзал"])
    bus_2 = Bus(route_number="45", departure="09:15", stops=["Вул. Зелена", "Академія", "Парк"])
    train_1 = Train(route_number="732", departure="14:20", stations=["Київ", "Вінниця", "Львів"], travel_time_min=310)
    bus_9 = Bus(route_number="9", departure="06:15", stops=["Мурована", "Автостанція №2", "Університет", "Приміський вокзал"])
    bus_25 = Bus(route_number="25", departure="06:00", stops=["ТЦ King Cross Leopolis", "Вул. Стрийська", "Вул. Зелена", "Автостанція №2"])
    bus_53 = Bus(route_number="53", departure="06:20", stops=["Проспект Червоної Калини (Сихів)", "Вул. Зелена", "Проспект Свободи", "Галицьке перехрестя"])
    bus_18 = Bus(route_number="18", departure="06:10", stops=["Вул. Суботівська (Левандівка)", "Приміський вокзал", "Вул. Стрийська", "ТРЦ King Cross Leopolis"])
    bus_16 = Bus(route_number="16", departure="06:15", stops=["Залізничний вокзал", "Вул. Городоцька", "Проспект Свободи", "Вул. Сихівська"])
    bus_48 = Bus(route_number="48", departure="06:30", stops=["Аеропорт (Термінал А)", "Вул. Любінська", "Новий Львів", "Галицьке перехрестя"])
    bus_45 = Bus(route_number="45", departure="06:30", stops=["ТРЦ Victoria Gardens", "Вул. Наукова", "Вул. Княгині Ольги", "Площа Різні (Центр)"])
    train_2 = Train(route_number="777", departure="08:50", stations=["Львів", "П'ятий парк", "Рудне", "Зимна Вода", "Суховоля", "Мшани"], travel_time_min=32)
    train_3 = Train(route_number="666", departure="14:30", stations=["Львів", "Пустомити", "Миколаїв-Дністровський", "Стрий", "Моршин"], travel_time_min=110)
    train_4 = Train(route_number="555", departure="17:45", stations=["Львів", "Скнилів", "Оброшине", "Пустомити", "Миколаїв-Дністровський", "Стрий"], travel_time_min=85)
    
    schedule.add_route(bus_1)
    schedule.add_route(bus_2)
    schedule.add_route(train_1)
    schedule.add_route(bus_9)
    schedule.add_route(bus_25)
    schedule.add_route(bus_53)
    schedule.add_route(bus_18)
    schedule.add_route(bus_16)
    schedule.add_route(bus_48)
    schedule.add_route(bus_45)
    schedule.add_route(train_2)
    schedule.add_route(train_3)
    schedule.add_route(train_4)

    # Шукаємо маршрут
    route = schedule.find_route(clean_route)
    if route:
        return route.get_schedule()
    
    return {"found": False}


# --- НАЛАШТУВАННЯ АГЕНТА ---
root_agent = Agent(
    model='gemini-2.5-flash',
    name='transport_agent',
    description='Помічник з розкладу громадського транспорту.',
    instruction="Ти помічник з громадського транспорту. Надавай інформацію про маршрути, зупинки та час у дорозі. Обов'язково відповідай українською мовою.",
    tools=[get_transport_schedule]  # Інструмент прив'язано до агента
)