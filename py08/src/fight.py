# fight.py

import asyncio
from enum import Enum, auto
from random import choice

class Action(Enum):
    HIGHKICK = auto()
    LOWKICK = auto()
    HIGHBLOCK = auto()
    LOWBLOCK = auto()

class Agent:
    def __init__(self):
        self.health = 5  # Установим начальное здоровье агента
    
    def __aiter__(self):
        self.actions = list(Action)
        return self

    async def __anext__(self):
        await asyncio.sleep(0.1)  # Имитация задержки для асинхронности
        return choice(self.actions)

async def fight():
    agent = Agent()
    async for action in agent:
        if agent.health <= 0:
            print("Neo wins!")
            break
        
        if action == Action.HIGHKICK or action == Action.LOWKICK:
            response = Action.HIGHBLOCK if action == Action.HIGHKICK else Action.LOWBLOCK
            print(f"Agent: {action}, Neo: {response}, Agent Health: {agent.health}")
            agent.health -= 1  # Уменьшаем здоровье агента за каждый блок Нео
        
        elif action == Action.HIGHBLOCK or action == Action.LOWBLOCK:
            response = Action.LOWKICK if action == Action.HIGHBLOCK else Action.HIGHKICK
            print(f"Agent: {action}, Neo: {response}, Agent Health: {agent.health}")
            if response == Action.HIGHKICK or response == Action.LOWKICK:
                agent.health -= 1  # Уменьшаем здоровье агента за каждый удар Нео

async def fightmany(n):
    agents = [Agent() for _ in range(n)]
    tasks = []

    for i, agent in enumerate(agents):
        task = asyncio.create_task(fight_agent(agent, i + 1))
        tasks.append(task)
    
    await asyncio.gather(*tasks)
    print("Neo wins all fights!")

async def fight_agent(agent, agent_id):
    async for action in agent:
        if agent.health <= 0:
            print(f"Agent {agent_id} defeated!")
            break
        
        if action == Action.HIGHKICK or action == Action.LOWKICK:
            response = Action.HIGHBLOCK if action == Action.HIGHKICK else Action.LOWBLOCK
            print(f"Agent {agent_id}: {action}, Neo: {response}, Agent {agent_id} Health: {agent.health}")
            agent.health -= 1
        
        elif action == Action.HIGHBLOCK or action == Action.LOWBLOCK:
            response = Action.LOWKICK if action == Action.HIGHBLOCK else Action.HIGHKICK
            print(f"Agent {agent_id}: {action}, Neo: {response}, Agent {agent_id} Health: {agent.health}")
            if response == Action.HIGHKICK or response == Action.LOWKICK:
                agent.health -= 1

# Запуск поединков
if __name__ == '__main__':
    asyncio.run(fight())  # Запустить бой с одним агентом
    # asyncio.run(fightmany(3))  # Запустить бой с несколькими агентами (раскомментируйте для теста)

