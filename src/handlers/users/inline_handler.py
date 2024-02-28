import uuid

from aiogram import types
from src.handlers.users.private import private_router, IsPrivate
from src.utils.runner import BubbleRunner

@private_router.inline_query()
async def inline_handler(query: types.InlineQuery):
    q = query.query
    results = []
    try:
        sss = uuid.uuid4().hex[:11]
        Bubble = BubbleRunner()
        res = Bubble.run(q)
        if res['result'] == '':
            result = res['errors']
        else:
            result = res['result']
        results.append(types.InlineQueryResultArticle(
                          id=sss,
                          title="❗️Click here",
                          input_message_content=types.InputTextMessageContent(
                              message_text=f"<b>Code:\n<code>{q}</code>\n\nResult:\n<code>{result}</code></b>",
                              disable_web_page_preview=True
                          ),
                          thumb_url="https://img2.teletype.in/files/d6/27/d62724c4-44b0-4fcc-9fd8-8b82bdd8398a.png",
                        ))
        await query.answer(results, cache_time=5)
    except Exception as e:
        print(f'Error: {e}')
        await query.answer([], cache_time=5, switch_pm_parameter='start', switch_pm_text='Start Bot')
