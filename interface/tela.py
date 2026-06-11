import customtkinter as ctk
from PIL import Image
import tkinter as tk 
from tkinter import messagebox
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from docs.perguntas import PERGUNTAS
from docs.resultados import RESULTADOS

#configurações da tela
ctk.set_appearance_mode("system")
janela = ctk.CTk()
janela.title("PersonaCode")
janela.resizable(True, True)

caminho_da_imagem = os.path.join(os.path.dirname(__file__), "logo2.png")
estado = {
    "nome": "",
    "idade": 0
}

# Zoom na tela

zoom = 1.0
tela_atual = None
 
def f(tamanho: int):
    #Retorna o tamanho de fonte escalado pelo zoom atual
    return max(8, round(tamanho * zoom))
 
def w(tamanho: int):
    #Retorna largura/altura de widget escalada pelo zoom atual
    return max(10, round(tamanho * zoom))
 
def logo_size():
    return (round(450 * zoom), round(225 * zoom))
 
def _atualizar_zoom(novo_zoom: float):
    global zoom
    zoom = round(novo_zoom, 1)
    if tela_atual:
        tela_atual()
 
def aumentar_zoom():
    if zoom < 2.0:
        _atualizar_zoom(zoom + 0.1)
 
def diminuir_zoom():
    if zoom > 0.6:
        _atualizar_zoom(zoom - 0.1)

# ADICIONAR SCROLL
canvas_scroll = None
frame_conteudo = None

# Remove todos os widgets da janela, incluindo o canvas de scroll
def limpar_tela() -> None:
    for widget in janela.winfo_children():
        widget.destroy()

 # Cria um canvas com scrollbar vertical ocupando a janela inteira e retorna o frame interno onde os widgets devem ser colocados
def criar_area_scroll() -> ctk.CTkFrame:
    global canvas_scroll, frame_conteudo
 
    canvas_scroll = tk.Canvas(janela, highlightthickness=0, bg=janela.cget("bg"))
    scrollbar = ctk.CTkScrollbar(janela, orientation="vertical",
                                  command=canvas_scroll.yview)
 
    canvas_scroll.configure(yscrollcommand=scrollbar.set)
 
    scrollbar.pack(side="right", fill="y")
    canvas_scroll.pack(side="left", fill="both", expand=True)
 
    frame_conteudo = ctk.CTkFrame(canvas_scroll, fg_color="transparent")
    janela_canvas_id = canvas_scroll.create_window(
        (0, 0), window=frame_conteudo, anchor="nw"
    )
 
    def _on_frame_resize(event):
        canvas_scroll.configure(scrollregion=canvas_scroll.bbox("all"))
 
    def _on_canvas_resize(event):
        canvas_scroll.itemconfig(janela_canvas_id, width=event.width)
 
    def _on_mousewheel(event):
        canvas_scroll.yview_scroll(int(-1 * (event.delta / 120)), "units")
 
    frame_conteudo.bind("<Configure>", _on_frame_resize)
    canvas_scroll.bind("<Configure>", _on_canvas_resize)
    canvas_scroll.bind_all("<MouseWheel>", _on_mousewheel)
    
    return frame_conteudo

def barra_zoom(pai) -> None:                                                                #Botões +/− com visual arredondado, fixos no topo direito do frame de conteúdo.
    frame_zoom = ctk.CTkFrame(
        pai,
        fg_color="#1C1C2E",
        corner_radius=0,
        border_width=0,
    )
    # Posicionado com place relativo ao frame_conteudo
    frame_zoom.place(relx=1.0, rely=0.0, anchor="ne", x=-12, y=8)
    frame_zoom.lift()
 
    ctk.CTkButton(
        frame_zoom,
        text="−",
        width=44, height=36,
        font=("Arial", 18, "bold"),
        fg_color="transparent",
        hover_color="#3071FF",
        text_color="white",
        corner_radius=20,
        command=diminuir_zoom
    ).pack(side="left", padx=(6, 2), pady=4)
 
    ctk.CTkLabel(
        frame_zoom,
        text=f"{int(zoom * 100)}%",
        font=("Arial", 13),
        text_color="#AAAAAA",
        fg_color="transparent",
        width=40
    ).pack(side="left", pady=4)
 
    ctk.CTkButton(
        frame_zoom,
        text="+",
        width=44, height=36,
        font=("Arial", 18, "bold"),
        fg_color="transparent",
        hover_color="#3071FF",
        text_color="white",
        corner_radius=20,
        command=aumentar_zoom
    ).pack(side="left", padx=(2, 6), pady=4)

