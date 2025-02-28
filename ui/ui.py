def solicitar_datos():
    departamento = input("Ingrese el nombre del departamento: ")
    limite = int(input("Ingrese el número de registros a consultar: "))
    return departamento, limite

def mostrar_datos(df):
    print(df[["ciudad_municipio_nom", "departamento_nom", "edad", "tipo", "estado", "pais_viajo_1_nom"]])

