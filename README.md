 Permanente 1b Trabajo realizado por:
 
 Kelvin Andreé Caya Zeballos
          
          
          x = int(input("Ingrese su clave"))

          if x == 1313:

          a = 1000

La x seria la variable de la clave y la a es la variable que esta representando al saldo


        print("Bienvenido al cajero su saldo es de", a)
        print("Seleccione la opcion que desea")
        print("1. Retirar dinero\n2. Mostrar saldo dispnible\n3. Salir")

Aqui se muestran las opciones al ingresar al cajero con la contraseña

        b = int(input("->")
Esto solo es decoracion al elegir una opción

             if b == 1:
             print("","Opcion 1 = Retirar 20 soles","\n",  "Opcion 2 = Retirar 50 soles", "\n","Opcion 3 = Retirar 100 soles","\n","Opcion 4 = Retirar 150 soles","\n",  "Opcion 5 = Retirar 500 soles", "\n","Opcion 6 = Elije el monto")
             
Al entrar a Retirar dinero estas son las opciones que te da a elegir

                r20 = 1
                r50 = 2
                r100 = 3
                r150 = 4
                r500 = 5
                g = 6
                
Asignamos distintas variables y el numero para elegir estas opciones 

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