#def para limpar a tela
def limpar_tela():
    for widget in janela.winfo_children():
        widget.destroy()

def azul_topo_logo(pai):
    # Cria o cabeçalho azul com logo dentro do frame pai
    frame_topo = ctk.CTkFrame(pai, height=w(180), fg_color="#00193A",
                               corner_radius=0)
    frame_topo.pack(fill="x", side="top")
    frame_topo.pack_propagate(False)
 
    logo = ctk.CTkImage(Image.open(caminho_da_imagem), size=logo_size())
    label_logo = ctk.CTkLabel(frame_topo, image=logo, text="",
                               fg_color="transparent")
    label_logo.image = logo
    label_logo.place(relx=0.5, rely=0.5, anchor="center")

def corpo(pai) -> ctk.CTkFrame:
    """Retorna um frame de conteúdo com padding lateral padrão."""
    frame = ctk.CTkFrame(pai, fg_color="transparent")
    frame.pack(fill="both", expand=True, padx=60, pady=30)
    return frame
    
def tela_inicio():
    global tela_atual
    tela_atual = tela_inicio
    limpar_tela()
    pai = criar_area_scroll()
    azul_topo_logo(pai)
    barra_zoom(pai)
    c = corpo(pai)
 
    ctk.CTkLabel(
        c,
        text="Bem-vindo(a) ao PersonaCode!",
        font=("Poppins", f(50), "bold"),
    ).pack(anchor="center", pady=(20, 10))
 
    ctk.CTkLabel(
        c,
        text=(
            "Antes de começar, vamos te apresentar a base deste teste.\n"
            "O PersonaCode tem como base a Tríade do Tempo de Christian Barbosa — "
            "metodologia que revela como cada pessoa distribui seu tempo entre o urgente, "
            "o importante e o circunstancial. Criada para o mundo corporativo, ela ganha "
            "aqui uma nova dimensão: adaptada para diferentes fases da vida, torna-se um "
            "espelho de quem você é — e um caminho para quem você quer ser."
        ),
        font=("Segoe UI", f(28), "bold"),
        anchor="center",
        justify="center",
        fg_color="transparent", 
        wraplength=1100
    ).pack(anchor="center", pady=(10, 30))

 
    ctk.CTkButton(
        c,
        width=w(200), height=w(80),
        text="COMEÇAR",
        font=("Poppins", f(28), "bold"),
        fg_color="#3071FF",
        corner_radius=30,
        command=tela_nome
    ).pack(anchor="center", pady=20)

