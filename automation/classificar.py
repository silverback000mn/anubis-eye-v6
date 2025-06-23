import random

def classificar_conta(bio_ok=True, fotos=12, interacoes=5):
    score = 0

    if bio_ok:
        score += 1
    if fotos >= 9:
        score += 1
    if interacoes >= 4:
        score += 1

    if score == 3:
        qualidade = "Alta"
    elif score == 2:
        qualidade = "Média"
    else:
        qualidade = "Baixa"

    print(f"[CLASSIFICADOR] ✅ Conta classificada como: {qualidade.upper()}")

    return qualidade

# Exemplo de uso:
if __name__ == "__main__":
    bio = random.choice([True, False])
    fotos = random.randint(4, 15)
    interacoes = random.randint(1, 6)

    print(f"\nBio presente: {bio}")
    print(f"Fotos: {fotos}")
    print(f"Interações: {interacoes}")
    classificar_conta(bio, fotos, interacoes)
