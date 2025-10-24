# TablePrinter.py

**Code Analysis**

The provided Python code is designed to print a table in a specific format, with each row printed sideways from top to bottom and then left to right. The table is defined as a list of lists, where each inner list represents a row in the table.

**Key Functions**

The code consists of two main functions:

1. `print_table(table)`: This function takes a table as input and prints it in the desired format. It uses two nested loops to iterate over the table, printing each element with the correct spacing based on the length of the longest word in each column.
2. `longest_word(table)`: This function finds the longest word in each column of the table and stores the maximum length in a separate list (`longest_word_list`). This list is used to determine the correct spacing for each element in the `print_table` function.

**Additional Variables**

The code uses two additional variables:

1. `tableData`: A list of lists representing the table