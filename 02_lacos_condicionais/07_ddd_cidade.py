"""
Exercício 07 - Consulta de cidade pelo DDD
Tabela: 11 São Paulo | 21 Rio de Janeiro | 27 Vitória | 31 Belo Horizonte
"""
import os

os.system("")  # habilita as cores ANSI no terminal do Windows

# ---------- Paleta de cores (códigos ANSI) ----------
RESET = "\033[0m"
NEGRITO = "\033[1m"
CIANO = "\033[96m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
VERMELHO = "\033[91m"
ROXO = "\033[95m"
CINZA = "\033[90m"

LARGURA = 54
SETA = f"{CIANO}{NEGRITO}➤{RESET} "
ERRO = f"{VERMELHO}✖{RESET} "

print(f"{ROXO}{NEGRITO}╔{'═' * LARGURA}╗")
print(f"║{'CONSULTA DE DDD'.center(LARGURA)}║")
print(f"╚{'═' * LARGURA}╝{RESET}")
print()

ddd = int(input(SETA + "Digite um DDD: "))

if ddd == 11:
    mensagem = f"O DDD {ddd} pertence à cidade de São Paulo"
    cor = VERDE
elif ddd == 21:
    mensagem = f"O DDD {ddd} pertence à cidade de Rio de Janeiro"
    cor = VERDE
elif ddd == 27:
    mensagem = f"O DDD {ddd} pertence à cidade de Vitória"
    cor = VERDE
elif ddd == 31:
    mensagem = f"O DDD {ddd} pertence à cidade de Belo Horizonte"
    cor = VERDE
else:
    mensagem = "DDD não encontrado!"
    cor = VERMELHO

print()
print(f"{cor}┌{'─' * LARGURA}┐")
print(f"│{mensagem.center(LARGURA)}│")
print(f"└{'─' * LARGURA}┘{RESET}")
