nombre = raw_input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
if edad > 0 and edad < 18:
    print "aun no eres mayor de edad", (nombre)
elif edad >= 18:
    print "eres mayor de edad", (nombre)
else:
    print "error"
