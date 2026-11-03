"""
Exercício 15 - Posições da lista com valores menores ou iguais a 10
Lê 10 números inteiros e mostra índice e valor dos que forem <= 10.
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
print(f"║{'FILTRO DE VALORES ≤ 10'.center(LARGURA)}║")
print(f"╚{'═' * LARGURA}╝{RESET}")
print()

ordinais = ["primeiro", "segundo", "terceiro", "quarto", "quinto",
            "sexto", "sétimo", "oitavo", "nono", "décimo"]

lista = []

for i in range(10):
    numero = int(input(SETA + f"Digite o {ordinais[i]} número inteiro: "))
    lista.append(numero)

print()
print(f"{AMARELO}{NEGRITO}Números menores ou iguais a 10:{RESET}")
print(f"{VERDE}┌{'─' * LARGURA}┐")
encontrados = 0
for i in range(10):
    if lista[i] <= 10:
        linha = f"  lista[{i}] = {lista[i]}"
        print(f"│{linha.ljust(LARGURA)}│")
        encontrados = encontrados + 1
if encontrados == 0:
    print(f"│{'  Nenhum valor encontrado.'.ljust(LARGURA)}│")
print(f"└{'─' * LARGURA}┘{RESET}")
