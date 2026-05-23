from config import API_URL
from fetcher import buscar_dados
from storage import salvar_dados


def main() -> None:
    """Busca dados da API e salva em arquivo JSON."""

    dados = buscar_dados(API_URL)

    if dados:
        salvar_dados(dados, "posts.json")
    else:
        print("Nenhum dado retornado. Sincronizacao falhou.")


if __name__ == "__main__":
    main()
