#(©)Codexbotz

import pyromod.listen
from pyrogram import Client
import sys

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, CHANNEL_ID

class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()

        if FORCE_SUB_CHANNEL:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                self.invitelink = link
            except:
                self.LOGGER(__name__).warning("Bot tidak dapat Mengekspor tautan Undangan dari Force Sub Channel!")
                self.LOGGER(__name__).warning("COBA CEK UDAH DOJADIIN ADMIN LOM BOTNYA?")
                self.LOGGER(__name__).info("\nBOT BERHENTI UNTUK BANTUAN https://t.me/K4N3N")
                sys.exit()
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning("Pastikan bot adalah Admin di DB Channel, dan periksa kembali Nilai CHANNEL_ID")
            self.LOGGER(__name__).info("\nBOT BERHENTI UNTUK BANTUAN https://t.me/K4N3N")
            sys.exit()

        self.set_parse_mode("html")
        self.LOGGER(__name__).info(f"BOT BERJALAN..!\n\nCreated by ALEX ")
        self.username = usr_bot_me.username

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("BOT BERHENTI.")
