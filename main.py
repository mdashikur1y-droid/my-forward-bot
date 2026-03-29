
import os
import asyncio
from telethon import TelegramClient, events

# Environment Variables থেকে ডাটা নেবে
API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# Edit Infinity File এর আইডি
SOURCE_CHAT = -1001550570530 

client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

print("বট সচল হয়েছে...")

# /start দিলে উত্তর দেবে
@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.reply("হ্যালো আশিক! আমি তৈরি। অ্যাপের নাম লিখে সার্চ করো।")

# সার্চ করলে ফাইল দেওয়ার জন্য
@client.on(events.NewMessage)
async def search_files(event):
    if event.is_private and not event.text.startswith('/'):
        query = event.text.lower()
        found = False
        async for msg in client.iter_messages(SOURCE_CHAT, search=query):
            if msg.file:
                await client.send_file(event.chat_id, msg.file, caption=msg.text)
                found = True
                break
        if not found:
            await event.reply("দুঃখিত, এই নামে কোনো অ্যাপ পাওয়া যায়নি।")

client.run_until_disconnected()
