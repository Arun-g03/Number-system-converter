#######=newpage/pagebreak
import time
print("-----------")
print("NUMBER SYSTEM CONVERTER")
print("-----------")
print("By A.Garcha")
print("This application can be used to convert the 4 number systems listed below, between each other.")
time.sleep(2)

#######
#######

class denaryNS():
    def __init__(self):
        print("-----------")
        print("\nChoose output number system:\nDenary to ....")
        print("  1. Binary (Base 2)")
        print("  2. Octal (Base 8)")
        print("  3. Hexadecimal (Base 16)")
        print("  4. Restart\n")
        

        choice = int(input("Option number: "))
        if choice == 1:
            denaryNS.denary_to_binary()
        elif choice == 2:
            denaryNS.denary_to_octal()
        elif choice == 3:
            denaryNS.denary_to_hexadecimal()
        elif choice == 4:
            time.sleep(1)
            Menu()
        else:
            print("\nInvalid option.\n")
            time.sleep(1)
            denaryNS()

    def denary_to_binary():
        EuInput=[]
        print("\n-----------")
        print("Denary to Binary:")
        # Prompt user for input
        num = int(input("Enter a Denary number: "))
        EuInput.append(num)
        

        # Initialize binary string
        binary = ""

        # Convert to binary using division and remainder
        while num > 0:
            binary = str(num % 2) + binary
            num //= 2

        # Output result
        print("\nDenary:", EuInput, "\nBinary:", binary)
        time.sleep(4)
        
        choice = input("Press R to repeat conversion type.\nPress E to Exit\nInput:")
        if choice.lower() == "r":
            denaryNS.denary_to_binary()
        elif choice.lower() == "e":
            Menu()
        else:
            print("\nInvalid option.\n")
            time.sleep(1)
            denaryNS.denary_to_binary()
##denary to binary completed
    def denary_to_octal():
        EuInput=[]
        print("\n-----------")
        print("Denary to Octal:")
        # Prompt user for input
        num = int(input("Enter a Denary number: "))
        EuInput.append(num)
        

        # Initialize Octal string
        octal = ""

        # Convert to Octal 
        while num > 0:
            octal = str(num % 8) + octal
            num //= 8

        # Output result
        print("\nDenary:", EuInput, "\nOctal:", octal)
        time.sleep(4)
        
        choice = input("Press R to repeat conversion type.\nPress E to Exit\nInput:")
        if choice.lower() == "r":
            denaryNS.denary_to_octal()
        elif choice.lower() == "e":
            Menu()
        else:
            print("\nInvalid option.\n")
            time.sleep(1)
            denaryNS.denary_to_octal()
            
    def denary_to_hexadecimal():
        EuInput=[]
        print("\n-----------")
        print("Denary to Hexadecimal:")
        # Prompt user for input
        num = int(input("Enter a Denary number: "))
        EuInput.append(num)
        

        # Convert to hexadecimal 
        #wanted to ensure hexidecimals were output as capitals
        hex_digits = "0123456789ABCDEF"
        hexadecimal = ""

        while num > 0:
            remainder = num % 16
            hexadecimal = hex_digits[remainder] + hexadecimal
            num = num // 16

        
        
        # Output result
        print("\nDenary:", EuInput, "\nHexadecimal:", hexadecimal)
        time.sleep(4)
        
        choice = input("Press R to repeat conversion type.\nPress E to Exit\nInput:")
        if choice.lower() == "r":
            denaryNS.denary_to_hexadecimal()
        elif choice.lower() == "e":
            Menu()
        else:
            print("\nInvalid option.\n")
            time.sleep(1)
            denaryNS.denary_to_hexadecimal()
#######
#######


class binaryNS():
    def __init__(self):
        print("\nInput type= Binary\nChoose output number system:")
        print("1. Denary (Base 10")
        print("2. Octal (Base 8)")
        print("3. Hexadecimal (Base 16)")
        print("4. Restart")

#######
#######

        def binary_to_denary():
            EuInput=[]
            print("\n-----------")
            print("Binary to Denary:")
            # Prompt user for input
            while True:
                num = input("Enter a Binary  number: ")
                if num.isdigit() and all(c in '01' for c in num):
                    break
                else:
                    print("Invalid input. Please enter a binary number.")
                EuInput.append(num)

                # Convert to denary 
                decimal_num = int(num, 2)

                # Output result
                print("\nBinary:", EuInput, "\nDenary:", decimal_num)
                time.sleep(4)

                
        
                choice = input("Press R to repeat conversion type.\nPress E to Exit\nInput:")
                if choice.lower() == "r":
                    binaryNS.binary_to_denary()
                elif choice.lower() == "e":
                    Menu()
                else:
                    print("\nInvalid option.\n")
                    time.sleep(1)
                    binaryNS.binary_to_denary()
        
                
