from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from services.task_service import list_tasks


def tasks_keyboard(user_id):
    tasks = list_tasks(user_id)

    kb = []

    for task_id, text, done in tasks:
        kb.append([
            InlineKeyboardButton(
                text=f"{'✅' if done else '❌'} {text}",
                callback_data="noop"
            ),
            InlineKeyboardButton("✔", callback_data=f"toggle:{task_id}"),
            InlineKeyboardButton("🗑", callback_data=f"delete:{task_id}")
        ])

    kb.append([
        InlineKeyboardButton("➕ Добавить", callback_data="add")
    ])

    return InlineKeyboardMarkup(inline_keyboard=kb)