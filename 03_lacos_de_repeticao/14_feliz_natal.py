"""
Exercício 14 - Feliz Nataaaal!
O índice de felicidade I (1 a 100) define quantos 'a' aparecem em 'Natal'.
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
print(f"║{'ÍNDICE DE FELICIDADE NATALINA'.center(LARGURA)}║")
print(f"╚{'═' * LARGURA}╝{RESET}")
print()

indice = int(input(SETA + "Digite o primeiro número inteiro: "))

while indice < 1 or indice > 100:
    print(ERRO + "Valor inválido! Digite um número entre 1 e 100.")
    indice = int(input(SETA + "Digite o primeiro número inteiro: "))

letras_a = ""
for i in range(indice):
    letras_a = letras_a + "a"

print()
print(f"{VERMELHO}{NEGRITO}🎄 Feliz Nat{VERDE}{letras_a}{VERMELHO}l!{RESET} ❄️")
