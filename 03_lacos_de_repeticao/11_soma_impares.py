"""
Exercício 11 - Soma dos números ímpares entre X e Y (extremos não incluídos)
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
print(f"║{'SOMA DOS ÍMPARES'.center(LARGURA)}║")
print(f"╚{'═' * LARGURA}╝{RESET}")
print()

x = int(input(SETA + "Digite o primeiro número inteiro: "))
y = int(input(SETA + "Digite o segundo número inteiro: "))

# Garante que o laço sempre percorra do menor para o maior
if x < y:
    inicio = x
    fim = y
else:
    inicio = y
    fim = x

soma = 0
for i in range(inicio + 1, fim):
    if i % 2 != 0:
        soma = soma + i

print()
linha = f"  A Soma de todos os números ímpares é {soma}"
print(f"{VERDE}┌{'─' * LARGURA}┐")
print(f"│{linha.ljust(LARGURA)}│")
print(f"└{'─' * LARGURA}┘{RESET}")
