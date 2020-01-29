production = input("Enter the Production: ")
prod_list = production.split('|')
copy_prod_list = [v for v in prod_list]

# def search_for_longest(lst):
#     start = lst[0][0]
#     flag = 0
#     if len(lst) == 1:
#         return start
#     for index in range(1, len(lst)):
#         if  lst[index][0] != start:
#             flag = 1
def getProductions():
    global prod_list, copy_prod_list
    startChar = copy_prod_list[0][0]
    similarProd = []
    for prod in prod_list:
        if prod[0] == startChar:
            similarProd.append(prod)
            copy_prod_list.remove(prod)
    
    similarProd[0:0] = startChar

    return similarProd
length = len(copy_prod_list)
split_prod = []
while length:
    split_prod.append(getProductions())
    length = len(copy_prod_list)

count= 1
root_prod = []
new_prod = {}
for product in split_prod:
    symbol = 'A{}'.format(count)
    count += 1
    start = product.pop(0)
    new_prod[symbol]=[v[1:] for v in product]
    factored_prod = start+symbol
    root_prod.append(factored_prod)

print("New Production: ", new_prod)
print("Main production: ", root_prod)
