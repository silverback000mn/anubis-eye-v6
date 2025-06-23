import time
import random

def delay_curto():
    tempo = round(random.uniform(1.5, 3.0), 2)
    print(f"[DELAY] ⏱️ Aguardando {tempo}s (curto)")
    time.sleep(tempo)

def delay_medio():
    tempo = round(random.uniform(4.0, 7.0), 2)
    print(f"[DELAY] ⏱️ Aguardando {tempo}s (médio)")
    time.sleep(tempo)

def delay_longo():
    tempo = round(random.uniform(8.0, 15.0), 2)
    print(f"[DELAY] ⏱️ Aguardando {tempo}s (longo)")
    time.sleep(tempo)

def delay_customizado(segundos):
    print(f"[DELAY] ⏱️ Esperando {segundos}s (customizado)")
    time.sleep(segundos)

# Exemplo de uso:
if __name__ == "__main__":
    delay_curto()
    delay_medio()
    delay_longo()
    delay_customizado(5)
