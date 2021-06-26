# Coins Scrapper by Martín Ayo
## Descripción
API que devuelve las información de criptomonedas desde la web https://coinmarketcap.com/currencies/.
Al ejecutar el programa se creará un archivo dentro de la raíz llamado "currencies.json" que guardará
la información.


## Funcionalidades

- /currencies/all -- Devuelve todas las monedas actualizadas que se encuentren en el archivo "currencies.json".
- /currencies/<currency> -- Devuelve la información de la moneda que se ingresa por el parámetro.

Ejm.: /currencies/bitcoin



## Requerimientos

- Python 3.8+
- Flask 2.0+

## Ejecución
- Instalar dependencias desde el archivo requeriments.txt -- pip install -r requirements.txt
- Ejecutar flask run
