import telebot
from app import *

TOKEN = "6977590067:AAGYgmFWZTk3RsnDricMtwRr10LEsPWSius"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start", "help"])
def welcome_message(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Merhaba, sizin için YouTube videolarını indirebilirim :)")
    bot.send_message(chat_id, "Videoyu indirmek için /video <video çözünürlüğü> <video bağlantısı> gönderin")
    bot.send_message(chat_id, "Sesi indirmek için /mp <video url>'sini gönderin")

# Handeling audio requests

@bot.message_handler(commands=["mp"])
def audio_dwonloader(message):
    chat_id = message.chat.id
    message_text = message.text
    splitted_message = message_text.split()
    link = splitted_message[-1]
    video_details = video_info(link)
    file_title = title_finder(link)
    the_audio_file = audio_dl(link)
    new = replace_characters(file_title)
    audio_to_send = open(f'{new}.mp4', 'rb')
    bot.send_audio(chat_id, audio_to_send, caption=video_details)

# Handeling video requests 
@bot.message_handler(commands=["video"])
def video_downloader(message):
    chat_id = message.chat.id
    message_text = message.text
    splitted_message = message_text.split()
    link = splitted_message[-1]
    res = splitted_message[-2]
    video_details = video_info(link)
    bot.send_message(chat_id, f"İşte Youtube'un bana verdiği şey \n\n{video_details}")
    file_title = title_finder(link)
    new = replace_characters(file_title)
    if res == "360":
        bot.send_message(chat_id,"360p çözünürlükte indiriyorum")
        result_video_file = video_dl_360(link)
        result_video_file_to_send = open(f'{new}.mp4', 'rb')
        bot.send_video(chat_id, result_video_file_to_send)
    elif res == "720":
        bot.send_message(chat_id,"720p çözünürlükte indiriyorum")
        result_video_file = video_dl_720(link)
        result_video_file_to_send = open(f'{new}.mp4', 'rb')
        bot.send_video(chat_id, result_video_file_to_send)
    elif res == "1080":
        bot.send_message(chat_id,"1080p çözünürlükte indiriyorum")
        result_video_file = video_dl_1080(link)
        result_video_file_to_send = open(f'{new}.mp4', 'rb')
        bot.send_video(chat_id, result_video_file_to_send)
    else:
        bot.send_message("Geçersiz çözünürlük seçimi ;_;")


# Handle other commands
@bot.message_handler(commands=["help"])
def help_message(message):
    chat_id = message.chat.id
    text = "If you are facing problem while using this bot, refer to this post for more example"
    bot.send_message(chat_id, text)

@bot.message_handler(commands=["about"])
def about_message(message):
    chat_id = message.chat.id
    text = "This project was started as a side project, then it got picked for a full fledged project by my friends, and here we are...\n\nAnurag Dubey \nAkash Raj Nigam \nAishita Saxena \nAastha Khare"
    bot.send_message(chat_id, text)

@bot.message_handler(commands=["repo"])
def repo_message(message):
    chat_id = message.chat.id
    text = "Here is the GitHub Repository for this Bot:\n\nhttps://github.com/Anuragd275/yt_dl_bot"
    bot.send_message(chat_id, text)

@bot.message_handler(commands=["playlist", "audioplaylist"])
def playlist_message(message):
    chat_id = message.chat.id
    text = "This feature is currently in development, please try again later."
    bot.send_message(chat_id, text)




bot.infinity_polling()
