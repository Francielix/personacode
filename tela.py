import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
import os

from docs import perguntas
from docs import resultados

# configurações da tela
ctk.set_appearance_mode("system")
janela = ctk.CTk()
janela.title("PersonaCode")
janela.state("zoomed")
janela.resizable(True, True)

estado = {
    "nome": "",
    "idade": 0
}

# def para limpar a tela
def limpar_tela():
    for widget in janela.winfo_children():
        widget.destroy()

def azul_topo():
    frame_1 = ctk.CTkFrame(janela, width=1920, height=180, fg_color="#00193A", bg_color="#00193A")
    frame_1.place(x=0, y=0)
    return frame_1

# -----------Adicionar Logo-----------------
caminho_da_imagem = os.path.join(os.path.dirname(__file__), "interface", "logo2.png")

def azul_topo_logo():
    frame_1 = azul_topo()
    logo = ctk.CTkImage(Image.open(caminho_da_imagem), size=(450, 225))
    label_logo = ctk.CTkLabel(frame_1, image=logo, text="", fg_color="transparent")
    label_logo.image = logo
    label_logo.place(relx=0.4, rely=0.5, anchor="center")