def tela_nome():
    global tela_atual
    tela_atual = tela_nome
    limpar_tela()
    pai = criar_area_scroll()
    azul_topo_logo(pai)
    barra_zoom(pai)
    c = corpo(pai)
 
    def botao_continuar():
        nome = entry.get().strip().capitalize()
        idade = entry_idade.get()
        nome = entry.get().strip().capitalize()
        idade = entry_idade.get()
        if not nome:
            messagebox.showwarning("ATENÇÃO!", "Por favor, informe como deseja ser chamado(a).")
            return
        if not idade.isdigit() or not (5 <= int(idade) <= 200):
            messagebox.showwarning("ATENÇÃO!", "Por favor, informe uma idade válida.")
            return
            
        estado["nome"] = nome
        estado["idade"] = int(idade)
        tela_instrucao()
 
    ctk.CTkLabel(c, text="Como gostaria de ser chamado(a)?",
                 font=("Arial", f(36), "bold")).pack(anchor="center", pady=(20, 4))
    ctk.CTkLabel(c, text="Conte-nos um pouco sobre você.",
                 font=("Arial", f(26)), text_color="#3D3D3D").pack(anchor="center", pady=(0, 20))
 
    ctk.CTkLabel(c, text="Nome:", font=("Arial", f(32), "bold")).pack(anchor="center")
    entry = ctk.CTkEntry(c, width=w(700), height=w(70),
                         placeholder_text="Digite seu Nome",
                         font=("Arial", f(22)))
    entry.pack(anchor="center", pady=(4, 20))
 
    ctk.CTkLabel(c, text="Idade:", font=("Arial", f(32), "bold")).pack(anchor="center")
    entry_idade = ctk.CTkEntry(c, width=w(700), height=w(70),
                               placeholder_text="Digite sua idade",
                               font=("Arial", f(22)))
    entry_idade.pack(anchor="center", pady=(4, 30))
 
    frame_botoes = ctk.CTkFrame(c, fg_color="transparent")
    frame_botoes.pack(anchor="center", pady=10)
 
    ctk.CTkButton(
        frame_botoes, width=w(200), height=w(80),
        text="Voltar", font=("Arial", f(26), "bold"),
        fg_color="transparent", corner_radius=30,
        border_width=2, border_color="#000000",
        text_color="#000000", hover_color="#EE7733",
        command=tela_inicio
    ).pack(side="left", padx=(0, 40))
 
    ctk.CTkButton(
        frame_botoes, width=w(200), height=w(80),
        text="Continuar", font=("Arial", f(26), "bold"),
        fg_color="#3071FF", corner_radius=30,
        command=botao_continuar
    ).pack(side="left", padx=(0, 60))

def tela_instrucao():
    global tela_atual
    tela_atual = tela_instrucao
    limpar_tela()
    pai = criar_area_scroll()
    azul_topo_logo(pai)
    barra_zoom(pai)
    c = corpo(pai)
 
    ctk.CTkLabel(c, text="Instruções",
                 font=("Arial", f(50), "bold")).pack(anchor="w", pady=(20, 4))
    ctk.CTkLabel(c, text="Leia com atenção antes de continuar.",
                 font=("Arial", f(32)), text_color="#3D3D3D").pack(anchor="w", pady=(0, 20))
 
    cards_dados = [
        ("Não há respostas certas ou erradas", "O importante é a sua opinião sincera."),
        ("Leva cerca de 10 minutos",           "Não pense muito. Seja você mesmo(a)."),
        ("Responda de forma espontânea",       "Aqui, intuição vale mais que perfeição."),
        ("Evite pedir ajuda de outras pessoas","O resultado deve refletir apenas você."),
    ]
 
    # Grade 2×2 de cards
    for linha in range(0, 4, 2):
        row_frame = ctk.CTkFrame(c, fg_color="transparent")
        row_frame.pack(fill="x", pady=8)
        for titulo_card, sub_card in cards_dados[linha:linha+2]:
            card = ctk.CTkFrame(row_frame, width=w(560), height=w(120),
                                fg_color="white", border_width=3,
                                border_color="#000000", corner_radius=10)
            card.pack(side="left", padx=(0, 20))
            card.pack_propagate(False)
            ctk.CTkLabel(card, text=titulo_card, font=("Arial", f(22), "bold"),
                         text_color="#000000", fg_color="transparent").place(x=20, y=18)
            ctk.CTkLabel(card, text=sub_card, font=("Arial", f(19)),
                         text_color="#555555", fg_color="transparent").place(x=20, y=52)
 
    frame_botoes = ctk.CTkFrame(c, fg_color="transparent")
    frame_botoes.pack(anchor="w", pady=30)
 
    ctk.CTkButton(
        frame_botoes, width=w(200), height=w(80),
        text="Voltar", font=("Arial", f(26), "bold"),
        fg_color="transparent", corner_radius=30,
        border_width=2, border_color="#000000",
        text_color="#000000", hover_color="#EE7733",
        command=tela_nome
    ).pack(side="left", padx=(0, 20))
 
    ctk.CTkButton(
        frame_botoes, width=w(200), height=w(80),
        text="Continuar", font=("Arial", f(26), "bold"),
        fg_color="#3071FF", corner_radius=30,
        command=tela_perguntas
    ).pack(side="left")
    
