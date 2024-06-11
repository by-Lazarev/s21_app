# tests/test_fight.py

import pytest
import asyncio
from fight import Agent, Action, fight, fightmany

@pytest.mark.asyncio
async def test_agent_fight():
    agent = Agent()
    agent.health = 2  # Устанавливаем здоровье агента в 2 для быстрого теста
    actions = [Action.HIGHKICK, Action.LOWKICK, Action.HIGHBLOCK, Action.LOWBLOCK]

    neo_actions = []
    async for action in agent:
        if action == Action.HIGHKICK:
            neo_actions.append(Action.HIGHBLOCK)
        elif action == Action.LOWKICK:
            neo_actions.append(Action.LOWBLOCK)
        elif action == Action.HIGHBLOCK:
            neo_actions.append(Action.LOWKICK)
        elif action == Action.LOWBLOCK:
            neo_actions.append(Action.HIGHKICK)

        agent.health -= 1  # Уменьшаем здоровье агента

        if agent.health <= 0:
            break

    assert agent.health == 0
    assert len(neo_actions) == 2  # Нео должен был ответить дважды

@pytest.mark.asyncio
async def test_fight():
    # Переопределим stdout для захвата вывода
    from io import StringIO
    from contextlib import redirect_stdout

    output = StringIO()
    with redirect_stdout(output):
        await fight()

    output = output.getvalue()
    assert "Neo wins!" in output

@pytest.mark.asyncio
async def test_fightmany():
    # Переопределим stdout для захвата вывода
    from io import StringIO
    from contextlib import redirect_stdout

    output = StringIO()
    with redirect_stdout(output):
        await fightmany(3)

    output = output.getvalue()
    assert "Neo wins all fights!" in output
    assert "Agent 1 defeated!" in output
    assert "Agent 2 defeated!" in output
    assert "Agent 3 defeated!" in output

