import requests
import json

URL = "http://127.0.0.1:8000/api/articulos/"

titulo='Titulo3'

PARAMS = {'titulo':titulo}

r = requests.get(url = URL, params = PARAMS)

data = r.json()

print(data)


r= requests.post('http://httpbin.org/post', json={"key": "value"})
r.status_code

print(r)
print(r.json())





data = {"articulo":{
            "titulo": "TituloNuevo",
            "contenido": "Contenido NUEVO",
            "autores_id": 1
}}


#headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
headers = {'Accept':'application/json, text/plain', 'Content-type': 'application/json',}
r = requests.post(URL, json=data, headers=headers)
pastbin_url = r.text
print(pastbin_url)



URL = "http://127.0.0.1:8000/api/articulos/17"
r = requests.delete(URL, headers=headers)
pastbin_url = r.text
print(pastbin_url)


data = {"articulo":{
            "titulo": "TituloNuevoModificado",
            "contenido": "Contenido NUEVOModificado",
            "autores_id": 1
}}




URL = "http://127.0.0.1:8000/api/articulos/19"
headers = {'Accept':'application/json, text/plain', 'Content-type': 'application/json',}
r = requests.put(URL, json=data, headers=headers)
pastbin_url = r.text
print(pastbin_url)
