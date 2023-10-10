from telethon import TelegramClient, events, Button
import asyncio

# Set your API ID, API hash, and phone number with country code
api_id = 28787245
api_hash = '754ad6c7cd9c2817202bc4b2d8eab4e3'
phone_number = '+2347080429713'

client = TelegramClient('session_name', api_id=api_id, api_hash=api_hash)

# Start the client
client.start(phone=phone_number)
print('Client started successfully!')

# Define the channels to forward messages to
destination_channels = ["@Interactive_GoldSignals", "@MetaTraderForex_Signals", "@FreeForexFactory_Signals", "@FreeForex_XaussdSignals", "@Deriv_GoldSignals", "@XAUSSD_FreeFXSignals", "@FXfreepremium_Signals", "@AccurateCrypto_FreeSignals", "@FXpremiere_freeSignal"]
source = "@Deriv_FreeFXSignal"

@client.on(events.NewMessage(chats=[source]))
async def forward_messages(event):
    print(event.message)
    if event.message.text is not None:
        if "DerivBotManager" not in event.message.text:
            if event.message.fwd_from is None:
                if event.message.photo:
                    for channel in destination_channels:
                        await client.send_file(entity=channel, file=event.message.photo, caption=event.message.text)
                elif event.message.photo is None:
                    for channel in destination_channels:
                        await client.send_message(entity=channel, message=event.message.text)
            else:
                for channel in destination_channels:
                    await client.forward_messages(entity=channel, messages=event.message)
    elif event.message.text is None:
        print("hh")
        if event.message.fwd_from is None:
            if event.message.photo:
                for channel in destination_channels:
                    await client.send_file(entity=channel, file=event.message.photo)
        else:
            for channel in destination_channels:
                await client.forward_messages(entity=channel, messages=event.message)

# Run the client until disconnected
client.run_until_disconnected()
