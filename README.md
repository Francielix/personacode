<p align="center">
  <img src="interface/logo2.png" width="420"/>
</p>

# ---------- PersonaCode ----------

> Transformando a Tríade do Tempo em uma ferramenta de desenvolvimento humano contextualizado.

O classificador de perfil do PersonaCode é inteiramente baseado na **Tríade do Tempo de Christian Barbosa** — metodologia criada originalmente para o contexto corporativo adulto. Diante da percepção de que o que é importante é relativo à fase de vida de cada pessoa, o PersonaCode tornou o classificador de perfil acessível e consistente a diferentes faixas etárias, transformando uma ferramenta de diagnóstico em uma **ferramenta de desenvolvimento humano contextualizado**.

-------------------------------------------------------------------------------------------------------------------------------------------

# ---------- Funcionalidades ----------

- 📋 Quiz interativo com perguntas adaptadas por faixa etária
- 🎯 Classificação em 5 perfis baseados na Tríade do Tempo
- 💡 Resultado personalizado com dica de desenvolvimento
- ♿ Interface pensada com foco em acessibilidade e usabilidade (IHC/UX)
- 🖥️ Aplicação desktop com interface gráfica moderna (CustomTkinter)

-------------------------------------------------------------------------------------------------------------------------------------------

# ---------- Fluxograma do projeto ----------

