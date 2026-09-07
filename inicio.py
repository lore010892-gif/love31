# Un programa que decide si un usuario puede registrarse
edad = int(input("Por favor, ingresa tu edad: "))

if edad >= 18:
    print("¡Acceso concedido! Eres mayor de edad para usar la app. 🎉")
else:
    print("Acceso denegado. Debes tener al menos 18 años. ❌")