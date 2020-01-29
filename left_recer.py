prod = input("Enter the production: ")
symbol = prod.split('-')
productions = symbol[1].split('|')

recursive=[]
non_recur = []
for production in productions:
    if symbol[0] == production[0]:
        recursive.append(production[1:]+'A1')    
    else:
        non_recur.append(production+'A1')

main_prod = 'A -> '+"|".join(non_recur)
derived_prod = 'A1 -> '+"|".join(recursive) + "|eps"

print(main_prod)
print(derived_prod)


