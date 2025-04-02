from pyrogram import filters, Client 
import tgcrypto
# Dal modulo pyrogram chiamiamo le funzioni filters e Client
#from pyrogram import message

app = Client(
    session_name= "Cephalon Gioggi", # Nome a scelta della sessione
    api_id= , # api_id tuoi ottenuti da my.telegram.org
    api_hash= "", # api_hash tuoi ottenuti da my.telegram.org
    bot_token= "" # bot_token ottenuto da @BotFather
)

@app.on_message(filters.command(["start"]) & filters.private)
# Abbiamo usato il filtro private, cossìche il bot risponda solo se il messaggio è stato inviato nella sua chat
async def start(app, message):
    await app.send_message(
     message.chat.id,
     text="Cephalon Gioggi è ora in esecuzione, operatore. Usa il comando /lista per vedere la lista degli Warframe presenti in gioco. Usa il comando /cerca <nome warframe> per cercare uno specifico warframe, le sue abilità e il luogo in cui si trovano componenti e schema. Usa il comando /supporto per contattare l'amministratore in caso di problemi e/o consigli"
     )

@app.on_message(filters.command(["helminth"])) 
async def helminth(app,message):
  await app.send_message(
    message.chat.id,
    text="""\nSalve Operatore, questa è una breve guida in merito al sistema Helminth dove potrai trovare le principali informazioni in maniera rapida e semplificata, spero ti sia d'aiuto!
    \nhttps://telegra.ph/Sistema-Helminth-09-24
    """
  )    

@app.on_message(filters.command(["lista"]))
async def lista(app, message):
 await app.send_message(
     message.chat.id,
     text="""Ecco ciò che stava cercando, Operatore
     \nhttps://telegra.ph/Lista-Warframe-06-19"""
     )

@app.on_message(filters.command(["supporto"]))
async def supporto(app, message):
    await app.send_message(
     message.chat.id,
     text="Se hai riscontrato problemi col bot, vuoi dare consigli su certi dettagli o altro, contatta @Gioele0330! Se invece vuoi supportare il Bot e vuoi vederlo migliorare, offrigli un caffè su https://ko-fi.com/cephalongioggi così smetterà di poltrire e lavorerà per voi!"
     )

@app.on_message(filters.command(["comandi"]))
async def supporto(app, message):
    await app.send_message(
     message.chat.id,
    text="""Operatore, ecco la lista dei comandi che posso eseguire:
    \n/lista - Usa il seguente comando per visualizzare la lista dei Warframe presenti in gioco.
    \n/supporto - Usa il seguente comando per richiedere supporto o supportare il mio creatore su https://ko-fi.com/cephalongioggi.
    \n/stickers - Usa il seguente comando per ottenere uno sticker pack!
    \n/cerca - Usa il seguente comando per cercare un Warframe. Attenzione, rispetta la grammatica. Per testare il comando, fai /cerca "nome warframe", come ad esempio /cerca Garuda o /cerca Wisp. 
    \n/guide - Usa il seguente comando per visualizzare la lista di guide create dal sottoscritto per voi!"""
     )

@app.on_message(filters.command(["stickers"]))
async def sticker(app, message):
  await app.send_message(
    message.chat.id,
   text="Operatore, eccoti lo sticker pack a tema della nostra community! https://t.me/addstickers/Gastel"
  )
 
