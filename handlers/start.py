from aiogram import types
from aiogram.filters import Command
from services.task_service import list_tasks
from keyboards.inline import tasks_keyboard


def format_text(user_id):
    tasks = list_tasks(user_id)

    if not tasks:
        return "📭 У тебя нет задач"

    text = "📋 Твои задачи:\n\n"

    for task_id, t, done in tasks:
        status = "✅" if done else "❌"
        text += f"{task_id}. {t} {status}\n"

    return text


async def register_start(dp):

    @dp.message(Command("start"))
    async def start(message: types.Message):
        uid = message.from_user.id

        await message.answer(
            format_text(uid),
            reply_markup=tasks_keyboard(uid)
        )