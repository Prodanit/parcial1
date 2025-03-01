import requests
import pandas as pd

APP_TOKEN = "qzQcSzKYMXVL4zbxEd9TB2zbC"

def obtener_datos(departamento, limite=100):
    """
    Realiza una solicitud a la API de datos abiertos de Colombia.

    Args:
        departamento (str): Nombre del departamento a consultar.
        limite (int): Número de registros a obtener.

    Returns:
        list: Datos obtenidos de la API o None en caso de error.
    """
    url = "https://www.datos.gov.co/resource/gt2j-8ykr.json"
    params = {
        "departamento_nom": departamento,
        "$limit": limite,
        "$$app_token": APP_TOKEN  
    }

    # Solicitud a la API
    response = requests.get(url, params=params)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        datos = response.json()  # Convertir la respuesta a JSON
    else: 
        print(f"Error al obtener datos de la API. Código; {response.status_code}")
    return None

def convertir_a_dataframe(datos):
        """
    Convierte los datos de la API en un DataFrame con columnas seleccionadas.

    Args:
        datos (list): Datos obtenidos de la API.

    Returns:
        DataFrame | None: DataFrame con los datos filtrados o None si no hay datos.
    """
        if not datos:
            return None
        
        df = pd.DataFrame(datos)

        columnas_correctas = [
                "ciudad_municipio_nom",
                "departamento_nom",
                "edad",
                "fuente_tipo_contagio", 
                "estado",
                "pais_viajo_1_nom"
            ]

            # Mostrar solo si existen en el DataFrame
        columnas_existentes = [col for col in columnas_correctas if col in df.columns]

        return df[columnas_existentes] if columnas_existentes else None