@app.on_message(filters.command (["cerca"]))
async def cerca(app, message):
    #print(message.text)
    text=message.text.split()
    text=text[1]

    if(text=="Garuda" and "garuda"):
        text="""
        \nEcco le informazioni principali su Garuda, Operatore.
        \nhttps://telegra.ph/Garuda-Garuda-Prime-06-26
        """
    else:
     if(text=="Lavos" and "lavos"):
        text="""
     \nEcco le informazioni principali su Lavos, Operatore.
     \nhttps://telegra.ph/Lavos-06-28
     """ 
     else:
      if(text=="Atlas" and "atlas"):
        text="""
        \nEcco le informazioni principali su Atlas, Operatore.
        \nhttps://telegra.ph/Atlas-Atlas-Prime-06-27
        """
      else:
       if(text=="Hildryn" and "hildryn"):
        text="""
       \nEcco le informazioni principali su Hildryn, Operatore.
       \nhttps://telegra.ph/Hildryn-06-25 """
       else:
        if(text=="Mag" and "mag"):
         text="""
        \nEcco le informazioni principali su Mag, Operatore.
        \nhttps://telegra.ph/Mag-Mag-Prime-06-30
          """
        else:
         if(text=="Zephyr" and "zephyr"):
          text="""
        \nEcco le informazione principali su Zephyr, Operatore.
        \nhttps://telegra.ph/Zephyr-Zephyr-Prime-07-03
         """
         else:
          if(text=="Mesa" and "mesa"):
           text="""
        \nEcco le informazione principali su Mesa, Operatore.
        \nhttps://telegra.ph/Mesa-Mesa-Prime-06-30
         """
          else:
           if(text=="Loki" and "loki"):
             text="""
        \nEcco le informazione principali su Loki, Operatore.
        \nhttps://telegra.ph/Loki-Loki-Prime-06-30
             """
           else:
            if(text=="Limbo" and "limbo"):
             text="""
              \nEcco le informazioni principali su Limbo, Operatore.
              \nhttps://telegra.ph/Limbo-Limbo-Prime-06-28
             """
            else:
             if(text=="Banshee" and "banshee"):
              text="""
        \nEcco le informazioni principali su Banshee, Operatore.
        \nhttps://telegra.ph/Banshee-Banshee-Prime-06-27
        """
             else:
              if(text=="Nidus" and "nidus"):
               text="""
        \nEcco le informazione principali su Nidus, Operatore.
        \nhttps://telegra.ph/Nidus-Nidus-Prime-06-30
                 """
              else:
               if(text=="Xaku" and "xaku"):
                 text="""
        \nEcco le informazione principali su Xaku, Operatore.
        \nhttps://telegra.ph/Xaku-07-03
                 """
               else:
                 if(text=="Yareli" and "yareli"):
                  text="""
        \nEcco le informazione principali su Yareli, Operatore.
        \nhttps://telegra.ph/Yareli-07-03
                 """
                 else :
                  if(text=="Baruuk" and "baruuk"):
                   text="""
        \nEcco le informazioni principali su Baruuk, Operatore.
        \nhttps://telegra.ph/Baruuk-06-19
        """
                  else:
                   if(text=="Chroma" and "chroma"):
                    text="""
        \nEcco le informazioni principali su Chroma, Operatore.
        \nhttps://telegra.ph/Chroma-Chroma-Prime-06-27"""
                   else:
                    if(text=="Ember" and "ember"):
                     text="""
        \nEcco le informazioni principali su Ember, Operatore.
        \nhttps://telegra.ph/Ember-Ember-Prime-06-27
        """
                    else:
                     if(text=="Equinox" and "equinox"):
                      text="""
        \nEcco le informazioni principali su Equinox, Operatore.
        \nhttps://telegra.ph/Equinox-Equinox-Prime-06-27
        """
                     else:
                      if(text=="Excalibur" and "excalibur"):
                       text="""
        \nEcco le informazioni principali su Excalibur, Operatore.
        \nhttps://telegra.ph/Excalibur-Excalibur-Umbra-06-27
        """
                      else:
                       if(text=="Frost" and "frost"):
                        text="""
        \nEcco le informazioni principali su Frost, Operatore.
        \nhttps://telegra.ph/Frost-Frost-Prime-06-27
        """
                       else:
                        if(text=="Gara" and "gara"):
                          text="""
        \nEcco le informazioni principali su Gara, Operatore.
        \nhttps://telegra.ph/Gara-Gara-Prime-06-27
        """
                        else:
                         if(text=="Gauss" and "gauss"):
                          text="""
        \nEcco le informazioni principali su Gauss, Operatore.
        \nhttps://telegra.ph/Gauss-06-25
        """
                         else:
                          if(text=="Grendel" and "grendel"):
                            text="""
        \nEcco le informazioni principali su Grendel, Operatore.
        \nhttps://telegra.ph/Grendel-06-25
        """
                          else:
                           if(text=="Harrow" and "harrow"):
                             text="""
        \nEcco le informazioni principali su Harrow, Operatore.
        \nhttps://telegra.ph/Harrow-Harrow-Prime-06-27
        """
                           else:
                            if(text=="Hydroid" and "Hydroid"):
                             text="""
        \nEcco le informazione principali su Hydroid, Operatore.
        \nhttps://telegra.ph/Hydroid-Hydroid-Prime-06-27
     """
                            else:
                             if(text=="Inaros" and "inaros"):
                               text="""
        \nEcco le informazione principali su Inaros, Operatore.
        \nhttps://telegra.ph/Inaros-Inaros-Prime-06-27
     """
                             else:
                              if(text=="Ivara" and "ivara"):
                               text="""
        \nEcco le informazione principali su Ivara, Operatore.
        \nhttps://telegra.ph/Ivara-Ivara-Prime-06-27"""
                              else:  
                               if(text=="Khora" and "khora"):
                                text="""
        \nEcco le informazione principali su Khora, Operatore.
        \nhttps://telegra.ph/Khora-Khora-Prime-09-04
     """
                               else:
                                if(text=="Mirage" and "mirage"):
                                 text="""
        \nEcco le informazione principali su Mirage, Operatore.
        \nhttps://telegra.ph/Mirage-Mirage-Prime-06-30
     """
                                else:
                                 if(text=="Nekros" and "nekros"):
                                  text="""
        \nEcco le informazione principali su Nekros, Operatore.
        \nhttps://telegra.ph/Nekros-Nekros-Prime-06-30
     """
                                 else:
                                    if(text=="Nezha" and "nezha"):
                                     text="""
        \nEcco le informazione principali su Nezha, Operatore.
        \nhttps://telegra.ph/Nezha-Nezha-Prime-06-30
     """
                                    else:
                                     if(text=="Nova" and "nova"):
                                       text="""
        \nEcco le informazione principali su Nova, Operatore.
        \nhttps://telegra.ph/Nova-Nova-Prime-07-02
     """
                                     else:
                                      if(text=="Nyx" and "nyx"):
                                       text="""
        \nEcco le informazione principali su Nyx, Operatore.
        \nhttps://telegra.ph/Nyx-Nyx-Prime-07-02
     """
                                      else:
                                       if(text=="Oberon" and "oberon"):
                                        text="""
        \nEcco le informazione principali su Oberon, Operatore.
        \nhttps://telegra.ph/Oberon-Oberon-Prime-07-02
     """
                                       else:
                                         if(text=="Octavia" and "octavia"):
                                          text="""
        \nEcco le informazione principali su Octavia, Operatore.
        \nhttps://telegra.ph/Octavia-Octavia-Prime-07-02
     """
                                         else:
                                          if(text=="Protea" and "protea"):
                                            text="""
        \nEcco le informazione principali su Protea, Operatore.
        \nhttps://telegra.ph/Protea-07-02
     """
                                          else:
                                           if(text=="Revenant" and "revenant"):
                                            text="""
        \nEcco le informazione principali su Revenant, Operatore.
        \nhttps://telegra.ph/Revenant-Revenant-Prime-10-22
      """
                                           else:
                                            if(text=="Rhino" and "rhino"):
                                             text="""
        \nEcco le informazione principali su Rhino, Operatore.
        \nhttps://telegra.ph/Rhino-Rhino-Prime-07-02
     """
                                            else:
                                             if(text=="Saryn" and "saryn"):
                                               text="""
        \nEcco le informazione principali su Saryn, Operatore.
        \nhttps://telegra.ph/Saryn-Saryn-Prime-07-02
     """
                                             else:
                                              if(text=="Sevagoth" and "sevagoth"):
                                               text="""
        \nEcco le informazione principali su Sevagoth, Operatore.
        \nhttps://telegra.ph/Sevagoth-07-02
      """
                                              else:
                                               if(text=="Titania" and "titania"):
                                                text="""
        \nEcco le informazione principali su Titania, Operatore.
        \nhttps://telegra.ph/Titania-Titania-Prime-07-02
     """
                                               else:
                                                if(text=="Trinity" and "trinity"):
                                                 text="""
        \nEcco le informazione principali su Trinity, Operatore.
        \nhttps://telegra.ph/Trinity-Trinity-Prime-07-03
     """
                                                else:
                                                 if(text=="Valkyr" and "valkyr"):
                                                  text="""
        \nEcco le informazione principali su Valkyr, Operatore.
        \nhttps://telegra.ph/Valkyr-Valkyr-Prime-07-03
     """
                                                 else:
                                                  if(text=="Vauban" and "vauban"):
                                                   text="""
        \nEcco le informazione principali su Vauban, Operatore.
        \nhttps://telegra.ph/Vauban-Vauban-Prime-07-03
     """
                                                  else:
                                                   if(text=="Volt" and "volt"):
                                                    text="""
        \nEcco le informazione principali su Volt, Operatore.
        \nhttps://telegra.ph/Volt-Volt-Prime-07-03
     """
                                                   else:
                                                    if(text=="Wisp" and "wisp"):
                                                     text="""
        \nEcco le informazione principali su Wisp, Operatore.
        \nhttps://telegra.ph/Wisp-07-03
      """
                                                    else:
                                                     if(text=="Wukong" and "wukong"):
                                                      text="""
        \nEcco le informazione principali su Wukong, Operatore.
        \nhttps://telegra.ph/Wukong-Wukong-Prime-07-03
     """
                                                     else:
                                                      if(text=="Caliban" and "caliban"):
                                                       text="""
        \nEcco le informazione principali su Caliban, Operatore.
        \nhttps://telegra.ph/Caliban-06-19
     """
                                                      else:
                                                       if(text=="Gyre" and "gyre"):
                                                        text="""
        \nEcco le informazione principali su Gyre, Operatore.
        \nhttps://telegra.ph/Gyre-06-25
        """
                                                       else:
                                                        if(text=="Ash" and "ash"):
                                                         text="""
      \nEcco le informazioni principali su Ash, Operatore.
      \nhttps://telegra.ph/Ash-Ash-Prime-06-27
     """   
                                                        if(text=="Voruna" and "voruna"):
                                                            text="""
      \nEcco le informazioni principali su Voruna, Operatore
      \nhttps://telegra.ph/Voruna-11-18"""
                                                        else:

                                                         if(text=="Styanax" and "styanax"):
                                                                                text="""
      \nEcco le informazioni principali su Styanax, Operatore
      \nhttps://telegra.ph/Styanax-09-04"""
                                                         else:
                                                                               text="Nessun Warframe trovato, controlla di aver scritto bene e rispetta minuscole e maiuscole!"
                                                                            
    await app.send_message(
    message.chat.id,
    text
    )

@app.on_message(filters.command(["guide"])) 
async def guide(app,message):
  await app.send_message(
    message.chat.id,
    text="""\nEcco una lista di guide che ho creato appositamente per voi! E non preoccupatevi, in caso di bisogno, verranno aggiornate ed aggiunte di nuove!
    \nhttps://telegra.ph/Guide-Warframe-09-27
    """
  )    

app.run()