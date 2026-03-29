import os
import asyncio
from telethon import TelegramClient, events

# Environment Variables
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
SOURCE_CHAT = -1001550570530 

client = TelegramClient('bot', API_ID, API_HASH)

async def main():
    await client.start(bot_token=BOT_TOKEN)
    print("বট অনলাইনে এসেছে!")

    @client.on(events.NewMessage(pattern='/start'))
    async def start(event):
        await event.reply("হ্যালো আশিক! আমি এখন কাজ করছি।")

    @client.on(events.NewMessage)
    async def search(event):
        if event.is_private and not event.text.startswith('/'):
            async for msg in client.iter_messages(SOURCE_CHAT, search=event.text.lower()):
                if msg.file:
                    await client.send_file(event.chat_id, msg.file, caption=msg.text)
                    return
            await event.reply("অ্যাপটি খুঁজে পাওয়া যায়নি।")

    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main()
