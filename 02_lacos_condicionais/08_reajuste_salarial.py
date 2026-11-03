"""
Exercício 08 - Reajuste salarial (Portugol TI)
Até 1412,00 -> 15% | Até 2824,00 -> 12% | Até 4236,00 -> 10%
Até 5648,00 -> 7%  | Acima de 5648,00 -> 5%
reajuste = (salario * percentual) / 100 | novo salário = salario + reajuste
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
print(f"║{'REAJUSTE SALARIAL'.center(LARGURA)}║")
print(f"╚{'═' * LARGURA}╝{RESET}")
print()

salario = float(input(SETA + "Digite o valor do salário (R$): "))

if salario <= 1412.00:
    percentual = 15
elif salario <= 2824.00:
    percentual = 12
elif salario <= 4236.00:
    percentual = 10
elif salario <= 5648.00:
    percentual = 7
else:
    percentual = 5

reajuste = (salario * percentual) / 100
novo_salario = salario + reajuste

print()
linha_1 = f"  Novo salario: R$ {novo_salario:.2f}"
linha_2 = f"  Valor do reajuste: R$ {reajuste:.2f}"
linha_3 = f"  Percentual do aumento: {percentual}%"
print(f"{VERDE}┌{'─' * LARGURA}┐")
print(f"│{NEGRITO}{linha_1.ljust(LARGURA)}{RESET}{VERDE}│")
print(f"│{AMARELO}{linha_2.ljust(LARGURA)}{VERDE}│")
print(f"│{CIANO}{linha_3.ljust(LARGURA)}{VERDE}│")
print(f"└{'─' * LARGURA}┘{RESET}")
