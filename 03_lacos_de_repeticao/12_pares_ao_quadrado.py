"""
Exercício 12 - Números pares de 1 até N elevados ao quadrado
N deve estar entre 5 e 2000.
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
print(f"║{'PARES AO QUADRADO'.center(LARGURA)}║")
print(f"╚{'═' * LARGURA}╝{RESET}")
print()

n = int(input(SETA + "Digite o primeiro número inteiro: "))

while n < 5 or n > 2000:
    print(ERRO + "Valor inválido! Digite um número entre 5 e 2000.")
    n = int(input(SETA + "Digite o primeiro número inteiro: "))

print()
for i in range(1, n + 1):
    if i % 2 == 0:
        print(f"  {AMARELO}{i}^2{RESET} = {VERDE}{NEGRITO}{i ** 2}{RESET}")
