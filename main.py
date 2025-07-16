# Libraries
import os

# Create History file if it does not exist
History_file = "history.txt"
if not os.path.exists(History_file):
    with open(History_file , "w") as f:
        pass # Create An Empty file


# Function to show History

def show_history():
    with open(History_file, "r") as f:
        lines = f.readlines()
        if len(lines)==0:
            print("No History found. Empty Record")
        else:
            print("\n----- Calculation History(Latest Record)----")
            for line in reversed(lines):
                print(line.strip())
                print("---------------------------\n")

# Function to Clear History
def  clear_history():
    with open(History_file, "w") as f:
        pass
    print("\n -----------History Cleared Successfully-------\n")   

# Function to Quit the Program
def quit_program():
    print("\n----------- Ending The Calculator. See You Next Time! --------")
    exit()

# Function to save History in history.txt file

def save_history(entry):
    with open(History_file, "a")as f:
        f.write(f"{entry} \n")
        print("\n------------- History Saved Successfully------------\n)")


# Functions to Perfrom Calculations

def calculate_expression():
    user_input = input("Enter Expression in proper format (For Example: 4 + 9) \n").strip()
    try:
        parts = user_input.split()
        if len(parts)!=3:
            raise ValueError("Invalid Format! Please Use Number format: num_1 operator num_2 (e.g., 4 + 9)")
        num_1 , operator, num_2 = parts
        num_1 = float(num_1)
        num_2 = float(num_2)

        if operator == "+":
            result = num_1 + num_2
        elif operator == "-":
            result = num_1 - num_2
        elif operator == "*":
            result = num_1 * num_2
        elif operator == "/":
            if num_2==0:
                raise ZeroDivisionError("Cannot Divide by Zero!")
            result = num_1 / num_2
        else:
            raise ValueError("Please Use Valid Operator (+, -, *, /)")
        print(f"\n Result : {result}")
        entry = f"{num_1} {operator} {num_2} = {result}"
        save_history(entry)
    except ValueError as v:
        print(f"Error : {v}")
    except ZeroDivisionError as z:
        print(f"Error : {z}")
    except Exception:
        print(f" Error!! Invalid Input. Please Try Again")

# Function to run the Calculator Program
def calculator():
        print("\n--------------Welcome To The Calculator Program--------------\n")
        print("\n--------------Designed by : Mabtoor Mabx-----------------\n")

        while True:
            print("\n------------------Menu------------------")
            print("Choose The Operation You Want To Perform:")
            print("1- Perform Calculation")
            print("2- Show History")
            print("3- Clear History")
            print("4- Quit Program")
            choose = input("Enter Your Choice (1-4): ")

            if choose == "1":
                calculate_expression()
            elif choose == "2":
                show_history()
            elif choose == "3":
                clear_history()
            elif choose == "4":
                quit_program()
            else:
                print("Invalid Choice! Please Try Again.")


# Main Program 
if __name__=="__main__":
    calculator()