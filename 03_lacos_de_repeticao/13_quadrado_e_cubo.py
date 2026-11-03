"""
Exercício 13 - Tabela de números, quadrados e cubos de 1 até N
N deve estar entre 1 e 1000.
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
print(f"║{'QUADRADOS E CUBOS'.center(LARGURA)}║")
print(f"╚{'═' * LARGURA}╝{RESET}")
print()

n = int(input(SETA + "Digite o primeiro número inteiro: "))

while n < 1 or n > 1000:
    print(ERRO + "Valor inválido! Digite um número entre 1 e 1000.")
    n = int(input(SETA + "Digite o primeiro número inteiro: "))

print()
print(f"{ROXO}┌{'─' * 10}┬{'─' * 14}┬{'─' * 16}┐")
print(f"│{NEGRITO}{'Número'.center(10)}{RESET}{ROXO}│{NEGRITO}{'Quadrado'.center(14)}{RESET}{ROXO}│{NEGRITO}{'Cubo'.center(16)}{RESET}{ROXO}│")
print(f"├{'─' * 10}┼{'─' * 14}┼{'─' * 16}┤{RESET}")
for i in range(1, n + 1):
    print(f"{ROXO}│{CIANO}{str(i).center(10)}{ROXO}│{AMARELO}{str(i ** 2).center(14)}{ROXO}│{VERDE}{str(i ** 3).center(16)}{ROXO}│")
print(f"└{'─' * 10}┴{'─' * 14}┴{'─' * 16}┘{RESET}")
