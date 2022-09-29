#Hacer un algoritmo que permita ingresar por pantalla números naturales y al finalizar informar:
# ¿Cuántos están entre el 50 y 75, ambos inclusive?
# ¿Cuántos mayores de 80?
# ¿Cuántos menores de 30?
# El algoritmo debe permitir continuar ingresando números hasta que se ingrese el número 0.
Numero=int(input("Ingrese un numero: "))
Entre50_75=0
Mayores_80=0
Menores_30=0
while Numero!=0:
    if 50<=Numero<=75:
        Entre50_75=Entre50_75+1
    elif Numero>80:
        Mayores_80=Mayores_80+1
    elif Numero<30:
        Menores_30=Menores_30+1
    Numero = int(input("Ingrese un numero: "))
print("La cantidad de numeros entre 50 y 75 es {}".format(Entre50_75))
print("La cantidad de numeros mayores de 80 es {}".format(Mayores_80))
print("La cantidad de numeros menores de 30 es {}".format(Menores_30))
