import asyncio
import aiogram
import os
from aiogram import Bot, Dispatcher  , executor ,types 
from aiogram.types import Message ,Video , Audio
import pafy
import pytube
from pytube import YouTube, Search
import requests
from requests import get
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

#token = '1675623193:AAGuJo2e2EBO4m2GHsQVthRA0M46gYuFTL0'
token = '1655671816:AAFdrX2jOt7Xr9LhDCNGIKp1q_opu2VN7U0'   #calc
admin_id =[]
mainadmin = 907267780
#admin_id.append(907267780)
admin_id.append(2137186514)
admin_id.append(5543791558)
# =)
vistik='🎬'
castik='🎥'
downstik='⬇️'
mustik='🎧'
hanstik='👇'
thor='👤'
timer='⏱'

loop=asyncio.get_event_loop()
bot=Bot(token)
dp=Dispatcher(bot,loop=loop)
dedict={}
#_____________________________________________________________________________________________________
@dp.message_handler(commands=['start'])
async def start (message: Message):
	await bot.send_message(chat_id=message.chat.id , text='hello')
#_____________________________________________________________________________________________________
@dp.message_handler(content_types='video')
async def video_handler(message: Message):
	if message.chat.id in admin_id:
		#await bot.send_message(chat_id=mainadmin , text = 'start adminka')
		await adminka(message)
#_____________________________________________________________________________________________________
@dp.message_handler(content_types='audio')
async def audio_handler(message: Message):
	if message.chat.id in admin_id:
		#await bot.send_message(chat_id=mainadmin , text = 'start adminka')
		await adminka(message)
#______________________________________________________________________________________________________
@dp.message_handler(Message)
async def echo(message: Message):
	try:
		kal=YouTube(message.text)
		await mess(message)
	except:
		#await bot.send_message(chat_id=message.chat.id , text='searching video')
		await search(message)
#_______________________________________________________________________________________________________		
async def mess(message , url=None , edit = 'false' ):
	try:
		if url ==None:
			text=message.text
		else:
			text=url
		#await bot.send_message(chat_id=message.chat.id ,text=message)
		#await bot.send_message(chat_id=message.chat.id ,text=text)
		#Скачка фото ____________________________
		yVideo = YouTube(text)
		stream = InlineKeyboardMarkup(row_width=3)
		if edit == 'false': 
			photo=yVideo.thumbnail_url
			pho=yVideo.length
			with open(f'{pho}.jpg', 'wb') as f:
	                    f.write(get(photo).content)
			poto = open(f'{pho}.jpg' , 'rb')
		# выбор качество________________________
		mar=""
		try:
			streams=yVideo.streams.filter(res="1080p" , progressive="True")
			stre = sorted(list(streams), key=lambda f: f.filesize)
			first=stre[-1]
			stream.insert(InlineKeyboardButton( 'res:1080p', callback_data= f'{first.itag} video {text}'))

			mar=mar+ f'{vistik}1080p - {int(first.filesize/1024/1024*100)/100} MB\n'
			#await bot.send_message(chat_id=message.chat.id ,text=f'{first.itag} video {text}')
		except Exception as e:
			pass 
		
		try:
			streams=yVideo.streams.filter(res="720p" , progressive="True")
			stre = sorted(list(streams), key=lambda f: f.filesize)
			first=stre[-1]
			stream.insert(InlineKeyboardButton('res:720p ', callback_data= f'{first.itag} video {text}'))
			mar+=( f'{vistik}720p - {int(first.filesize/1024/1024*100)/100} MB\n')

		except:
			pass
		try:
			streams=yVideo.streams.filter(res="480p", progressive="True")
			stre = sorted(list(streams), key=lambda f: f.filesize)
			first=stre[-1]
			stream.insert(InlineKeyboardButton( f'res:480p ', callback_data= f'{first.itag} video {text}'))
			mar+= f'{vistik}480p - {int(first.filesize/1024/1024*100)/100} MB\n'
			#await bot.send_message(chat_id=message.chat.id ,text=f'{first.itag} video {text}')
		except:
			pass
		try:
			streams=yVideo.streams.filter(res="360p", progressive="True")
			stre = sorted(list(streams), key=lambda f: f.filesize)
			first=stre[-1]
			stream.insert(InlineKeyboardButton( f'res:360p ', callback_data= f'{first.itag} video {text}'))
			mar+= f'{vistik}360p - {int(first.filesize/1024/1024*100)/100} MB\n'
			#await bot.send_message(chat_id=message.chat.id ,text=f'{first.itag} video {text}')
		except:
			pass
		try:
			streams=yVideo.streams.filter(res="240p", progressive="True")
			stre = sorted(list(streams), key=lambda f: f.filesize)
			first=stre[-1]
			stream.insert(InlineKeyboardButton( f'res:240p ', callback_data= f'{first.itag} video {text}'))
			mar+= f'{vistik}480p - {int(first.filesize/1024/1024*100)/100} MB\n'
		except:
			pass
		try:
			streams=yVideo.streams.filter(res="144p", progressive="True")
			stre = sorted(list(streams), key=lambda f: f.filesize)
			first=stre[-1]
			stream.insert(InlineKeyboardButton( f'res:144p ', callback_data= f'{first.itag} video {text}'))
			mar+=f'{vistik}144p - {int(first.filesize/1024/1024*100)/100} MB\n'
		except Exception as e:
			await bot.send_message(chat_id=message.chat.id , text=f'Message Error\n\n{e}')

		#audio_codec--------------------
		try:
			streams=yVideo.streams.filter(type="audio")
			stre = sorted(list(streams), key=lambda f: f.filesize)
			first=stre[-1]
			stream.insert(InlineKeyboardButton( f'audio', callback_data= f'{first.itag} audio {text}'))
			mar+=f'{mustik}audio-{int(first.filesize/1024/1024*100)/100} MB\n'
		except Exception as e:
			await bot.send_message(chat_id=message.chat.id , text=f'Message Error\n\n{e}')

		# sending >>> 
		if edit == 'false':	
			await bot.send_photo(
				chat_id=message.chat.id ,
				photo=poto,
				caption= f'{yVideo.title}\n\nchoose one of them{hanstik}\n\n{mar}' ,
				reply_markup=stream)
			#REMOVE QUERY---
			os.remove(f'{pho}.jpg')
			await bot.delete_message(message.chat.id , message.message_id)

		else:
			await bot.edit_message_caption(
				chat_id = message.chat.id,
				message_id=message.message_id,
				caption = f'{yVideo.title}\n\nchoose one of them{hanstik}\n\n{mar}',
				reply_markup = stream)

	except Exception as e:
		await bot.send_message(chat_id=message.chat.id , text=f'Message lih Error\n\n{e}')
