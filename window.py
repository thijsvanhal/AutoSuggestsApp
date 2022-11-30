from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar
import tkinter.font as TkFont
import pandas as pd
import cmath
import requests
import json
import time
import os
import sys
import string
import threading
from platform import system
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
import nltk
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
from nltk.corpus import stopwords
from collections import Counter
from json import loads

#Variabelen
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./")
clusterdf = " "

#Functies
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def start():
    global clusterdf
    canvas.itemconfig(mytext, text="Ophalen", anchor='nw')
    #language code and keywords
    keyword1= entry_2.get()
    keyword2= entry_3.get()
    keyword3= entry_4.get()
    keyword4= entry_5.get()
    keyword5= entry_6.get()
    lang_code= entry_1.get().lower()
    
    #generate keyword list
    keywords=[keyword1,keyword2,keyword3,keyword4,keyword5]
    keywordlist = list(filter(None, keywords))

    #Make a list of letters to use for Google Suggest
    letterlist=[""]
    letterlist=letterlist+list(string.ascii_lowercase + string.digits)

    #Google Suggest for each combination of keyword and letter
    keywordsuggestions=[]
    for keyword in keywordlist: 
      for letter in letterlist :
        URL="https://suggestqueries.google.com/complete/search?client=firefox&hl="+str(lang_code)+"&q="+keyword+" "+letter
        headers = {'User-agent':'Mozilla/5.0'} 
        response = requests.get(URL, headers=headers) 
        result = json.loads(response.content.decode('utf-8'))
        keywordsuggest=[keyword,letter] 
        for word in result[1]:
          if(word!=keyword):
            keywordsuggest.append(word)
        time.sleep(0.5)
        keywordsuggestions.append(keywordsuggest)
    #create a dataframe from this list
    keywordsuggestions_df = pd.DataFrame(keywordsuggestions)
    
    #Rename columns of dataframe
    columnnames=["Keyword","Letter"]
    for i in range(1,len(keywordsuggestions_df.columns)-1):
      columnnames.append("Suggestion"+str(i))
    keywordsuggestions_df.columns=columnnames
    
    #Make a list of all suggestions
    allkeywords = keywordlist
    for i in range(1,len(keywordsuggestions_df.columns)-1):
      suggestlist = keywordsuggestions_df["Suggestion"+str(i)].values.tolist()
      for suggestion in suggestlist:
        allkeywords.append(suggestion)

    taal=""
    if lang_code == "nl":
        taal="dutch"
    elif lang_code == "en":
        taal="english"
    elif lang_code == "fr":
        taal="french"
    elif lang_code == "de":
        taal="german"
        
    #exclude stopwords and seed keywords from this list
    stop_words = set(stopwords.words(taal))
    wordlist=[]
    seed_words=[]
    for keyword in keywords:
       for seed_word in nltk.word_tokenize(str(keyword).lower()):
         if(len(seed_word)>0):
           seed_words.append(seed_word)
    for keyword in allkeywords:
       words = nltk.word_tokenize(str(keyword).lower()) 
       #word tokenizer
       for word in words:
         if(word not in stop_words and word not in seed_words and len(word)>1):
          wordlist.append(word)

    #find the most common words in the suggestions
    most_common_words= [word for word, word_count in Counter(wordlist).most_common(200)]

    #assign each suggestion to a common keyword
    clusters=[]
    for common_word in most_common_words:
        for keyword in allkeywords:
          if(common_word in str(keyword)):
             clusters.append([keyword,common_word])
    clusterdf = pd.DataFrame(clusters,columns=['Keyword', 'Cluster'])
    canvas.itemconfig(mytext, text="Klaar ✅", anchor='nw')

def startStart():
    threading.Thread(target=start).start()

def kopie():
    global clusterdf
    clusterdf.to_clipboard(excel=True, index=False)
    canvas.itemconfig(mytext, text="Kopie ✅", anchor='nw')

def csv():
    global clusterdf
    clusterdf.columns = ['Keyword', 'Ad Group']
    clusterdf.to_csv(r'~/Downloads/zoekwoorden.csv', index=False)
    canvas.itemconfig(mytext, text="CSV ✅", anchor='nw')

#Tkinter
window = Tk()
window.title('AutoSuggestsApp')

#font
font = TkFont.Font(family="Mada",size=20)
window.option_add( "*font", font )

#logo
platformD = system()
if platformD == 'Windows':

    logo_image = relative_to_assets('logo.ico')
    window.iconbitmap(logo_image)

else:

    print("")

#default language
v = StringVar(window, value='NL')

window.geometry("700x700")
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 700,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas_background = PhotoImage(
    file=relative_to_assets("background.png"))

canvas.place(x = 0, y = 0)
canvas_bg = canvas.create_image(
    350,
    350,
    image=canvas_background
)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    564.5,
    200.0,
    image=entry_image_1
)

entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    fg = "#02343F",
    insertbackground = "#02343F",
    justify = "center",
    textvariable = v,    
)
entry_1.place(
    x=538.0,
    y=189.0,
    width=53.0,
    height=22.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    349.0,
    243.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    fg = "#02343F",
    insertbackground = "#02343F",
)
entry_2.place(
    x=107.0,
    y=226.0,
    width=484.0,
    height=35.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    221.0,
    318.96295166015625,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    fg = "#02343F",
    insertbackground = "#02343F",    
)
entry_3.place(
    x=107.0,
    y=300.96295166015625,
    width=228.0,
    height=35.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    477.0,
    318.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    fg = "#02343F",
    insertbackground = "#02343F",    
)
entry_4.place(
    x=363.0,
    y=300.0,
    width=228.0,
    height=35.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    221.0,
    393.96295166015625,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    fg = "#02343F",
    insertbackground = "#02343F",    
)
entry_5.place(
    x=107.0,
    y=377.96295166015625,
    width=228.0,
    height=35.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    477.0,
    394.7407531738281,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0,
    fg = "#02343F",
    insertbackground = "#02343F",    
)
entry_6.place(
    x=363.0,
    y=378.7407531738281,
    width=228.0,
    height=35.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=kopie,
    relief="flat"
)
button_1.place(
    x=358.0,
    y=558.0,
    width=238.0,
    height=40.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=csv,
    relief="flat"
)
button_2.place(
    x=102.0,
    y=558.0,
    width=238.0,
    height=40.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=startStart,
    relief="flat"
)
button_3.place(
    x=102.0,
    y=448.96295166015625,
    width=494.0,
    height=49.90740966796875
)

mytext = canvas.create_text(
    169.0,
    510.0,
    anchor="nw",
    text="Wachten",
    fill="#02343F",
    font=("Mada Medium", 20 * -1)
)
window.resizable(False, False)
window.mainloop()
