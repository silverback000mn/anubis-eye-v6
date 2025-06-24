import json, os
from datetime import datetime

def atualizar_status(nome):
    os.makedirs("status", exist_ok=True)
    status_data = {
        "nome": nome,
        "status": "🟢 Ativa",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    with open(f"status/{nome}.status", "w") as f:
        json.dump(status_data, f, indent=4)