#____________
client = 0
#CallBack of Quality_____________________________________________________________________________________________
@dp.callback_query_handler(lambda c: len(list(c.data.split()))==3)
async def callback(callback_query: types.CallbackQuery):
	try:
		global client
		if client >= len(admin_id) - 1:
			client = 0
		else:
			client+=1
	except Exception as e:
		await bot.send_message(chat_id=callback_query.message.chat.id, text=f'Message client up  Error\n\n{e}')
	try:
		try:
			id=callback_query.message.message_id
			chat=callback_query.message.chat.id
			await bot.delete_message(chat, id)
		except Exception as e:
			await bot.send_message(chat_id=mainadmin , text =f'Message call ID,chat Error: {e}')
		text=callback_query.data
		d ,format ,  url = text.split()
		#await bot.send_message(chat_id=callback_query.from_user.id , text='I_working_2')
		# Sending download data to admin bot_______________
		await bot.send_message(chat_id=admin_id[client] , text=f'{callback_query.from_user.id}  {url}  {d} {format}')
	except Exception as e:
		await bot.send_message(chat_id=mainadmin , text =f'Message call quality Error: {e}')

#_______________________________________________________________________________________________________________
async def adminka(Video):
	#await bot.send_message(chat_id=mainadmin , text = 'adminka')
	chat_id=int(Video.caption)
	await bot.copy_message(chat_id=chat_id, from_chat_id=Video.chat.id, message_id=Video.message_id , caption='')

