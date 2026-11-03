"""
Exercício 04 - Decomposição de um valor em cédulas
Para cada nota: quantidade = valorRestante // valorNota
                valorRestante = valorRestante % valorNota
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
print(f"║{'DECOMPOSIÇÃO EM CÉDULAS'.center(LARGURA)}║")
print(f"╚{'═' * LARGURA}╝{RESET}")
print()

valor = int(float(input(SETA + "Digite um valor em Reais (sem os centavos): ")))

valor_restante = valor

notas_200 = valor_restante // 200
valor_restante = valor_restante % 200

notas_100 = valor_restante // 100
valor_restante = valor_restante % 100

notas_50 = valor_restante // 50
valor_restante = valor_restante % 50

notas_20 = valor_restante // 20
valor_restante = valor_restante % 20

notas_10 = valor_restante // 10
valor_restante = valor_restante % 10

notas_5 = valor_restante // 5
valor_restante = valor_restante % 5

notas_2 = valor_restante // 2
valor_restante = valor_restante % 2

notas_1 = valor_restante // 1

print()
print(f"{AMARELO}{NEGRITO}💵 Para o valor R$ {valor:.2f}".replace(".", ",") + f" utilizaremos:{RESET}")
print(f"{VERDE}┌{'─' * LARGURA}┐")
# Notas utilizadas ficam em verde; notas não utilizadas ficam em cinza
print(f"│{VERDE if notas_200 > 0 else CINZA}{f'  {notas_200} nota(s) de R$ 200,00'.ljust(LARGURA)}{VERDE}│")
print(f"│{VERDE if notas_100 > 0 else CINZA}{f'  {notas_100} nota(s) de R$ 100,00'.ljust(LARGURA)}{VERDE}│")
print(f"│{VERDE if notas_50 > 0 else CINZA}{f'  {notas_50} nota(s) de R$ 50,00'.ljust(LARGURA)}{VERDE}│")
print(f"│{VERDE if notas_20 > 0 else CINZA}{f'  {notas_20} nota(s) de R$ 20,00'.ljust(LARGURA)}{VERDE}│")
print(f"│{VERDE if notas_10 > 0 else CINZA}{f'  {notas_10} nota(s) de R$ 10,00'.ljust(LARGURA)}{VERDE}│")
print(f"│{VERDE if notas_5 > 0 else CINZA}{f'  {notas_5} nota(s) de R$ 5,00'.ljust(LARGURA)}{VERDE}│")
print(f"│{VERDE if notas_2 > 0 else CINZA}{f'  {notas_2} nota(s) de R$ 2,00'.ljust(LARGURA)}{VERDE}│")
print(f"│{VERDE if notas_1 > 0 else CINZA}{f'  {notas_1} nota(s) de R$ 1,00'.ljust(LARGURA)}{VERDE}│")
print(f"└{'─' * LARGURA}┘{RESET}")
