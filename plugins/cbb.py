#(Β©)kakahsi

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"πββπΈββπΌππ βπΈβπβπΌβππ\n<b>Β§ 01 : <a href=''>Channel</a>\nΒ§ 02 : <a href=''>Channel</a>\nΒ§ 03 : <a href='https://'>Channel</a>\nΒ§ Twitter : <a href='?s=08'>KEPO</a>\nΒ§ Facebook : - \nΒ§ Owner : @K4N3N</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("ππΌβπ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
