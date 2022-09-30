from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.database import  insert 

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
	insert(int(message.chat.id))
	await message.reply_text(text =f"""
	
        photo="START_PIC" ,url="https://telegra.ph/file/7751a3ea7ce9ce85d8b4e.jpg") ]  ])) 
   
	Hey buddy 👋 {message.from_user.first_name }
	
🔸️I'AM A FAST RENAMER BOT WITH PERMAENENT THUMNAIL SUPPORT.

💠 SEND ME A FILE OR VIDEO.

💠 SEND A IMAGE TO SAVE AS THUMBNAIL.

💠 CHOOSE A SUITABLE OPTION.

💠 PROCESS WILL GET SATRTED WAIT FOR SOME TIME!

💠 OWNER : @Sanaticsmovies 

**◾ JOIN OUR CHANNEL AND SUPPORT US **
	""",reply_to_message_id = message.message_id ,  
	reply_markup=InlineKeyboardMarkup(
	 [[ InlineKeyboardButton("Sanaticsmovies" ,url="https://t.me/sanaticsmovies") ]  ]))


@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       media = await client.get_messages(message.chat.id,message.message_id)
       file = media.document or media.video or media.audio 
       filename = file.file_name
       filesize = humanize.naturalsize(file.file_size)
       fileid = file.file_id
       await message.reply_text(
       f"""__𝘞𝘩𝘢𝘵 𝘋𝘰 𝘠𝘰𝘶 𝘞𝘢𝘯𝘵 𝘔𝘦 𝘛𝘰 𝘋𝘰 𝘞𝘪𝘵𝘩 𝘛𝘩𝘪𝘴 𝘍𝘪𝘭𝘦?__\n**File Name** :- {filename}\n**File Size** :- {filesize}"""
       ,reply_to_message_id = message.message_id,
       reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("✏ Rename ✏",callback_data = "rename")
       ,InlineKeyboardButton("Cancel ❌",callback_data = "cancel")  ]]))
