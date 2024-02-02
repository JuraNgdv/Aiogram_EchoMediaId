import asyncio
from aiogram import Bot, Dispatcher, types,F


bot = Bot(token="12345678:AaBbCcDdEeFfGgHh")
dp = Dispatcher()


@dp.message(F.video)
@dp.message(F.audio)
@dp.message(F.photo)
async def cmd_start(msg: types.Message):
    await msg.answer("Hello!")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())