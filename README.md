# **Calculator\_With\_Saved\_History\_Using\_Python**

## **📌 Introduction**

The **Calculator With Saved History Using Python** is a simple command-line application that allows users to perform basic arithmetic operations such as addition, subtraction, multiplication, and division.
One of the key features of this project is the ability to **save calculation history** to a file (`history.txt`) and retrieve it later. Users can also clear the history when needed, making it a practical and lightweight tool for everyday calculations.

---

## **✨ Features**

* ✅ Perform basic arithmetic operations: `+`, `-`, `*`, `/`.
* ✅ Handles **invalid input** and **zero division errors** gracefully.
* ✅ **Persistent history storage**: All calculations are saved in a text file (`history.txt`).
* ✅ View the **calculation history** in reverse order (latest first).
* ✅ **Clear history** whenever required.
* ✅ **Interactive menu-driven interface** for easy navigation.
* ✅ Simple and lightweight **Python script** with no heavy dependencies.

---

## **🛠️ Libraries Used**

* **os** → To check and create the `history.txt` file if it does not exist.
* **Built-in Python functions** → For file handling (`open`, `readlines`, etc.), input/output, and basic control flow.

---

## **📂 Project Workflow**

1. **Start the Program**
   The calculator welcomes the user and displays an interactive menu.

2. **Choose an Option from the Menu**

   * **Option 1:** Perform a calculation by entering an expression in the format:
     `number operator number` (Example: `4 + 5`).
   * **Option 2:** View the calculation history (latest entries shown first).
   * **Option 3:** Clear the saved history file.
   * **Option 4:** Quit the program gracefully.

3. **Perform Calculation**

   * Accepts input in proper format.
   * Validates operator and operands.
   * Displays the result and **saves it in the history file**.

4. **Show or Clear History**

   * Users can check previously saved calculations.
   * History can be cleared with one command.

5. **Exit the Program**

   * Ends the session with a friendly message.

---

## **📁 File Structure**

```
Calculator_With_Saved_History_Using_Python/
│
├── calculator.py        # Main Python script
├── history.txt          # Stores calculation history
└── README.md            # Project documentation
```

---

## **🚀 How It Works**

* The script checks for `history.txt` when the program starts.
* If the file does not exist, it creates an empty file.
* Each calculation result is appended to `history.txt` for future reference.
* History can be viewed in reverse order or completely cleared.

---

### ✅ **This project is beginner-friendly and a great example of Python file handling combined with a simple user interface.**

---
