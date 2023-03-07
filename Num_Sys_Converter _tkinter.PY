#######=newpage/pagebreak
import time
import tkinter as tk



#######
#######

class denaryNS:
    def __init__(self, master):
        self.master = master
        master.title("Denary Number System")
        
        # Create label for output
        self.output_label = tk.Label(self.root, text="Choose output number system:\nDenary to ....")
        self.output_label.pack()
        
        # Create buttons for options
        self.binary_button = tk.Button(self.root, text="Binary (Base 2)", command=self.denary_to_binary)
        self.binary_button.pack()
        
        self.octal_button = tk.Button(self.root, text="Octal (Base 8)", command=self.denary_to_octal)
        self.octal_button.pack()
        
        self.hexadecimal_button = tk.Button(self.root, text="Hexadecimal (Base 16)", command=self.denary_to_hexadecimal)
        self.hexadecimal_button.pack()
        
        self.restart_button = tk.Button(self.root, text="Restart", command=self.restart)
        self.restart_button.pack()
        

    def denaryToBinary():
        def __init__(self, master):
            self.master = master
            master.title("NUMBER SYSTEM CONVERTER - Denary Number System")

            
        def convert(self):
            # Get input from user
            num = int(self.num_entry.get())

            # Initialize binary string
            binary = ""

            # Convert to binary using division and remainder
            while num > 0:
                binary = str(num % 2) + binary
                num //= 2

            # Output result
            result_str = f"The binary representation of {num} is {binary}"
            tk.Label(self.master, text=result_str).grid(row=3, column=0, columnspan=2, pady=10)

            # Prompt for repeat or exit
            repeat_exit_frame = tk.Frame(self.master)
            repeat_exit_frame.grid(row=4, column=0, columnspan=2)

            tk.Button(repeat_exit_frame, text="Repeat", command=self.repeat).grid(row=0, column=0, padx=5)
            tk.Button(repeat_exit_frame, text="Exit", command=self.master.quit).grid(row=0, column=1, padx=5)

        def repeat(self):
            self.num_entry.delete(0, 'end')
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
        print("\nThe binary representation of", EuInput, "is", octal)
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
        print("\nThe hexadecimal representation of", EuInput, "is", hexadecimal)
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
    def __init__(self,master):
        self.master = master
        master.title("Binary Number System")
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
            num = (input("Enter a Binary  number: "))
            EuInput.append(num)
            
            

            # Convert to denary 
            decimal_num = int(num, 2)

            
            
            # Output result
            print("\nThe Denary representation of", num, "is", decimal_num)
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
            print("\nThe Octal representation of", EuInput, "is", octal_num)
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
            print("\nThe Hexadecimal representation of", EuInput, "is", hexadecimal_str)
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
    def __init__(self,master):
        self.master = master
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
        print("\nThe denary representation of", EuInput, "is", decimal)
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
    def __init__(self,master):
        self.master = master
        master.title("NUMBER SYSTEM CONVERTER - Hexadecimal Number System")
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
class Menu:
    def __init__(self, master):
        self.master = master
        master.title("NUMBER SYSTEM CONVERTER")
        master.geometry("350x300")
        master.configure(background='black')
        self.main_frame = tk.Frame(master)
        self.main_frame.pack()

        tk.Label(self.main_frame, text="Choose input number system:").grid(row=0, column=0, columnspan=2)
        tk.Button(self.main_frame, text="1. Denary (Base 10)",  width=20, command=self.open_denaryNS).grid(row=1, column=0)
        tk.Button(self.main_frame, text="2. Binary (Base 2)", width=20, command=self.open_binaryNS).grid(row=2, column=0)
        tk.Button(self.main_frame, text="3. Octal (Base 8)",  width=20, command=self.open_octalNS).grid(row=3, column=0,)
        tk.Button(self.main_frame, text="4. Hexadecimal (Base 16)", width=20, command=self.open_hexadecimalNS).grid(row=4, column=0,)


       
        tk.Button(self.main_frame, text="Exit", width=20,command=master.quit).grid(row=7, column=0, padx=10, pady=10)

        self.current_menu = None

    def open_denaryNS(self):
        if self.current_menu:
            self.current_menu.destroy()
        self.current_menu = denaryNS(self.master)
        tk.Label(self.master, text="Enter a Denary number:").grid(row=0, column=0)
        self.num_entry = tk.Entry(self.master)
        self.num_entry.grid(row=0, column=1)

        tk.Button(self.master, text="Convert", command=self.convert).grid(row=1, column=0, columnspan=2, pady=10)
        tk.Button(self.master, text="Exit", command=self.master.quit).grid(row=2, column=0, columnspan=2, pady=10)


    def open_binaryNS(self):
        if self.current_menu:
            self.current_menu.destroy()
        self.current_menu = binaryNS(self.master)

    def open_octalNS(self):
        if self.current_menu:
            self.current_menu.destroy()
        self.current_menu = octalNS(self.master)

    def open_hexadecimalNS(self):
        if self.current_menu:
            self.current_menu.destroy()
        self.current_menu = hexadecimalNS(self.master)


    


#######
#######
root = tk.Tk()
menu = Menu(root)
root.mainloop()