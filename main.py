import telebot # Yeh humara package hai jo abhi install kiya hai
import time # Bot ko restart hone par thoda wait karne ke liye

# Tumhara Telegram bot token (jo tumne diya tha)
BOT_TOKEN = '7882537126:AAEBOGNN03dT4j1jZRjgl3p9tys6J6ZWtQI' 

# Bot object banate hain
bot = telebot.TeleBot(BOT_TOKEN)

# Yeh function /start command ko handle karega
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Namaste! Main tumhara naya bot hu. Ab main Flask ke bina chal raha hu.")

# Bot ko hamesha chalu rakhne ke liye polling
def start_bot_polling():
    while True: # Infinite loop taaki bot chalta rahe
        try:
            print("Bot chalne ke liye taiyar hai...")
            # none_stop=True bot ko hamesha chalu rakhta hai, reconnect karega agar disconnect ho
            bot.polling(none_stop=True, interval=0, timeout=20) 
        except Exception as e:
            print(f"Bot mein error aayi: {e}")
            print("20 seconds mein bot ko phir se shuru kar raha hu...")
            time.sleep(20) # Error aane par 20 second wait kare aur phir se try kare

if __name__ == "__main__":
    start_bot_polling()
