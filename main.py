import asyncio as aio
from bot import *
from web import app  # Flask app import kiya

async def async_main():
    db = DB()
    await db.connect()

    # Flask ko async mode me run karo
    loop = aio.get_running_loop()
    loop.create_task(run_flask())

if __name__ == '__main__':
    loop = aio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(async_main())
    loop.create_task(manga_updater())
    for i in range(10):
        loop.create_task(chapter_creation(i + 1))
    bot.run()

# Flask server async function
async def run_flask():
    from hypercorn.asyncio import serve
    from hypercorn.config import Config

    config = Config()
    config.bind = ["0.0.0.0:8000"]  # Koyeb expects 8000
    await serve(app, config)