#######
#######
        def binary_to_octal():
            EuInput=[]
            print("\n-----------")
            print("Binary to Octal:")
            # Prompt user for input
            num = (input("Enter a Binary  number: "))
            EuInput.append(num)
            

            # Convert to octal 
            decimal_num = int(num, 2)
            octal_num = oct(decimal_num)

            
            
            # Output result
            print("\nBinary:", EuInput, "\nOctal:", decimal_num)
            time.sleep(4)
        
            choice = input("Press R to repeat conversion type.\nPress E to Exit\nInput:")
            if choice.lower() == "r":
                binaryNS.binary_to_octal()
            elif choice.lower() == "e":
                Menu()
            else:
                print("\nInvalid option.\n")
                time.sleep(1)
                binaryNS.binary_to_octal()
#######
#######
        def binary_to_hexadecimal():
            EuInput=[]
            print("\n-----------")
            print("Binary to Hexadecimal:")
            # Prompt user for input
            num = (input("Enter a Binary  number: "))
            EuInput.append(num)
            

            # Convert to binary 
            denary = 0
            for digit in num:
                denary = denary * 2 + int(digit)
            hexadecimal_str = hex(denary).lstrip("0x").upper()

            
            
            # Output result
            print("\Binary:", EuInput, "\nHexadecimal:", hexadecimal_str)
            
            time.sleep(4)
        
            choice = input("Press R to repeat conversion type.\nPress E to Exit\nInput:")
            if choice.lower() == "r":
                binaryNS.binary_to_hexadecimal()
            elif choice.lower() == "e":
                Menu()
            else:
                print("\nInvalid option.\n")
                time.sleep(1)
                binaryNS.binary_to_denary()
                
        choice = int(input("Option number: "))
        if choice == 1:
            binary_to_denary()
        elif choice == 2:
            binary_to_octal()
        elif choice == 3:
            binary_to_hexadecimal()
        elif choice == 4:
            time.sleep(1)
            Menu()
        else:
            print("\nInvalid option.\n")
            time.sleep(1)
            binaryNS()
#######
#######
class octalNS():
    def __init__(self):
        print("\nInput type= Octal\nChoose output number system:")
        print("1. Denary (Base 10)")
        print("2. Binary (Base 2)")
        print("3. Hexadecimal (Base 16)")
        print("4. Restart")

        choice = int(input("Option number: "))
        if choice == 1:
            octalNS.octal_to_denary()
        elif choice == 2:
            octalNS.octal_to_binary()
        elif choice == 3:
            octalNS.octal_to_hexadecimal()
        elif choice == 4:
            time.sleep(1)
            Menu()
        else:
            print("\nInvalid option.\n")
            time.sleep(1)
            octalNS()
#######
#######
    def octal_to_denary():
        EuInput=[]
        print("\n-----------")
        print("Octal to Denary:")
        # Prompt user for input
        num = (input("Enter a Octal number: "))
        EuInput.append(num)
        

        # Convert to Octal 
        decimal = 0
        power = 0
        for digit in reversed(num):
            decimal += int(digit) * (8 ** power)
            power += 1
        
        
        # Output result
        print("\nOctal:", EuInput, "\nDenary:", decimal)
        time.sleep(4)

        choice = input("Press R to repeat conversion type.\nPress E to Exit\nInput:")
        if choice.lower() == "r":
            octalNS.octal_to_denary()
        elif choice.lower() == "e":
            Menu()
        else:
            print("\nInvalid option.\n")
            time.sleep(1)
            denaryNS.denary_to_hexadecimal()
    #######
    #######
    def octal_to_binary():
        EuInput=[]
        print("\n-----------")
        print("Octal to Binary:")
        # Prompt user for input
        num = (input("Enter a Octal number: "))
        EuInput.append(num)
        

        # Convert to Octal 
        binary = ""
        for digit in num:
            binary += format(int(digit), '03b')
        
        
        # Output result
        print("\nThe Binary representation of", EuInput, "is", binary)
        
        time.sleep(4)

        choice = input("Press R to repeat conversion type.\nPress E to Exit\nInput:")
        if choice.lower() == "r":
            octalNS.octal_to_binary()
        elif choice.lower() == "e":
            Menu()
        else:
            print("\nInvalid option.\n")
            time.sleep(1)
            denaryNS.denary_to_hexadecimal()
    #######
    #######
    def octal_to_hexadecimal():
        EuInput=[]
        print("\n-----------")
        print("Octal to Hexadecimal:")
        # Prompt user for input
        num = (input("Enter a Octal number: "))
        EuInput.append(num)
        

        # Convert to Octal 
        decimal = int(num, 8)
        hexadecimal = format(decimal, 'X')
        
        
        # Output result
        print("\nThe Hexadecimal representation of", EuInput, "is", hexadecimal)
        time.sleep(4)

        choice = input("Press R to repeat conversion type.\nPress E to Exit\nInput:")
        if choice.lower() == "r":
            octalNS.octal_to_hexadecimal()
        elif choice.lower() == "e":
            Menu()
        else:
            print("\nInvalid option.\n")
            time.sleep(1)
            denaryNS.denary_to_hexadecimal()
