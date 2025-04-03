# create two lists of items
# create two lists with a ID so line items can be paired
# print the two lists as a table
# add a new item and sort the lists
# create a test document with the lists (up to you 2 files or one)
# read from the lists
# edit lines and write to lists

Col_1 = ["inshallah", "astagfirullah", "mahsallah"]
Col_2 = ["quran", "pork", "islam"]


print("| Col_1 | Col_2 |")
print("|-------|-------|")
for i in range(len(Col_1)):
    print(f"| {Col_1[i]} | {Col_2[i]} | ")


new_item_1 = input("Enter a new item for Col_1: ")
new_item_2 = input("Enter a new item for Col_2: ")
Col_1.append(new_item_1)
Col_2.append(new_item_2)
Col_1.sort()
Col_2.sort()





