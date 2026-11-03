"""
Exercício 06 - Classificação de triângulos
Condição de existência: cada lado deve ser menor que a soma dos outros dois.
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
print(f"║{'CLASSIFICADOR DE TRIÂNGULOS'.center(LARGURA)}║")
print(f"╚{'═' * LARGURA}╝{RESET}")
print()

a = float(input(SETA + "Digite o tamanho do lado A: "))
b = float(input(SETA + "Digite o tamanho do lado B: "))
c = float(input(SETA + "Digite o tamanho do lado C: "))

if a >= b + c or b >= a + c or c >= a + b:
    mensagem = "NÃO FORMA TRIÂNGULO"
    cor = VERMELHO
elif a == b and b == c:
    mensagem = "TRIÂNGULO EQUILÁTERO"
    cor = VERDE
elif a == b or a == c or b == c:
    mensagem = "TRIÂNGULO ISÓSCELES"
    cor = AMARELO
else:
    mensagem = "TRIÂNGULO ESCALENO"
    cor = CIANO

print()
print(f"{cor}┌{'─' * LARGURA}┐")
print(f"│{NEGRITO}{mensagem.center(LARGURA)}{RESET}{cor}│")
print(f"└{'─' * LARGURA}┘{RESET}")
