from faker import Faker
import random

fake = Faker('pt_BR')

def gerar_bio():
    emojis = ["🌟", "🚀", "💡", "📸", "🎯", "💬", "🌍", "💻", "🧠", "🎨"]
    profissoes = ["Designer", "Estudante", "Criador de Conteúdo", "Fotógrafo", "Desenvolvedor", "Artista", "Cientista", "Empreendedor"]
    frases = [
        "Vivendo um dia de cada vez