def get_faixa_etaria():
    idade = estado["idade"]
    if 5 <= idade <= 12:
        return "crianca"
    elif 13 <= idade <= 17:
        return "adolescente"
    elif 18 <= idade <= 59:
        return "jovem/adulto"
    else:
        return "idoso"
        
# determina o indici de 0 - 4 para apresentar o resultado final, com base na média das respostas
def calcular_resultado(respostas): # recebe a lista de respostas (pontuações)
    media = sum(respostas) / len(respostas) # calcula a média das respostas
    #define os intervalos de media para cada resultado
    if media >= 4.5:
        return 0
    elif media >= 3.5:
        return 1
    elif media >= 2.5:
        return 2
    elif media >= 1.5:
        return 3
    else:
        return 4

# tela das PERGUNTAS 

def tela_perguntas():
    faixa = get_faixa_etaria()        # Vê a idade da pessoa
    perguntas = PERGUNTAS[faixa]      # seleciona as questões com base na idade
    total = len(perguntas)            #total de perguntas
    respostas = []                    # armazena as respostas.
 
    def exibir_pergunta(indice: int): # vai mostrar questões específicas com base no índice
        global tela_atual
        tela_atual = lambda: exibir_pergunta(indice)
        limpar_tela()
        pai = criar_area_scroll() # Cria uma área de rolagem cpro conteúdo
        azul_topo_logo(pai)
        barra_zoom(pai)
        c = corpo(pai)
 
        pergunta = perguntas[indice]
 
        # Contador e barra de progresso
        ctk.CTkLabel(                                                        #contador
            c,
            text=f"Pergunta {indice + 1} de {total}",
            font=("Arial", f(22)),
            text_color="#888888"
        ).pack(anchor="w", pady=(10, 4))
 
        barra = ctk.CTkProgressBar(c, width=w(900), height=12,                # barrinha de progresso
                                   corner_radius=6, fg_color="#DDDDDD",
                                   progress_color="#3071FF")
        barra.set((indice + 1) / total)
        barra.pack(anchor="w", pady=(0, 16))
 
        ctk.CTkLabel(
            c,
            text=pergunta["texto"],            #Basicamente ajuste de posição, fonte, tamanho da letra, etc
            font=("Arial", f(28), "bold"),
            wraplength=1100,
            justify="left"
        ).pack(anchor="w", pady=(0, 20))
 
        # Opções de resposta
        for i, opcao in enumerate(pergunta["opcoes"]):     #percorre todas as opções da pergunta atual
            pontuacao = 5 - i
 
            def ao_clicar(pts=pontuacao, idx=indice):     # faz o registro da resposta e avança
                respostas.append(pts)
                if idx + 1 < total:
                    exibir_pergunta(idx + 1)
                else:
                    tela_resultado(faixa, calcular_resultado(respostas))
 
            ctk.CTkButton(                                # botão pra cada opção de repsosta
                c,
                width=w(1000), height=w(52),              
                text=opcao,
                font=("Arial", f(20)),
                fg_color="white",
                text_color="#000000",
                hover_color="#D6E4FF",
                border_width=2,
                border_color="#AAAAAA",
                corner_radius=10,
                anchor="w",
                command=ao_clicar
            ).pack(anchor="w", pady=4)
 
        def voltar():                            # volta a pergunta anterior, se for a primeira pergunta volta pra tela de instrução
            if indice > 0:
                respostas.pop()
                exibir_pergunta(indice - 1)
            else:
                tela_instrucao()
 
        ctk.CTkButton(                            # botão pra voltar
            c,
            width=w(160), height=w(60),
            text="Voltar",
            font=("Arial", f(22), "bold"),
            fg_color="transparent",
            corner_radius=30,
            border_width=2,
            border_color="#000000",
            text_color="#000000",
            hover_color="#EE7733",
            command=voltar                        
        ).pack(anchor="w", pady=20)
 
    exibir_pergunta(0)