#_______________________________________________________________________________________________________________
async def search(message):
	try: 
		try:
			text=message.text
			video=Search(text)
			Video=video.results
			if len(Video)==0:
				await 	bot.send_message(chat_id=message.message_id , text ="incorrect request")
				return

			vvv,svideo=str(Video[0]).split('=')

			yVideo = YouTube(f'https://www.youtube.com/watch?v={svideo[0:len(svideo)-1]}')
		except Exception as e:
			await bot.send_message(chat_id=mainadmin , text =f'Message Searching data Error: {e}')

		stream = InlineKeyboardMarkup(row_width=2)
		photo=yVideo.thumbnail_url
		pho=yVideo.length
		x=yVideo.length

		try:
			with open(f'{pho}.jpg', 'wb') as f:
      	 		            f.write(get(photo).content)
		except Exception as e:
			await bot.send_message(chat_id=mainadmin , text =f'Message searhing photo_downloading Error: {e}')

		poto = open(f'{pho}.jpg' , 'rb')
		
		stream.insert(InlineKeyboardButton( f'--->' ,  callback_data= f'1 {text}  0 forward'))
		stream.add(InlineKeyboardButton( f'Download' ,  callback_data= f'https://www.youtube.com/watch?v={svideo[0:len(svideo)-1]}'))
		#sending >>>>
		await bot.send_photo(chat_id=message.chat.id ,
						photo=poto,
						#thumb=poto,
						caption=  f'{yVideo.title}\n {thor}Author: {yVideo.author}\n {timer} {int(x/3600)}:{int(x/60-int(x/3600)*60)}:{x-int(x/60-int(x/3600)*60)*60}\n   search: {text}' ,
						reply_markup=stream)
		os.remove(f'{pho}.jpg')

	except Exception as e:
		await bot.send_message(chat_id=mainadmin , text =f'Message Search Error: {e}')

#Search CallBack __________________________________________________________________________________________________________
@dp.callback_query_handler(lambda c: len(list((c.data).split()))==4)
async def calack(callback_query: types.CallbackQuery):
	try:	
		#await bot.send_message(chat_id=callback_query.message.chat.id ,text='I_working')
		text=callback_query.data
		k, url,d, point =text.split()
		d=int(d)

		if point=="back":
			d=d-1
		else: 
			d=d+1

		video=Search(url)
		Video=video.results
		vvv , svideo=str(Video[d]).split('=')
		yVideo = YouTube(f'https://www.youtube.com/watch?v={svideo}') #[0:len(svideo)-1]
		stream = InlineKeyboardMarkup(row_width=2)

		photo=yVideo.thumbnail_url
		with open(f'{url}.jpg', 'wb') as f:
			f.write(get(photo).content)
		#poto = open(f'{url}.jpg' , 'rb')
		file =  open(f'{url}.jpg', 'rb')
		x=yVideo.length
		caption = f'{yVideo.title}\n {thor}Author: {yVideo.author}\n {timer} {int(x/3600)}:{int(x/60-int(x/3600)*60)}:{x-int(x/60-int(x/3600)*60)*60}\n   search: {url}'  
		poto = types.InputMediaPhoto( file , caption = caption)

		if d>0:
			stream.insert(InlineKeyboardButton( f'<---' ,  callback_data= f'1 {url}  {d} back'))
		if d<34:
			stream.insert(InlineKeyboardButton( f'--->' ,  callback_data= f'1 {url}  {d} forward'))
		stream.add(InlineKeyboardButton( f'Download' ,  callback_data= f'https://www.youtube.com/watch?v={svideo[0:len(svideo)-1]}'))
		#await bot.delete_message(callback_query.message.chat.id , callback_query.message.message_id)
		#await bot.send_photo(chat_id=callback_query.message.chat.id ,
		#			photo=poto,
		#			caption= f'{yVideo.title}\n {thor}Author: {yVideo.author}\n {timer} {int(x/3600)}:{int(x/60-int(x/3600)*60)}:{x-int(x/60-int(x/3600)*60)*60}\n   search: {url}' ,
		#			reply_markup=stream)
		
		await bot.edit_message_media(
			chat_id      = callback_query.message.chat.id , 
			message_id   = callback_query.message.message_id,
			media        = poto,
			reply_markup = stream
		)

		# await bot.send_message(chat_id = callback_query.message.chat.id , text = f'{callback_query.message.message_id}')
		os.remove(f'{url}.jpg')

	except Exception as e:
		await bot.send_message(chat_id=mainadmin , text =f'Message Error: {e}')

#______________________________________________________________________________________________________________________
@dp.callback_query_handler(lambda c: len(list((c.data).split()))==1)
async def caack(callback_query: types.CallbackQuery):
	#await bot.send_message(chat_id=callback_query.message.chat.id ,text='I_caak')
	await mess(callback_query.message  , callback_query.data , 'true' )
executor.start_polling(dp)
