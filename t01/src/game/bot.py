# src/game/bot.py

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from game.protagonist import Protagonist
from game.load_map import load_map
from game.load_data import load_initial_data
import os
import random

# Загрузка данных
locations = load_map()
player_data, npc_data, enemy_data = load_initial_data()

# Создание главного героя
hero = Protagonist(name=player_data["name"], id=player_data["id"])
hero.set_location(locations["loc_1"])

# Инициализация NPC и врагов
npcs = {npc["id"]: npc for npc in npc_data}
enemies = {enemy["id"]: enemy for enemy in enemy_data}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Move", callback_data='move'),
            InlineKeyboardButton("Talk", callback_data='talk'),
            InlineKeyboardButton("Fight", callback_data='fight'),
            InlineKeyboardButton("Inventory", callback_data='inventory')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Choose an action:', reply_markup=reply_markup)

async def move(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    location = hero.current_location
    keyboard = [[InlineKeyboardButton(direction, callback_data=direction)] for direction in location.get_connections()]
    keyboard.append([InlineKeyboardButton("Back", callback_data='back')])
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(text='Choose a direction to move:', reply_markup=reply_markup)

async def talk(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    npc_list = [npc for npc in npcs.values() if hero.current_location.id == npc["id"]]
    if npc_list:
        npc = npc_list[0]  # В этом примере берется первый доступный NPC
        dialogue = npc["dialogue"]
        response = hero.talk_to(npc)
        await query.edit_message_text(text=response)
    else:
        await query.edit_message_text(text="There's no one to talk to here.")

async def fight(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    enemy_list = [enemy for enemy in enemies.values() if hero.current_location.id == enemy["id"]]
    if enemy_list:
        enemy = enemy_list[0]  # В этом примере берется первый доступный враг
        result = hero.attack(enemy)
        await query.edit_message_text(text=result)
    else:
        await query.edit_message_text(text="There's no one to fight here.")

async def inventory(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    inventory_items = "\n".join([f"{item}: {count}" for item, count in hero.inventory.items()])
    await query.edit_message_text(text=f"Your inventory:\n{inventory_items}")

def main() -> None:
    token = os.getenv("TELEGRAM_TOKEN")
    application = Application.builder().token(token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(move, pattern='^move$'))
    application.add_handler(CallbackQueryHandler(talk, pattern='^talk$'))
    application.add_handler(CallbackQueryHandler(fight, pattern='^fight$'))
    application.add_handler(CallbackQueryHandler(inventory, pattern='^inventory$'))
    application.add_handler(CallbackQueryHandler(start, pattern='^back$'))

    application.run_polling()

if __name__ == "__main__":
    main()

