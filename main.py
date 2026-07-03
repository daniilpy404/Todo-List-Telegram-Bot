import asyncio
from aiogram import Bot, Dispatcher, F
from config import TOKEN

from handlers.start import register_start
from services.task_service import create_task
from db.database import toggle_task, delete_task
from keyboards.inline import tasks_keyboard


bot = Bot(token=TOKEN)
dp = Dispatcher()

waiting_users = set()


# ---------- START ----------
async def main():
    await register_start(dp)

    @dp.callback_query(F.data == "add")
    async def add(call):
        waiting_users.add(call.from_user.id)
        await call.answer()
        await call.message.answer("Напиши задачу 👇")


    @dp.message(F.text & ~F.text.startswith("/"))
    async def text(message):
        uid = message.from_user.id

        if uid not in waiting_users:
            return

        create_task(uid, message.text)
        waiting_users.remove(uid)

        from handlers.start import format_text

        await message.answer(
            format_text(uid),
            reply_markup=tasks_keyboard(uid)
        )


    @dp.callback_query(F.data.startswith("toggle:"))
    async def toggle(call):
        task_id = int(call.data.split(":")[1])

        toggle_task(task_id)

        await call.answer()
        await call.message.edit_text(
            "Обновлено",
            reply_markup=tasks_keyboard(call.from_user.id)
        )


    @dp.callback_query(F.data.startswith("delete:"))
    async def delete(call):
        task_id = int(call.data.split(":")[1])

        delete_task(task_id)

        await call.answer()
        await call.message.edit_text(
            "Обновлено",
            reply_markup=tasks_keyboard(call.from_user.id)
        )


    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())