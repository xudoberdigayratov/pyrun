from aiogram import Router, types
from aiogram.filters import Command, CommandObject
from connect import *

from src.filters import IsPrivate
from src.keyboards.inline.main import add_group
from src.utils.controller import controllerCode

from src.utils.runner import BubbleRunner

private_router = Router()
private_router.message.filter(IsPrivate())


@private_router.message(Command(commands=['start', 'help'], prefix='./!'))
async def start(message: types.Message):
    bot_ = await bot.get_me()
    text = f"""Execute code.

Usage: <code>/python print("Hello world")</code>

Inline mode: <code>@{bot_.username} print("Hello world")</code>

Line breaks and indentation are supported.

I'll also try to execute files pm'ed to me."""
    await message.answer(text, reply_markup=await add_group())


@private_router.message(Command(commands=['python', 'py', 'python3'], prefix='./!'))
async def python(message: types.Message, command: CommandObject):
    bot_ = await bot.get_me()
    if command.args:
        controller = await controllerCode(command.args)
        if controller:
            Bubble = BubbleRunner()
            result = Bubble.run(command.args)
            if result['result'] == '':
                await message.reply(f"""<b>🔰 Output :\n\n<code>{result['errors']}</code>\n©️ @{bot_.username}</b>""", reply_markup=await add_group())
            else:
                await message.reply(f"""<b>🔰 Output :\n\n<code>{result['result']}</code>\n©️ @{bot_.username}</b>""", reply_markup=await add_group())
        else:
            await message.reply(f"""<b>🔰 Output :\n\n<code>Unexpected error</code>\n©️ @{bot_.username}</b>""",
                                reply_markup=await add_group())
    else:
        await message.answer("""<b>To use mine:

<code>/python

print('Hello World!')</code>

Write code like this!</b>""", reply_markup=await add_group())

