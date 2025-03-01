from api.api import obtener_datos, convertir_a_dataframe
from ui.ui import solicitar_datos, mostrar_datos

def main():
    departamento, limite = solicitar_datos()

    datos = obtener_datos(departamento, limite)

    if datos:
        df = convertir_a_dataframe(datos)
        
        if df is not None:
            mostrar_datos(df)
        else:
            print("No hay datos para mostrar.")
    else:
        print("No se pudieron obtener los datos de la API.")

if __name__ == "__main__":
    main()
