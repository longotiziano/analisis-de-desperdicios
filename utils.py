import requests 
from typing import Any, Tuple

requests_headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}

def realizar_request(url: str) -> Tuple[bool, Any | None]:
    """
    Función auxiliar para realizar requests HTTP y manejar errores de forma centralizada.
    Retorna:
    - (True, data) si la request fue exitosa
    - (False, None) si ocurrió algún error
    """ 
    try:
        # Realizar la request con un timeout
        response = requests.get(url, headers=requests_headers, timeout=(5, 10))
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la request a {url}: {e}")
        return False, None

    try:
        # Parsear la respuesta JSON
        data = response.json()
    except ValueError:
        print(f"Error al parsear la respuesta JSON de {url}")
        return False, None
    return True, data