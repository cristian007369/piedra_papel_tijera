print("-----------------------------------------------")
print("-----------piedra,papel y tijera---------------")
print("-----------------------------------------------")

import random

print("selecciona 1 para piedra")
print("selecciona 2 para papel")
print("selecciona 3 para tijera")
print("-----------------------------------------------")
usuario=int(input("Seleccione una de las tres opccioes: "))
print("-----------------------------------------------")
maquina=random.randint(1,3)
if usuario==1 and maquina==1:
    rta="Empate"
elif usuario== 1 and maquina==2:
    rta="perdiste"
elif usuario==1 and maquina==3:
    rta="ganaste"
elif usuario==2 and maquina==1:
    rta="ganaste"
elif usuario==2 and maquina==2:
    rta="empate"
elif usuario==2 and maquina==3:
    rta="perdiste"
elif usuario==3 and maquina==1:
    rta="perdiste"
elif usuario==3 and maquina==2:
    rta="ganaste"
elif usuario==3 and maquina==3:
    rta="empate"
else:
    rta="Entrada no valida"

if usuario==1:
    usuario="piedra"
elif usuario==2:
    usuario="papel"
elif usuario==3:
    usuario="tijera"
else:
    usuario="opción no valida"

if maquina==1:
    maquina="piedra"
elif maquina==2:
    maquina="papel"
else:
    maquina="tijera"


print(str(rta))
print("-----------------------------------------------")
print("Maquina saco "+str(maquina))
print("usuario saco "+str(usuario))
print("-----------------------------------------------")