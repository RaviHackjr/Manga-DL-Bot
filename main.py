import asyncio as aio
from bot import *
from web import app
import threading

async def async_main():
    db = DB()
    await db.connect()

def run_web():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    loop = aio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(async_main())
    
    # Flask server ko alag thread me chalane ke liye
    threading.Thread(target=run_web, daemon=True).start()
    
    loop.create_task(manga_updater())
    for i in range(10):
        loop.create_task(chapter_creation(i + 1))
    
    bot.run()
