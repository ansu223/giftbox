from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

# Replace with your bot token
BOT_TOKEN = '7432253073:AAFTts6hbQ0ehD9D_uyGG9MBeYiLBsO4HOg'

# File containing chat IDs
CHAT_IDS_FILE = 'chat_ids.txt'

# Initialize the bot
bot = Bot(token=BOT_TOKEN)

def send_messages():
    # Message text
    message_text = "Hello! Check out this link:"

    # Create an inline keyboard with a button
    keyboard = [
        [InlineKeyboardButton("Visit My Website", url="https://example.com")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Read chat IDs from the file
    with open(CHAT_IDS_FILE, 'r') as file:
        chat_ids = file.read().splitlines()

    # Remove duplicates (optional, if you want to send only one message per user)
    chat_ids = list(set(chat_ids))

    # Send the message to all chat IDs
    for chat_id in chat_ids:
        try:
            bot.send_message(chat_id=chat_id, text=message_text, reply_markup=reply_markup)
            print(f"Message sent to {chat_id}")
        except Exception as e:
            print(f"Failed to send message to {chat_id}: {e}")

    print("Broadcast completed.")

if __name__ == '__main__':
    send_messages()