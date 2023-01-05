
# Expense Tracker
## Author: Technopy311

## Main Idea
The idea is to create a tracker for expenses, for that i need to get user input for each expense
where the user can input:
    1- Expense Name.
    2- Amount.
    3- Description.
    4- Date.

Basically I must create a CLi CRUD for the app.

After the user inputs expenses, the app shows all the expenses,
the view should be in a table format and, and at the last row, 
show the total amount of all the expenses.

This app will be CLi based, and then made GUI with Tkinter

To save the expenses,  will use a simple txt file as DB.
and each line will contain 1 expense

The dabatabase file will be saved as a .etdb (expense tracker data base).

## Flow
    When the app initializes, it will check if any database file exists,
    if it does, it will ask the user which db to use, then pass to the mainloop.

    If there's none DB, it will create one by asking the user:
        - Name for the DB.
        - Description for the tracker.
    
    After that, it will pass to the mainloop.

### Main loop
    The main loop will be an infinite loop, that allows the user to access the crud of the designated db,
    this by showing in a menu the 4 options (by using numbers from 1-4).
    Each of these options will execute an specific function of the crud.


### The CRUD

#### Create
    To add a new expense, the function will ask the user:
        - Expense name.
        - Amount.
        - Brief Description.
    
    Then the function will open the DB, count the amount of lines (to create an auto generated ID column)
    an add to the last line the information with the following format:

    id;expense-name;amount;description;


    Data type:
        - id -> int.
        - expense-name -> string.
        - amount -> int (this is because the chilean peso does not use decimals).
        - description -> string.

#### Read

#### Update
#### Delete