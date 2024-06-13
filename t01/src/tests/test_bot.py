# src/tests/test_bot.py

import pytest
from unittest.mock import AsyncMock, MagicMock
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from game.bot import start, move, talk, fight, inventory

@pytest.mark.asyncio
class TestBot:

    def setup_method(self):
        self.update = MagicMock()
        self.context = MagicMock()
        self.update.callback_query = MagicMock()
        self.update.message.reply_text = AsyncMock()
        self.update.callback_query.answer = AsyncMock()
        self.update.callback_query.edit_message_text = AsyncMock()

    async def test_start(self):
        await start(self.update, self.context)
        
        expected_reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Move", callback_data='move'),
              InlineKeyboardButton("Talk", callback_data='talk'),
              InlineKeyboardButton("Fight", callback_data='fight'),
              InlineKeyboardButton("Inventory", callback_data='inventory')]]
        )
        
        self.update.message.reply_text.assert_called_once_with(
            'Choose an action:',
            reply_markup=expected_reply_markup
        )

    async def test_move(self):
        self.update.callback_query.data = 'move'
        await move(self.update, self.context)

        # Создаем список доступных направлений
        available_directions = ["north", "east"]

        expected_reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton(direction, callback_data=direction)] for direction in available_directions] +
            [[InlineKeyboardButton("Back", callback_data='back')]]
        )

        self.update.callback_query.edit_message_text.assert_called_once_with(
            text='Choose a direction to move:',
            reply_markup=expected_reply_markup
        )

    async def test_talk(self):
        self.update.callback_query.data = 'talk'
        await talk(self.update, self.context)
        
        self.update.callback_query.edit_message_text.assert_called_once_with(
            text="There's no one to talk to here."
        )

    async def test_fight(self):
        self.update.callback_query.data = 'fight'
        await fight(self.update, self.context)
        
        self.update.callback_query.edit_message_text.assert_called_once_with(
            text="There's no one to fight here."
        )

    async def test_inventory(self):
        self.update.callback_query.data = 'inventory'
        await inventory(self.update, self.context)

        # Проверяем текущее содержимое инвентаря героя
        expected_inventory_text = "Your inventory:\npocket dust: 1"

        self.update.callback_query.edit_message_text.assert_called_once_with(
            text=expected_inventory_text
        )

