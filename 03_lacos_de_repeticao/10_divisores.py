"""
Exercício 10 - Divisores positivos de um número inteiro
Um número i é divisor de n quando n % i == 0.
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
print(f"║{'DIVISORES DE UM NÚMERO'.center(LARGURA)}║")
print(f"╚{'═' * LARGURA}╝{RESET}")
print()

numero = int(input(SETA + "Digite um número inteiro: "))

if numero <= 0:
    print(ERRO + "Digite um número inteiro positivo!")
else:
    print()
    print(f"{AMARELO}{NEGRITO}Os divisores positivos do número {numero} são:{RESET}")
    print()
    quantidade = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(f"  {VERDE}◆{RESET} {i}")
            quantidade = quantidade + 1
    print()
    print(f"{CINZA}  Total: {quantidade} divisor(es){RESET}")
