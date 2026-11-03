"""
Exercício 16 - Inversão de uma lista de 20 posições por trocas
Troca 1º<->20º, 2º<->19º, ... até 10º<->11º (10 trocas).
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
print(f"║{'INVERSOR DE LISTA'.center(LARGURA)}║")
print(f"╚{'═' * LARGURA}╝{RESET}")
print()

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
         11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(f"{AMARELO}{NEGRITO}Lista original:{RESET}")
print(f"{CINZA}{lista}{RESET}")

for i in range(10):
    auxiliar = lista[i]
    lista[i] = lista[19 - i]
    lista[19 - i] = auxiliar

print()
print(f"{VERDE}{NEGRITO}⇅ Lista modificada:{RESET}")
print(f"{VERDE}{lista}{RESET}")
