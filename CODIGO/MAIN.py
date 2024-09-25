import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, MenuButtonWebApp
from CONFIG import*

bot = telebot.TeleBot(TOKEN)

def set_webapp_button(chat_id):
    web_app_info = WebAppInfo(url=MINI_APP_URL)
    menu_button = MenuButtonWebApp(type="web_app", text="🎮 JOGAR", web_app=web_app_info)
    bot.set_chat_menu_button(chat_id=chat_id, menu_button=menu_button)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    set_webapp_button(message.chat.id)

    markup = InlineKeyboardMarkup()
    web_app_button = InlineKeyboardButton(
        text="🎮JOGAR AGORA", 
        web_app=WebAppInfo(url=MINI_APP_URL)
    )
    
    markup.add(web_app_button)
    
    bot.send_message(
        message.chat.id, 
        "😃Olá! Pronto para jogar o Memory Game?\n\n👇 Clique no botão abaixo para começar:",
        reply_markup=markup
    )

@bot.message_handler(commands=['help'])
def send_help(message):
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton("🧑‍💻CRIADOR", url="https://t.me/VILHALVA100")
    button2 = InlineKeyboardButton("📢CANAL", url="https://t.me/VILHALVA100_CANAL")
    button3 = InlineKeyboardButton("🐱FONTE", url="https://github.com/VILHALVA/MEMORY-GAME")
    markup.add(button1, button2, button3)
    
    bot.send_message(
        message.chat.id, 
        "👇Clique nos botões abaixo para acessar aos subsídios:",
        reply_markup=markup
    )

if __name__ == '__main__':
    print("BOT EM EXECUÇÃO!")
    bot.infinity_polling(timeout=60)
