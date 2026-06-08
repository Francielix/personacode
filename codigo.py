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

def tela_nome():
    limpar_tela()
    azul_topo_logo()
    enunciado = ctk.CTkLabel(janela, text="Como gostaria de ser chamado(a)?", font=("Arial", 50, "bold"), bg_color="transparent")
    enunciado.place(relx=0.05, rely=0.2)
    sub_enunciado = ctk.CTkLabel(janela, text="Conte-nos um pouco sobre você.", font=("Arial", 40), bg_color="transparent", text_color="#3D3D3D")
    sub_enunciado.place(relx=0.05, rely=0.28)
    nome = ctk.CTkLabel(janela, text="Nome:", font=("Arial", 50, "bold"), bg_color="transparent")
    nome.place(relx=0.05, rely=0.40)
    entry = ctk.CTkEntry(janela, width=800, height=80, placeholder_text="Digite seu Nome", font=("Arial", 25), bg_color="transparent")
    entry.place(relx=0.05, rely=0.47)
    botao_voltar = ctk.CTkButton(janela, width=820, height=120, text="Voltar", font=("Arial", 30, "bold"), fg_color="transparent", corner_radius=30, command=tela_inicio, border_width=2, border_color="#000000", text_color="#000000", hover_color="#EE7733")
    botao_voltar.place(relx=0.05, rely=0.85)
    botao_continuar = ctk.CTkButton(janela, width=820, height=120, text="Continuar", font=("Arial", 30, "bold"), fg_color="#3071FF", corner_radius=30, border_width=2, border_color="#3071FF", command=tela_instrucao)
    botao_continuar.place(relx=0.52, rely=0.85)

def tela_instrucao():
    limpar_tela()
    azul_topo_logo()
    enunciado_inst = ctk.CTkLabel(janela, text="Instruções", font=("Arial", 50, "bold"), bg_color="transparent")
    enunciado_inst.place(relx=0.05, rely=0.2)
    sub_enunciado_inst = ctk.CTkLabel(janela, text="Leia com atenção antes de continuar.", font=("Arial", 40), bg_color="transparent", text_color="#3D3D3D")
    sub_enunciado_inst.place(relx=0.05, rely=0.28)

    #Instrução 
    card1 = ctk.CTkFrame(janela, width=820, height=150, fg_color="white", border_width=3, border_color="#000000", corner_radius=10)
    card1.place(relx=0.05, rely=0.40)
    ctk.CTkLabel(card1, text="Não há respostas certas ou erradas", font=("Arial", 25, "bold"), text_color="#000000", fg_color="transparent").place(x=20, y=25)
    ctk.CTkLabel(card1, text="O importante é a sua opinião sincera.", font=("Arial", 22), text_color="#555555", fg_color="transparent").place(x=20, y=55)

    #Instrução 2
    card2 = ctk.CTkFrame(janela, width=820, height=150, fg_color="white", border_width=3, border_color="#000000", corner_radius=10)
    card2.place(relx=0.52, rely=0.40)
    ctk.CTkLabel(card2, text="Leva cerca de 10 minutos", font=("Arial", 25, "bold"), text_color="#000000", fg_color="transparent").place(x=20, y=15)
    ctk.CTkLabel(card2, text="Não pense muito. Seja você mesmo(a).", font=("Arial", 22), text_color="#555555", fg_color="transparent").place(x=20, y=55)

    #Instrução 3
    card3 = ctk.CTkFrame(janela, width=820, height=150, fg_color="white", border_width=3, border_color="#000000", corner_radius=10)
    card3.place(relx = 0.05, rely = 0.58)
    ctk.CTkLabel(card3, text="Responda de forma espontânea", font=("Arial", 25, "bold"), text_color="#000000", fg_color="transparent").place(x=20, y=15)
    ctk.CTkLabel(card3, text="Não pense muito. Seja você mesmo(a).", font=("Arial", 22), text_color="#555555", fg_color="transparent").place(x=20, y=55)

    #Instrução 4
    card4 = ctk.CTkFrame(janela, width=820, height=150, fg_color="white", border_width=3, border_color="#000000", corner_radius=10)
    card4.place(relx=0.52, rely=0.58)
    ctk.CTkLabel(card4, text="Evite pedir ajuda de outras pessoas", font=("Arial", 25, "bold"), text_color="#000000", fg_color="transparent").place(x=20, y=15)
    ctk.CTkLabel(card4, text="O resultado deve refletir apenas você..", font=("Arial", 22), text_color="#555555", fg_color="transparent").place(x=20, y=55)
    
    botao_voltar = ctk.CTkButton(janela, width=820, height=120, text="Voltar", font=("Arial", 30, "bold"), fg_color="transparent", corner_radius=30, command=tela_nome, border_width=2, border_color="#000000", text_color="#000000", hover_color="#EE7733")
    botao_voltar.place(relx=0.05, rely=0.85)
    botao_continuar = ctk.CTkButton(janela, width=820, height=120, text="Continuar", font=("Arial", 30, "bold"), fg_color="#3071FF", corner_radius=30, border_width=2, border_color="#3071FF", command=tela_instrucao)
    botao_continuar.place(relx=0.52, rely=0.85)

tela_inicio()
janela.mainloop()# Abrir a janela
