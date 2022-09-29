#Hacer un programa que permita ingresar los nombres y las notas de 10 alumnos. Mostrar por pantalla el nombre del alumno con la nota más alta ingresada.
MayorNota=1
MayorAlumno=None
for i in range(10):
    Nombre=input("Ingrese el nombre del alumno: ")
    Nota=float(input("Ahora ingrese su nota: "))
    if Nota>MayorNota:
        MayorNota=Nota
        MayorAlumno=Nombre
print("El alumno con la nota mas alta es {} con {}".format(MayorAlumno,MayorNota))