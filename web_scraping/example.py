import time
import web_scrapping as ws # importando el script

navegador = ws.WebScrapper() # creando el objeto navegador
#Por defecto ya tiene definido una ruta de descarga y un useragent

"""
algunas de las funciones que selenium usa por defecto son reutilizadas en otras funciones para manejarlos comodame
nte a partir del objeto creado
go_to:  siendo get para ir a un sitio web especifico
refr:   siendo refresh para recargar el sitio
"""
navegador.go_to("https://www.w3schools.com/")
time.sleep(2)
navegador.refr()
"""

Se han establecido acciones predeterminadas que son las mas usadas comunmente
click:      para "clickear" sobre un elemento
write:      para escribir sobre un elemento (esto es en los coampos de texto)
get_text:   para obtener el valor de un elemento transformado y retornando a string

"""

navegador.click('//*[@id="subtopnav"]/a[5]')
time.sleep(2)
navegador.write("Java", '//*[@id="tnb-google-search-input"]')
time.sleep(2)
navegador.click('//*[@id="tnb-google-search-submit-btn"]')
time.sleep(2)
cadena = navegador.get_text('//*[@id="main"]/h1')

print(cadena)