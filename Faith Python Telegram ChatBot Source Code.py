import telebot
from telebot import types

#bot = telebot.TeleBot(<TOKEN>)
chat_id = -1001142641475


Ursaia = -1001142641475
Fenrir = -1001444193301
#bot chat:-1001380399945
#House comm: -189986429
Ishaan = 607666667
Faith = 540123505
#zhili = 83939701
#sabrina = 195584732
updates = bot.get_updates()
'''
@bot.message_handler(func=lambda message: True)
def echo_messages(message):
    """
    Echoes all incoming messages of content_type 'text'.
    """
    print()
    bot.send_message
    if message.from_user.id != Ishaan or Faith:
        name = message.from_user.first_name
        bot.send_message(chat_id, f"Hello {name},  :( My Ishaan is so handsome <3!" )
    
    if message.from_user.id == Ishaan:
        bot.send_message(chat_id, 'Good Morning Ishaan! Lets go on our date today! <3')

    if message.from_user.id == Faith:
        bot.send_message(chat_id, "Hello imposter @faithortammy! Why you copy me :( last warning don't steal Ishaan ah")

'''
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "press /faith instead")


@bot.message_handler(commands=['faith'])
def profile(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Faith Profile')
    itembtn2 = types.KeyboardButton('Favourite Drink')
    itembtn3 = types.KeyboardButton('Favourite Movie')
    itembtn4 = types.KeyboardButton('See me Laugh')
    itembtn5 = types.KeyboardButton('Why am I called Faith?')
    itembtn6 = types.KeyboardButton('Shocked Faith')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
    bot.send_message(chat_id, "What do want to know about me?", reply_markup=markup)
    
@bot.message_handler(content_types = ['text'], func = lambda message : message.text == 'Faith Profile')
def profile1(message):
        photo = open('C:\\Users\\Zhili\\Desktop\\Ursaia\\Faith Bot\\Faith Photos\\Faith Profile.jpg','rb')
        bot.send_photo(chat_id, photo)
        bot.send_message(chat_id, "Howdy, I am Faith Tammy, a Year 2 Pharmacy Major, NUS Pharmaceutical Society (Director Of Marketing And Public Relations) :) Do hit me up")

@bot.message_handler(content_types = ['text'], func = lambda message : message.text == 'Favourite Drink')
def profile2(message):
        photo = open('C:\\Users\\Zhili\\Desktop\\Ursaia\\Faith Bot\\Faith Photos\\bubbletea.jpg','rb')
        bot.send_photo(chat_id, photo)
        bot.send_message(chat_id, "Hello boys, my favourite Bubble Tea is Koi Milk Tea with Golden Bubbles 25% Sugar!")

@bot.message_handler(content_types = ['text'], func = lambda message : message.text == 'Favourite Movie')
def profile3(message):
        photo = open('C:\\Users\\Zhili\\Desktop\\Ursaia\\Faith Bot\\Faith Photos\\UA 1.jpg','rb')
        bot.send_photo(chat_id, photo)
        bot.send_message(chat_id, "Howdy, my favourite show is Umbrella Academy! Im so Fabulousss!")

@bot.message_handler(content_types = ['text'], func = lambda message : message.text == 'See me Laugh')
def profile4(message):
        photo = open('C:\\Users\\Zhili\\Desktop\\Ursaia\\Faith Bot\\Faith Photos\\Faith mugshot.jpg','rb')
        bot.send_photo(chat_id, photo)
        bot.send_message(chat_id, "HAHAHAHAHAHAHAHAHA YOU'RE SO FUNNY")

@bot.message_handler(content_types = ['text'], func = lambda message : message.text == 'Why am I called Faith?')
def profile5(message):
        photo = open('C:\\Users\\Zhili\\Desktop\\Ursaia\\Faith Bot\\Faith Photos\\heaven.jpg','rb')
        bot.send_photo(chat_id, photo)
        bot.send_message(chat_id, "I am called faith because I am Faithful teehee")

@bot.message_handler(content_types = ['text'], func = lambda message : message.text == 'Shocked Faith')
def profile5(message):
        photo = open('C:\\Users\\Zhili\\Desktop\\Ursaia\\Faith Bot\\Faith Photos\\shockedfaith.mp4','rb')
        bot.send_video(chat_id, photo)
        bot.send_message(chat_id, "OMG Ishaann!")
'''
@bot.message_handler(content_types = ['text'], user_id == 195584732 and func = lambda message: True )
def profile5(message):
        bot.send_message(chat_id, "Hello Sabrina!")
    '''


@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "Type 1 of the following: /start, Faith Profile, Favourite Drink, Favourite Movie, See me Laugh")
	'''
@bot.message_handler(commands=['faithstory'])
def profile(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('F1')
    itembtn2 = types.KeyboardButton('F2')
    itembtn3 = types.KeyboardButton('F3')
    itembtn4 = types.KeyboardButton('F4')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(chat_id, "The Love Story Begins...", reply_markup=markup)

@bot.message_handler(content_types = ['text'], func = lambda message : message.text == 'F1')
def profile4(message):
        photo = open('C:\\Users\\Zhili\\Desktop\\Ursaia\\Faith Bot\\Faith Photos\\Faith Profile.jpg','rb')
        bot.send_photo(chat_id, photo)
        bot.send_message(chat_id, "Omg HI ISHAAN!! I am Faith Tammy!" )

@bot.message_handler(content_types = ['text'], func = lambda message : message.text == 'F2')
def profile4(message):
        bot.send_message(chat_id, "Oh really? awww im flattered!! Omo are you attached?")

@bot.message_handler(content_types = ['text'], func = lambda message : message.text == 'F3')
def profile4(message):
        bot.send_message(chat_id, "You can spend your life with me if you want")

@bot.message_handler(content_types = ['text'], func = lambda message : message.text == 'F4')
def profile4(message):
        bot.send_message(chat_id, "OMG OMG OMG.... Yes and Yes!!! Can't wait to see you tmr")
'''

'''
@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, "You got the wrong input")
        '''

bot.polling()

