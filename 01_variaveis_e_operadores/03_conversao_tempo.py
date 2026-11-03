"""
Exercício 03 - Conversão de segundos para hh:mm:ss
horas = tempo // 3600 | minutos = (tempo % 3600) // 60 | segundos = tempo % 60
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
print(f"║{'CONVERSOR DE TEMPO'.center(LARGURA)}║")
print(f"╚{'═' * LARGURA}╝{RESET}")
print()

tempo = int(input(SETA + "Digite o tempo: "))

horas = tempo // 3600
minutos = (tempo % 3600) // 60
segundos = tempo % 60

print()
linha = f"  Tempo expresso em (hh:mm:ss): {horas}:{minutos}:{segundos}"
print(f"{VERDE}┌{'─' * LARGURA}┐")
print(f"│{linha.ljust(LARGURA)}│")
print(f"└{'─' * LARGURA}┘{RESET}")