#-------------------------------------
#funçao da tela de resultados
#-------------------------------------

def tela_resultado(faixa, indice_resultado):  #funçao da tela de resultados
    global tela_atual
    tela_atual = lambda: tela_resultado(faixa, indice_resultado)
    limpar_tela()
    pai = criar_area_scroll()
    azul_topo_logo(pai)
    barra_zoom(pai)
    c = corpo(pai)

    # Faixa de exibição para RESULTADOS usa chave diferente de PERGUNTAS
    faixa_resultado = faixa
    if faixa == "crianca":
        faixa_resultado = "criança"
    elif faixa == "jovem/adulto":
        faixa_resultado = "jovem/adulto"

    resultado = RESULTADOS[faixa_resultado][indice_resultado]

    # resultado é uma tupla: (TÍTULO, descrição, complemento, "DICA", texto_dica)

    # alguns perfis têm 5 elementos, outros 4 — tratamos os dois casos
    if len(resultado) == 5:
        titulo, descricao, complemento, _, dica = resultado
    else:
        titulo, descricao, _, dica = resultado
        complemento = ""

    nome = estado["nome"]  #variavel do estado

    ctk.CTkLabel( # nome do usuario do app
        janela,
        text=f"{nome}, seu perfil é:",
        font=("Arial", 32),
        bg_color="transparent",
        text_color="#EB7C24"
    ).place(relx=0.05, rely=0.28)

    ctk.CTkLabel( #titulo 
        janela,
        text=titulo,
        font=("Arial", 46, "bold"),
        bg_color="transparent",
        text_color="#3071FF"
    ).place(relx=0.05, rely=0.34)

    ctk.CTkLabel(  #descriçao
        janela,
        text=descricao,
        font=("Arial", 24),
        bg_color="transparent",
        wraplength=1100,
        justify="left"
    ).place(relx=0.05, rely=0.44)

    if complemento:
        ctk.CTkLabel( #complemento
            janela,
            text=complemento,
            font=("Arial", 22),
            bg_color="transparent",
            text_color="#555555",
            wraplength=1100,
            justify="left"
        ).place(relx=0.05, rely=0.54)

    # Card da dica
    card_dica = ctk.CTkFrame(janela, width=1100, height=130, fg_color="#FFF8DC", border_width=2, border_color="#3071FF", corner_radius=15)
    card_dica.place(relx=0.05, rely=0.58)
    ctk.CTkLabel(card_dica, text="💡 DICA", font=("Arial", 22, "bold"), text_color="#3071FF", fg_color="transparent").place(x=20, y=12)
    ctk.CTkLabel(card_dica, text=dica, font=("Arial", 20), text_color="#333333", fg_color="transparent", wraplength=1060, justify="left").place(x=20, y=48)

    # Botao fazer novamento o app
    ctk.CTkButton(
        janela,
        width=260,
        height=80,
        text="Fazer novamente",
        font=("Arial", 24, "bold"),
        fg_color="#3071FF",
        corner_radius=30,
        command=tela_inicio
    ).place(relx=0.52, rely=0.87)

    ctk.CTkButton(  #botao voltar
        janela,
        width=180,
        height=80,
        text="Sair",
        font=("Arial", 24, "bold"),
        fg_color="transparent",
        corner_radius=30,
        border_width=2,
        border_color="#000000",
        text_color="#000000",
        hover_color="#EE7733",
        command=janela.destroy
    ).place(relx=0.05, rely=0.87)


tela_inicio()
janela.mainloop()# Abrir a janela
