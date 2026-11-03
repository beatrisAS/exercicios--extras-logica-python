"""
Exercício 09 - O duende Ed e os presentes de Natal
Se o tempo dos dois presentes couber no tempo restante: 'Farei hoje!'
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
print(f"║{'OFICINA DO PAPAI NOEL'.center(LARGURA)}║")
print(f"╚{'═' * LARGURA}╝{RESET}")
print()

tempo_restante = int(input(SETA + "Tempo restante (min): "))
presente_1 = int(input(SETA + "Tempo de fabricação do presente 01 (min): "))
presente_2 = int(input(SETA + "Tempo de fabricação do presente 02 (min): "))

tempo_necessario = presente_1 + presente_2

print()
print(f"{CINZA}  Necessário: {tempo_necessario} min  |  Disponível: {tempo_restante} min{RESET}")

if tempo_necessario <= tempo_restante:
    print(f"{VERDE}{NEGRITO}🎁 Farei hoje!{RESET}")
else:
    print(f"{AMARELO}{NEGRITO}😴 Deixa para amanhã!{RESET}")
