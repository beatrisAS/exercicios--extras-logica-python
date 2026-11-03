"""
Exercício 01 - Área de um círculo
Fórmula: area = PI * raio^2
"""
import os
import math

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
print(f"║{'ÁREA DO CÍRCULO'.center(LARGURA)}║")
print(f"╚{'═' * LARGURA}╝{RESET}")
print()

raio = float(input(SETA + "Digite o raio do círculo: "))

area = math.pi * raio ** 2

print()
linha = f"  A área do círculo é: {area:.2f}"
print(f"{VERDE}┌{'─' * LARGURA}┐")
print(f"│{linha.ljust(LARGURA)}│")
print(f"└{'─' * LARGURA}┘{RESET}")
