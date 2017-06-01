my_list = ['item1', 'item2', 'item3', 'item4', 'item5', 'item6', 'item7', 'item8', 'item9', 'item10']

file = open('file.txt', 'w')

for item in my_list:
    file.write(item + '\n')

file.close()

