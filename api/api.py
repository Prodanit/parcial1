import pandas as pd
from sodapy import Socrata

def obtener_datos(departamento, limite):
    client = Socrata("www.datos.gov.co", None)
    resultados = client.get("gt2j-8ykr", limit=limite, departamento=departamento)
    return pd.DataFrame.from_records(resultados)
