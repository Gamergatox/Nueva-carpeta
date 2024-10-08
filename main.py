from flask import Flask
import random 

app = Flask(__name__)
frases_list=["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos","Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.", "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna","Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo", "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo","Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos", "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos", "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas" ]
caracteres = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")


@app.route('/')
def pagina_inicial():
    return "<h1>Hola mundo<h1/><a href=/DatosAleatorios>Ir a ver los datos aleatorios<a/>   <a href=/Contraseña>Genera una contraseña de 10 caracteres<a/>   <a href=/Coin_flip>Gira una moneda<a/>"

@app.route('/DatosAleatorios')
def dato_alet():
    return f"<p>{random.choice(frases_list)}<p>"

@app.route('/Contraseña')
def contraseña():
    lenght = 10
    password = ""
    for i in range (lenght):
        password += random.choice(caracteres)
    return f"<p>{password}<p>"

@app.route('/Coin_flip')
def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "Cara"
    else:
        return "Cruz"

@app.route("/Gatoriendo")
def Gatoriendo():
   return "<img src=img/gatoriendo.jpg alt=Image>"

app.run(debug=True)