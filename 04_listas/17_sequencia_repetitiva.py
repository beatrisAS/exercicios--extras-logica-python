"""
Exercício 17 - Lista de 100 posições com sequência repetitiva de 0 até T-1
T deve estar entre 2 e 50. Valor da posição i = i % T.
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
print(f"║{'SEQUÊNCIA REPETITIVA'.center(LARGURA)}║")
print(f"╚{'═' * LARGURA}╝{RESET}")
print()

t = int(input(SETA + "Digite um número inteiro entre 2 e 50: "))

while t < 2 or t > 50:
    print(ERRO + "Valor inválido! Digite um número entre 2 e 50.")
    t = int(input(SETA + "Digite um número inteiro entre 2 e 50: "))

lista = []
for i in range(100):
    lista.append(i % t)

print()
for i in range(100):
    print(f"  {CINZA}N[{i}]{RESET} = {CIANO}{NEGRITO}{lista[i]}{RESET}")
