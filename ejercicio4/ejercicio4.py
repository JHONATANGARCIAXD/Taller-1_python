"""Ejercicio No. 3"""


# input 

peso=int(input("Cual es su peso:"))
altura=float(input("Cual es su altura:"))


# processing


IMC= peso / altura**2

if IMC<16:
    print("Su estado es: Criterio de ingreso en hospital.")

elif IMC >16 and IMC <17:
    print("Su estado es: Infrapeso") 
elif IMC >17 and IMC <18:
    print("Su estado es: Bajo peso")
elif IMC >18 and IMC <25:
    print("Su estado es: Peso normal (saludable)")
elif IMC >25 and IMC <30:
    print("Su estado es: Sobrepeso (obesidad de grado I)")
elif IMC >30 and IMC <35:
    print("Su estado es: Sobrepeso crónico (obesidad de grado II)")
elif IMC >35 and IMC <40:
    print("Su estado es: Obesidad premórbida (obesidad de grado III)")
elif IMC >40:
    print("Su estado es: Obesidad mórbida (obesidad de grado IV)")





