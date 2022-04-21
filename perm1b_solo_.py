x = int(input("Ingrese su clave"))
if x == 1313:
        a = 1000
        print("Bienvenido al cajero su saldo es de", a)
        print("Seleccione la opcion que desea")
        print("1. Retirar dinero\n2. Mostrar saldo dispnible\n3. Salir")

        b = int(input("->"))
      
        if b == 1:
                print("","Opcion 1 = Retirar 20 soles","\n",  "Opcion 2 = Retirar 50 soles", "\n","Opcion 3 = Retirar 100 soles","\n","Opcion 4 = Retirar 150 soles","\n",  "Opcion 5 = Retirar 500 soles", "\n","Opcion 6 = Elije el monto")
                r20 = 1
                r50 = 2
                r100 = 3
                r150 = 4
                r500 = 5
                g = 6
                monto = int(input("->"))
                if monto == r20:
                        print(a-20)
                elif monto == r50:
                        print(a-50)
                elif monto == r100:
                        print(a-100)
                elif monto == r150:
                        print(a-150)
                elif monto == r500:
                        print(a-500)
                elif monto == g:
                        w =int(input("Ingrese un monto deseado"))
                        if w == 0 or w > a:
                                print("Cantidad invalida") 
        elif b == 2:
                print(a)
        elif b == 3:
                print("Gracias por usar su cajero")
        else:
                print("seleccione una de las opciones indicadas")
else :
        print("Clave incorrecta")
 