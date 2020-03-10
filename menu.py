def menu():
        print("---------- Menu Laboratorio Seguridad Informatica 2020-I ----------")
        print ("\t1 - Generate a key public and private")
        print ("\t2 - View the key pulic and private")
        print ("\t3 - Encrypt a file")
        print ("\t4 - Decrypt a file")
        print ("\t5 - Exit")
        
while True:
        menu()
        opcionMenu = input("Choose an option: >> ")
 
        if opcionMenu=="1":
                print ("")
                input("Has pulsado la opción 1...\npulsa una tecla para continuar")
        elif opcionMenu=="2":
                print ("")
                input("Has pulsado la opción 2...\npulsa una tecla para continuar")
        elif opcionMenu=="3":
                print ("")
                input("Has pulsado la opción 3...\npulsa una tecla para continuar")
        elif opcionMenu=="4":
                print("")
                input("Has pulsado la opción 4...\npulsa una tecla para continuar")
        elif opcionMenu=="5":
                break
        else:
                print ("")
                input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
