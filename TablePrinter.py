tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
             
"""
This will print the table like:

   apples Alice  dogs
  oranges   Bob  cats
 cherries Carol moose
   banana David goose

"""
   
def print_table(table):
    #Reading the table sideways from up to down then right to left
    for x in range(len(table[0])):
        for y in range(len(table)):
            #Put the spacing based on largest value in column
            print(table[y][x].rjust(longest_word_list[y], ' '), end=' ')
        print()
        
#Find the largest word in column of an nested list
#then put value in list
def longest_word(table):
    for y in table:
        max_word = 0
        for x in table[table.index(y)]:
            lenght = len(x)
            if(lenght > max_word):
                max_word = lenght
        #Save the largest word value for each column
        longest_word_list.append(max_word)
        
#Save the largest word value for each column
longest_word_list = []

#Find the largest word in column of an nested list
longest_word(tableData)

print_table(tableData)
