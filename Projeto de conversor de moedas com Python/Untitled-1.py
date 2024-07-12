# janela -> 500X500
# Título -  Conversor de moedas
# Campos de selecionar moedas de origem e destino.
#botão de converter.

import customtkinter

#criar a janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry('500x500')

#criar os botões,textos e outros elementos.
titulo = customtkinter.CTkLabel(janela, text = "Conversor de moedas")
texto_modo_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem")
texto_modo_destino = customtkinter.CTkLabel(janela, text = "Selecione o mode de destino")

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values=["USD","BRL","EUR","BTC"])
campo_moeda_destino = customtkinter.CTkOptionMenu(janela, values=["USD","BRL","EUR","BTC"])

def converter_moeda():
    print("Converter moeda")

botao_converter = customtkinter.CTkButton(janela, text = "Converter", command=converter_moeda)

                                

lista_moedas = customtkinter.CTkScrollableFrame(janela)
moeda1 = customtkinter.CTkLabel(lista_moedas, text="USD: Dólar americano")
moeda2 = customtkinter.CTkLabel(lista_moedas, text="BRL: Real brasileiro")
moeda3 = customtkinter.CTkLabel(lista_moedas, text="BTC: Bitcoin")
moeda1.pack()
moeda2.pack()
moeda3.pack()

titulo.pack(padx=10,pady=10)
texto_modo_origem.pack(padx=10,pady=10)
campo_moeda_origem.pack(padx=10,pady=10)
texto_modo_destino.pack(padx=10,pady=10)
campo_moeda_destino.pack(padx=10,pady=10)
botao_converter.pack(padx=10,pady=10)
lista_moedas.pack(padx=10,pady=10)

janela.mainloop()