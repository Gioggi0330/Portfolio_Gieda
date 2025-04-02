import os
import random
from pyrogram import Client, filters

# Cartella dove sono salvate le immagini
IMAGE_FOLDER = r""

# Variabile per tenere traccia dell'ultima immagine inviata
last_sent_image = None


app = Client(
    "Jeff_TheSharkBot", # Nome a scelta della sessione
    api_id= , # api_id tuoi ottenuti da my.telegram.org
    api_hash= "b6259737568a06a8e73d3fcca3f8bfdc", # api_hash tuoi ottenuti da my.telegram.org
    bot_token="" # Token del bot ottenuto da @BotFather
   )

# Comando /start per salutare l'utente
@app.on_message(filters.command("start"))
def start(client, message):
    message.reply("Mrrr! Io sono Jeff, il piccolo squalo di terra! Usa il comando /jeff per vedermi!")

# Comando /jeff per inviare un'immagine casuale
@app.on_message(filters.command("jeff"))
def jeff(client, message):
    global last_sent_image
    
    # Verifica se la cartella esiste
    if not os.path.exists(IMAGE_FOLDER):
        message.reply("Oh oh! Credo ci sia un errore! Contatta @Gioggi0330 per ricevere assistenza!")
        return

    # Ottieni una lista di tutti i file nella cartella
    images = [f for f in os.listdir(IMAGE_FOLDER) if f.lower().endswith(('jpg', 'jpeg', 'png', 'gif'))]
    
    if images:
        # Se ci sono immagini, ne viene unviata una casuale, escludendo l'ultima inviata per evitare ripetizioni
        available_images = [img for img in images if img != last_sent_image]
        
        if not available_images:
            available_images = images
        
        random_image = random.choice(available_images)
        image_path = os.path.join(IMAGE_FOLDER, random_image)
        
        # Invia l'immagine
        message.reply_photo(image_path)
        
        # Aggiorna l'ultima immagine inviata
        last_sent_image = random_image
    else:
        message.reply("Non ci sono immagini nella cartella!")

# Avvia il bot
app.run()