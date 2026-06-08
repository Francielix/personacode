import customtkinter as ctk
from PIL import Image
import os

#configurações da tela
ctk.set_appearance_mode("system") 
janela = ctk.CTk() 
janela.title("PersonaCode") 
janela.geometry("1920x1080")
janela.resizable(True, True)

#def para limpar a tela
def limpar_tela():
    for widget in janela.winfo_children():
        widget.destroy()

def azul_topo():
    frame_1 = ctk.CTkFrame(janela, width=1920, height= 180, fg_color="#00193A", bg_color="#00193A")#faixa azul na tela
    frame_1.place(x=0, y=0)#local da faixa azul
    return frame_1
caminho_da_imagem = os.path.join(os.path.dirname(__file__), "interface", "logo2.png")

def azul_topo_logo():
    frame_1 = azul_topo()  # ← recebe o frame
    logo = ctk.CTkImage(Image.open(caminho_da_imagem), size=(500, 225))
    label_logo = ctk.CTkLabel(frame_1, image=logo, text="", fg_color="transparent")  # ←  faz ficar dentro do frame_1
    label_logo.image = logo  # ← evita a imagem sumir
    label_logo.place(relx=0.5, rely=0.6, anchor="center")

def tela_inicio():
    limpar_tela()
    azul_topo_logo()
    mensagem_b_vindo = ctk.CTkLabel(janela, text="Bem Vindo ao Persona Code!", font=("Poppins",50, "bold" ), bg_color="transparent")
    mensagem_b_vindo.place(relx=0.5, rely=0.25, anchor="center") 
    mensagem_inicial = ctk.CTkLabel(janela, text=(
    "Antes de começar, vamos te apresentar a base deste teste.\n"
    "A Tríade do Tempo é uma metodologia que organiza nossas atividades em três categorias:\n"
    "• Importante — ações que geram impacto no seu futuro\n"
    "• Urgente — demandas que exigem atenção imediata\n"
    "• Circunstancial — atividades que desviam seu foco do essencial.\n"
    "Ao longo do teste, suas respostas irão revelar qual desses padrões predomina no seu comportamento."
    ), font=("Segoe UI", 35, "bold"), fg_color="transparent", justify="left", wraplength=1150)
    mensagem_inicial.place(relx=0.52, rely=0.53, anchor="center")
    botao_comecar = ctk.CTkButton(janela, width=400, height=120, bg_color="transparent", text="COMEÇAR", font=("Poppins", 30,"bold"), fg_color="#3071FF", corner_radius=30, command=tela_nome )
    botao_comecar.place(relx=0.5, rely=0.85, anchor="center")


tela_inicio()
janela.mainloop()# Abrir a janela