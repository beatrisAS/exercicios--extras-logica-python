"""
Exercício 02 - Consumo de combustível (rendimento de 12 km/L)
distancia = tempo * velocidade
consumo   = distancia / rendimento
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

RENDIMENTO = 12  # km por litro

print(f"{ROXO}{NEGRITO}╔{'═' * LARGURA}╗")
print(f"║{'CONSUMO DE COMBUSTÍVEL'.center(LARGURA)}║")
print(f"╚{'═' * LARGURA}╝{RESET}")
print()

tempo_viagem = float(input(SETA + "Digite o tempo gasto na viagem (em horas): "))
velocidade_media = float(input(SETA + "Digite a velocidade média (em KM por horas): "))

distancia = tempo_viagem * velocidade_media
consumo_combustivel = distancia / RENDIMENTO

print()
linha_1 = f"  Distância percorrida: {distancia:.2f} km"
linha_2 = f"  Rendimento do veículo: {RENDIMENTO} km/L"
linha_3 = f"  Total de combustível gasto (em litros): {consumo_combustivel:.2f}"
print(f"{VERDE}┌{'─' * LARGURA}┐")
print(f"│{CINZA}{linha_1.ljust(LARGURA)}{VERDE}│")
print(f"│{CINZA}{linha_2.ljust(LARGURA)}{VERDE}│")
print(f"│{NEGRITO}{linha_3.ljust(LARGURA)}{RESET}{VERDE}│")
print(f"└{'─' * LARGURA}┘{RESET}")
