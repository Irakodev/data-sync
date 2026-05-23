import json
import os


def salvar_dados(dados: list[dict], arquivo: str) -> None:
    """Salva lista de dicts como JSON dentro da pasta data/."""

    caminho = os.path.join("data", arquivo)

    try:
        os.makedirs("data", exist_ok=True)

        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)

        print(f"Dados salvos em '{caminho}' ({len(dados)} registros).")

    except Exception as erro:
        print(f"Erro ao salvar os dados: {erro}")