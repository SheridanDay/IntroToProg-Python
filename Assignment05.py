# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# SDay,5.16.2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "C:\\_PythonClass\\Assignment05\\ToDoList.txt"   # An object that represents a file
objFile = None
strTask = "The task"
strPrior = "The priority level" # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strRemove = "" # Task being removed



# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here

objFile = open(strFile, "w")
dicRow = {"Task": "task1", "Priority": "low"}
objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print("\n")  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice == '1'):
        # TODO: Add Code Here
        objFile = open(strFile, "r")
        for row in objFile:
            lstRow = row.split(",")
            dicRow = {"Task": lstRow[0], "Priority": lstRow[1]}
            # print(dicRow)
            print(dicRow["Task"],  dicRow["Priority"], sep = " | ")
        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        strTask = input("Enter a Task: ")
        strPrior = input("Enter a Priority: ")
        dicRow = {"Task":strTask, "Priority":strPrior.strip()}
        lstTable.append(dicRow)
        print("Task added.")
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        strRemove = input("Enter a Task to remove: ")
        for row in lstTable:
            if row["Task"].lower() == strRemove.lower():
                lstTable.remove(row)
                print("Task removed.")
            else:
                print("Task not found!")
        print(lstTable)
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
    # TODO: Add Code Here
        objFile = open(strFile, "w")
        for row in lstTable:
            objFile.write(str(row["Task"] + "," + row["Priority"]) + "\n")
            print("Data saved.")
        continue

    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print(" Task list complete.")
        break
        # and Exit the program
