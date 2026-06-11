import customtkinter as ctk
from PIL import Image
import os

from docs import PERGUNTAS
from docs import RESULTADOS

#configurações da tela
ctk.set_appearance_mode("system") 
janela = ctk.CTk()

#Zoom na tela
zoom = 1.0

def _zoom(d):
    global zoom
    zoom = max(0.8, min(1.5, zoom + d))
    ctk.set_widget_scaling(zoom)

frame_zoom = ctk.CTkFrame(toolbar, fg_color="transparent")
frame_zoom.pack(side="right", padx=4)

ctk.CTkButton(frame_zoom, text="−", width=28, command=lambda: _zoom(-.1)).pack(side="left")
ctk.CTkButton(frame_zoom, text="+", width=28, command=lambda: _zoom(+.1)).pack(side="left", padx=(2,0))

janela.bind("<minus>", lambda e: _zoom(-.1))
janela.bind("<equal>", lambda e: _zoom(+.1))
         
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
    
def get_faixa_etaria() -> str:
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

def tela_perguntas() -> None:
    faixa = get_faixa_etaria()        # Vê a idade da pessoa
    perguntas = PERGUNTAS[faixa]      # seleciona as questões com base na idade
    total = len(perguntas)            #total de perguntas
    respostas = []                    # armazena as respostas.
 
    def exibir_pergunta(indice: int) -> None: # vai mostrar questões específicas com base no índice
        global tela_atual
        tela_atual = lambda: exibir_pergunta(indice)
        limpar_tela()
        area = criar_area_scroll() # Cria uma área de rolagem cpro conteúdo
        azul_topo_logo(area)
        barra_zoom(area)
        c = corpo(area)
 
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
    limpar_tela()
    azul_topo_logo()
    barra_zoom()

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
