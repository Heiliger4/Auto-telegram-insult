from telethon import TelegramClient, events
import asyncio
import random

api_id = 'xxxxxxxxx'  # Replace xxxxxxxxxx with your API ID
api_hash = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  # Replace xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx with your API hash
phone_number = '+2519xxxxxxxx'  # Replace +2519xxxxxxxx with your phone number

insults = [
    "Even a null pointer exception feels bad for you.",
    "Comments in the code exist because of people like you.",
    "Infinite loops make more sense than your logic.",
    "A syntax error is easier to debug than you.",
    "You’re like a missing semicolon—small but ruins everything.",
    "Your energy is a memory leak—draining everyone.",
    "Deprecated APIs are more useful than you.",
    "Recursive functions have a base case. You don’t.",
    "Deadlocks are less stuck than you.",
    "Your jokes are like a poorly written regex—confusing and broken.",
    "Ante shintam!",
]

client = TelegramClient('session_name', api_id, api_hash)
@client.on(events.NewMessage)
async def handler(event):
    if event.sender_id == xxxxxxxxxxxx:  # Replace xxxxxxxxxxxx with the user ID of the person you want to insult
        await asyncio.sleep(2)
        insult = random.choice(insults)
        await event.reply(insult)

async def main():
    await client.start(phone_number)
    print("Bot is running and listening for messages...")
    await client.run_until_disconnected()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())