from pyrogram import Client
from pyrogram.types import CallbackQuery
import logging , os 

class PepitoBot():
    def __init__(self):
        self.app = Client(
            "PepitoBot",
            api_id    = 26567703 ,
            api_hash  = '313f7ffe09155222946a65c09225d834',
            bot_token = '8004193792:AAF0ws17QmIbuLxzG7RF6kl_v3U9DHXa7UI',
            plugins   =  dict(root="plugins"))

        @self.app.on_callback_query()
        def clod(client, call: CallbackQuery):
            data = call.data.split(":")

            if call.from_user.id != int(data[1]):return call.answer("Botones bloqueados.")
            else: call.continue_propagation()

    def runn(self):
        os.system("cls")
        logging.basicConfig(level=logging.INFO)
        self.app.run()


if __name__ == "__main__":
    PepitoBot().runn()
    ""
    
#Note: Colocar las proxys aunque por defecto andan desactivadas en session