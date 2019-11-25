import requests
import json


def getArticulos(URL):
    response = requests.get(url=URL)
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print('Error getArticulos')


def createArticulo(URL, data):
    response = requests.post(URL, json=data, headers=headers)
    if response.status_code == 200:
        text_url = response.text
        print(text_url)
    else:
        print('Error createArticulo')


def updateArticulo(URL, data, pk):
    URL = URL+str(pk)
    response = requests.put(URL, json=data, headers=headers)
    if response.status_code == 200:
        pastbin_url = response.text
        print(pastbin_url)
    else:
        print('Error updateArticulo')


def deleteArticulo(URL, pk):
    URL = URL+str(pk)
    response = requests.delete(URL, headers=headers)
    if response.status_code == 200:
        pastbin_url = response.text
        print(pastbin_url)
    else:
        pastbin_url = response.text
        print(pastbin_url)


if __name__ == "__main__":

    # headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    URL = "http://127.0.0.1:8000/api/articulos/"
    headers = {'Accept': 'application/json, text/plain', 'Content-type': 'application/json'}
    print("\nARTICULOS: ")
    getArticulos(URL)

    data = {"articulo": {
                "id": 8,
                "titulo": "Titulo Nuevo",
                "contenido": "Contenido Nuevo",
                "autores_id": 1}}

    print("\nCreando articulo con id 8:")
    createArticulo(URL, data)
    getArticulos(URL)
    print("\n")

    print("Modificando articulo con id 8:")
    pk = 8
    data = {"articulo": {
                "titulo": "TituloModificado",
                "contenido": "Contenido Modificado",
                "autores_id": 1}}
    updateArticulo(URL, data, pk)
    getArticulos(URL)
    # for i in range(12, 21:
    # deleteArticulo(URL, i)
    print("\n")
    print("Eliminando articulo con id 8:")
    pk = 8
    deleteArticulo(URL, pk)
    getArticulos(URL)