[🔗 Ver fluxograma no Figma](https://www.figma.com/board/c6q1O2t2PPfnbraqI81k63/Untitled?node-id=0-1&t=jzPKI5iRTQi65pPr-1)

-------------------------------------------------------------------------------------------------------------------------------------------

# ---------- Sitemap do projeto ----------

[🔗 Ver sitemap no Figma](https://www.figma.com/board/e511WVHkhReGzajyPpTbLY/Site-Map?node-id=0-1&t=ahM6U177wzQsGpA4-1)

-------------------------------------------------------------------------------------------------------------------------------------------

# ---------- Estrutura do Projeto ----------

```
PersonaCode/
├── docs/
    └── perguntas.py       # Banco de perguntas por faixa etária
    └── resultados.py      # Perfis e descrições do resultado
    └── __init__.py        # Reconhecimento de pasta como Pacote Python
├── interface/
│   └── logo2.png          # Logo da aplicação
    └── tela.py            # Interface gráfica principal
├── README.md              # Documentação e especificações
├── main.py                # Arquivo de execução do programa
└── requirements.txt       # Dependências do projeto 
```

-------------------------------------------------------------------------------------------------------------------------------------------

# ---------- Como executar ----------

**Pré-requisitos:** Python 3.10 ou superior e pip instalado.

```bash
# 1. Clone o repositório
git clone https://github.com/Francielix/personacode.git

# 2. Entre na pasta do projeto
cd PersonaCode

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute a aplicação
python main.py
```

-------------------------------------------------------------------------------------------------------------------------------------------

# ---------- Dependências ----------

| Biblioteca | Versão | Finalidade |

| customtkinter | ≥ 5.2.0 | Interface gráfica moderna |
| Pillow | ≥ 10.0.0 | Carregamento e manipulação de imagens |
| tkinter | Python Standard Library | Criação da interface gráfica |
| os | Python Standard Library | Manipulação de diretórios e arquivos |
| messagebox | tkinter | Exibição de mensagens de alerta e validação |

-------------------------------------------------------------------------------------------------------------------------------------------

# ---------- Perfis identificados ----------

O PersonaCode classifica o usuário em um dos 5 perfis da Tríade do Tempo, adaptado para cada faixa etária:

| Perfil | Descrição resumida |

| 🟢 Importante | Foco no que realmente importa |
| 🔵 Equilibrado | Bom balanceamento entre as esferas |
| 🟡 Circunstancial | Reage ao ambiente e ao contexto |
| 🟠 Urgente | Vive apagando incêndios |
| 🔴 Crítico | Alta sobrecarga e baixo controle |

-------------------------------------------------------------------------------------------------------------------------------------------

# ---------- Equipe ----------
# 👥 Equipe de Desenvolvimento

O PersonaCode foi desenvolvido por uma equipe composta por 8 integrantes, que atuaram de forma colaborativa nas etapas de pesquisa, planejamento, prototipação, desenvolvimento, testes e documentação do sistema.

# ---------- Integrantes e Contribuições ----------

| Integrante                              | Contribuições para o PersonaCode  

| **Franciele Couto Costa Souza**         | Pesquisa sobre a metodologia Tríade do Tempo que fundamenta o PersonaCode, elaboração das perguntas e respostas dos questionários, desenvolvimento do fluxograma do sistema, implementação do recurso de scroll, integração de messagebox para validações, criação e gerenciamento do repositório principal no GitHub e apoio na estruturação geral da aplicação. 

| **Juliano de Carvalho Lacerda**         | Pesquisa e estudo da biblioteca CustomTkinter para auxiliar no desenvolvimento da interface do PersonaCode, elaboração das respostas dos questionários, implementação das respostas no sistema, organização da estrutura do projeto e contribuição na manutenção, correção e aprimoramento do código-fonte da aplicação.                                          

| **Itallo Gustavo Teixeira Gomes Frota** | Desenvolvimento da lógica de cálculo dos resultados do PersonaCode, implementação da funcionalidade de seleção de tema e elaboração do sitemap do projeto.                                                                                                                                                                                                        
| **Klever Santos Baliza**                | Participação na elaboração das perguntas dos questionários do PersonaCode, revisão e correção das perguntas e respostas, integração das respostas ao sistema, correção de erros identificados durante o desenvolvimento, organização da estrutura do projeto e suporte técnico aos demais integrantes da equipe.

| **Yuri Aguiar Junqueira Gomes**         | Desenvolvimento das telas iniciais de boas-vindas, nome e idade do PersonaCode, criação do protótipo interativo no Figma e participação na construção da identidade visual e da logo do projeto.                                                                                                                                                                  
| **Breno Henrique Vieira Silva**         | Desenvolvimento da tela de instruções do PersonaCode, criação do protótipo interativo no Figma e desenvolvimento da logo e dos elementos visuais da identidade do projeto.                                                                                                                                                                                        
| **Guilherme da Silva Roque**            | Desenvolvimento da lógica responsável pela identificação e determinação das faixas etárias dos usuários no PersonaCode, contribuindo para a personalização dos questionários e resultados.                                                                                                                                                                       
| **Tallita Souza dos Santos**            | Implementação da funcionalidade de zoom da interface, contribuindo para a acessibilidade e usabilidade do PersonaCode.                                                                                                                                                                                                                                            

# ---------- Histórico de Desenvolvimento ---------- 

Antes da criação da versão final do repositório, a equipe utilizou um repositório preliminar para estudos, testes e experimentação do código. Esse ambiente inicial foi utilizado para compreender o funcionamento do Git e GitHub, validar ideias, realizar testes de implementação e estruturar as primeiras versões da aplicação.

https://github.com/Francielix/Classificador-de-perfil-pass-

Após a consolidação da arquitetura e das funcionalidades principais, foi criado o repositório oficial do PersonaCode, reunindo a versão organizada e definitiva do projeto para desenvolvimento, documentação e apresentação.

## Metodologia de Trabalho

O desenvolvimento do PersonaCode foi realizado de forma colaborativa utilizando Git e GitHub para controle de versão. As atividades foram distribuídas entre os integrantes de acordo com suas habilidades e áreas de atuação, abrangendo pesquisa, levantamento de requisitos, prototipação, desenvolvimento, acessibilidade, testes, identidade visual e documentação.

A colaboração entre os membros permitiu a construção de uma aplicação focada no autoconhecimento, oferecendo uma experiência personalizada para crianças, adolescentes, adultos e idosos.


-------------------------------------------------------------------------------------------------------------------------------------------

# ---------- Base teórica ----------

- BARBOSA, C. *A Tríade do Tempo*. Editora Sextante, 2008.
- BENYON, D. *Interação Humano-Computador*. Pearson, 2011.
- BARRETO, J. S. et al. *Interface Humano-Computador*. Sagah, 2018.

-------------------------------------------------------------------------------------------------------------------------------------------

# ---------- Contexto acadêmico ----------

Projeto desenvolvido para as UCs de **Interação Humano-Computador e UX (IHC-UX)** e **Algoritmos e Programação**, com aplicação prática de conceitos de UX, acessibilidade e lógica de programação em Python.