#######
#######

class hexadecimalNS():
    def __init__(self):
        print("\nInput type= Hexadecimal\nChoose output number system:")
        print("1. Denary (Base 10)")
        print("2. Binary (Base 2)")
        print("3. Octal (Base 8)")
        print("4. Restart")

        choice = int(input("Option number: "))
        if choice == 1:
            hexadecimalNS.hexadecimal_to_denary()
        elif choice == 2:
            hexadecimalNS.hexadecimal_to_binary()
        elif choice == 3:
            hexadecimalNS.hexadecimal_to_octal()
        elif choice == 4:
            time.sleep(1)
            Menu()
        else:
            print("\nInvalid option.\n")
            time.sleep(1)
            hexadecimalNS()

    def hexadecimal_to_binary():
        EuInput=[]
        print("\n-----------")
        print("Hexadecimal to Binary:")
        # Prompt user for input
        num = (input("Enter a Octal number: "))
        EuInput.append(num)
        

        # Convert to Octal 
        binary = bin(int(num, 16)).lstrip("0b")
        
        # Output result
        print("\nThe Binary representation of Hex number-", EuInput, "is", binary)
        time.sleep(4)

        choice = input("Press R to repeat conversion type.\nPress E to Exit\nInput:")
        if choice.lower() == "r":
            hexadecimalNS.hexadecimal_to_binary()
        elif choice.lower() == "e":
            Menu()
        else:
            print("\nInvalid option.\n")
            time.sleep(1)
            hexadecimalNS.hexadecimal_to_binary()
        #######
        #######
    def hexadecimal_to_denary():
        EuInput=[]
        print("\n-----------")
        print("Hexadecimal to Denary:")
        # Prompt user for input
        num = (input("Enter a Hexadecimal number: "))
        EuInput.append(num)
        

        # Convert to Octal 
        denary = int(num, 16)
        
        # Output result
        print("\nThe Denary representation of Hex number-", EuInput, "is", denary)
        time.sleep(4)

        choice = input("Press R to repeat conversion type.\nPress E to Exit\nInput:")
        if choice.lower() == "r":
            hexadecimalNS.hexadecimal_to_denary()
        elif choice.lower() == "e":
            Menu()
        else:
            print("\nInvalid option.\n")
            time.sleep(1)
            hexadecimalNS.hexadecimal_to_denary()
        #######
        #######
    def hexadecimal_to_octal():
        EuInput=[]
        print("\n-----------")
        print("Hexadecimal to Octal:")
        # Prompt user for input
        num = (input("Enter a Hexadecimal number: "))
        EuInput.append(num)
        

        # Convert to Octal 
        decimal_num = int(num, 16)
        octal = oct(decimal_num).lstrip("0o")
        
        # Output result
        print("\nThe Octal representation of Hex number-", EuInput, "is", octal)
        time.sleep(4)

        choice = input("Press R to repeat conversion type.\nPress E to Exit\nInput:")
        if choice.lower() == "r":
            hexadecimalNS.hexadecimal_to_octal()
        elif choice.lower() == "e":
            Menu()
        else:
            print("\nInvalid option.\n")
            time.sleep(1)
            hexadecimalNS.hexadecimal_to_octal()
        #######
        #######
#######
#######
class Menu():
    def __init__(self):
        self.valid_choices = ['1', '2', '3', '4']
        
        print("\n------Main Menu------")
        print("Choose input number system:")
        print("1. Denary (Base 10)")
        print("2. Binary (Base 2)")
        print("3. Octal (Base 8)")
        print("4. Hexadecimal (Base 16)")
        print("5. Exit")

        choice = int(input("Option number: "))
        if choice == 1:
            time.sleep(1)
            denaryNS()
        elif choice == 2:
            time.sleep(1)
            binaryNS()
        elif choice == 3:
            time.sleep(1)
            octalNS()
        elif choice == 4:
            time.sleep(1)
            hexadecimalNS()
        elif choice == 5:
            print("\nThanks for coming!")
            time.sleep(1)
            SystemExit()
        else:
            print("\nInvalid option.\n")
            time.sleep(1)
            Menu()
#######
#######
if __name__ == "__main__":
    Menu()