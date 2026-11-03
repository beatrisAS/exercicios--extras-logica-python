"""
Exercício 05 - Ordenação de três números inteiros
Exibe: sequência original, ordem crescente e ordem decrescente.
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
print(f"║{'ORDENADOR DE NÚMEROS'.center(LARGURA)}║")
print(f"╚{'═' * LARGURA}╝{RESET}")
print()

a = int(input(SETA + "Digite o primeiro número inteiro: "))
b = int(input(SETA + "Digite o segundo número inteiro: "))
c = int(input(SETA + "Digite o terceiro número inteiro: "))

# Descobre o menor, o do meio e o maior valor usando apenas condicionais
if a <= b and a <= c:
    menor = a
    if b <= c:
        meio = b
        maior = c
    else:
        meio = c
        maior = b
elif b <= a and b <= c:
    menor = b
    if a <= c:
        meio = a
        maior = c
    else:
        meio = c
        maior = a
else:
    menor = c
    if a <= b:
        meio = a
        maior = b
    else:
        meio = b
        maior = a

print()
linha_1 = f"  Sequência original: {a} {b} {c}"
linha_2 = f"  ▲ Ordem crescente: {menor} {meio} {maior}"
linha_3 = f"  ▼ Ordem decrescente: {maior} {meio} {menor}"
print(f"{VERDE}┌{'─' * LARGURA}┐")
print(f"│{CINZA}{linha_1.ljust(LARGURA)}{VERDE}│")
print(f"│{CIANO}{linha_2.ljust(LARGURA)}{VERDE}│")
print(f"│{AMARELO}{linha_3.ljust(LARGURA)}{VERDE}│")
print(f"└{'─' * LARGURA}┘{RESET}")
