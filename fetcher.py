import time
import requests
from config import MAX_TENTATIVAS, ESPERA_INICIAL


def buscar_dados(url: str) -> list:
    """Faz GET com retry exponencial. Retorna lista vazia se tudo falhar."""

    espera = ESPERA_INICIAL

    for tentativa in range(1, MAX_TENTATIVAS + 1):
        try:
            resposta = requests.get(url, timeout=10)
            resposta.raise_for_status()
            return resposta.json()

        except requests.RequestException as erro:
            print(f"Tentativa {tentativa} falhou: {erro}")

            if tentativa < MAX_TENTATIVAS:
                print(f"Aguardando {espera}s...")
                time.sleep(espera)
                espera *= 2

    print("Todas as tentativas falharam.")
    return []