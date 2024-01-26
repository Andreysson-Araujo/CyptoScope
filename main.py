from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image



import requests
import json

##########CORES#########

co0 = "#444466" #Black
co1 = "#FEFFFF" #White
co2 = "#6f9fbd" #Blue



fundo = "#000000" 



##########Janela#########
janela =  Tk()
janela.title("CryptoScope")
janela.geometry("320x350")
janela.configure(bg=fundo)

#========Dividindo janela =======
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

frame_up = Frame(janela, width=320, height=70, bg=co1, pady=0, padx=0, relief="flat")
frame_up.grid(row=1, column=0)

frame_down = Frame(janela, width=320, height=280, bg=fundo, pady=0, padx=0, relief="flat")
frame_down.grid(row=2, column=0, sticky=NW)



#função para pegar dados
def info():
  api_link = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD%2CAOA%2CBRL";

  #----- HTTP Request
  response = requests.get(api_link)

  #--- convertendo dos dados em json
  dados = response.json()

  #-- ValorUSD
  valor_usd = float(dados["USD"])
  valor_formatado_usd = "${:,.3f}".format(valor_usd)
  l_p_usd["text"] = valor_formatado_usd

#valor em real
  valor_real = float(dados["BRL"])
  valor_formatado_BRL = "Em Reais R${:,.3f}".format(valor_real)
  l_p_real["text"] = valor_formatado_BRL

  frame_down.after(1000, info)




# configurando parte superior
imagem = Image.open("./bitimage.png")
image = imagem.resize((20,20), Image.ADAPTIVE)
imagem = ImageTk.PhotoImage(imagem)

l_ico = Label(frame_up, image=imagem, compound=LEFT, bg=co1, relief=FLAT) 
l_ico.place(x=10, y=10)

l_name = Label(frame_up, text="CyptoScope", bg=co1, fg=co0 , relief=FLAT, anchor="center", font=("Arial 30")) 
l_name.place(x=70, y=10)

# configurando parte baixo

l_p_usd = Label(frame_down, text="",bg=fundo, fg=co1 , relief=FLAT, anchor="center", font=("Arial 20")) 
l_p_usd.place(x=90, y=50)

l_p_real = Label(frame_down, text="",bg=fundo, fg=co1 , relief=FLAT, anchor="center", font=("Arial 12")) 
l_p_real.place(x=10, y=130)




info()

janela.mainloop()