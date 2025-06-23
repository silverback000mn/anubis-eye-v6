import random
import time

comentarios = [
    "Demais essa foto! 😍",
    "Sensacional 🔥",
    "Amei! 👏👏",
    "Muito top isso",
    "Me identifiquei 🙌",
    "Onde é isso? 👀",
    "👏👏👏",
    "Perfeito 🔥🔥",
    "Lindo demais",
    "Você manda bem demais 😎"
]

def delay_humano(min_t=1.0, max_t=3.0):
    tempo = round(random.uniform(min_t, max_t), 2)
    time.sleep(tempo)

def curtir_post():
    delay_humano()
    print("[AÇÃO] ❤️ Curtida enviada")

def seguir_usuario():
    delay_humano()
    print("[AÇÃO] ➕ Seguindo usuário")

def comentar_post():
    delay_humano()
    comentario = random.choice(comentarios)
    print(f"[AÇÃO] 💬 Comentário: \"{comentario}\"")

def simular_interacoes(qtd=5):
    print(f"[SIMULAÇÃO] Rodando {qtd} interações...")
    for _ in range(qtd):
        acao = random.choice([curtir_post, seguir_usuario, comentar_post])
        acao()

if __name__ == "__main__":
    simular_interacoes()
