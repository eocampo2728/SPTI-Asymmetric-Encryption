
import encrypt
import decrypt
import GenerateKeys

def menu():
        print("---------------------- Menu --------------------------")
        print ("1 - Generate a key public and private")
        print ("2 - Encrypt a file")
        print ("3 - Decrypt a file")
        print ("4 - Exit")
        
while True:
        menu()
        
        opcionMenu = raw_input("Choose an option: >> ").strip()
 
        if opcionMenu=="1":
                GenerateKeys.main()
                
        elif opcionMenu=="2":
                encrypt.main()

        elif opcionMenu=="3":
                decrypt.main()

        elif opcionMenu=="4":
                break
        else:
                print ("")
                raw_input("You have not pressed any correct option...\npress a key to continue ")
