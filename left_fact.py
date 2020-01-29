productions = input("Enter the Production: ")
prod_list = productions.split('|')
copy_prod_list = [v for v in prod_list]
main_prod = {}
no_match = []

def getProductions(production):
    global main_prod, copy_prod_list, no_match
    production = sorted(production)
    print(production)
    if len(production)<= 1:
        return
    start = production[0][0]
    prod_dict = {}

    similar = []
    print(similar)
    print(start)
    print("Prod before for -> ",production)
    for prod in production:
        print("Prod - > ",prod)
        print("prod[0] == start -> ",prod[0] == start)
        if prod[0] == start:
            similar.append(prod[1:])
            print("Before remove ",production)
            copy_prod_list.remove(prod)
            print("After remove ",production)
        else:
            no_match.append(prod + " | ")
    
    if len(similar) >= 2:
        prod_dict[start] = similar
        main_prod.update(prod_dict)
    print(similar)
    print("MainProd = ", main_prod)
    
    print(copy_prod_list)
    getProductions(copy_prod_list)

def get2ndProd(prod, start):
    global main_prod
    prod = sorted(prod, reverse=True)
    print("Production -> ",prod)
    new_prod=[]
    mini_prod = {}
    similar=[]
    never_enter = []
    startChar = prod[0][0]

    for p in prod:
        if p[0] == startChar:
            similar.append(p[1:])
        else:
            never_enter.append(p)
    if len(similar) == 1:
        new_prod = prod
        print(new_prod)
        print(mini_prod)
        
    elif len(similar) >= 2:
        mini_prod[startChar] = similar

        new_prod.append(mini_prod)
        if len(never_enter) >= 1:
            new_prod.extend(never_enter)
        print("never enter prod -> ", never_enter)
        print("Elif new Prod", new_prod)
        print("Elif mini prod", mini_prod)

    main_prod[start] = new_prod

getProductions(prod_list)
for key, value in main_prod.items():
    get2ndProd(value, key)
print(main_prod)


final_production = []
count=1
production_list = []
for key,values in main_prod.items():
    final_production.append(key+'A{}'.format(count)+"|")
    flag = 0
    for prod in values:
        if type(prod) is not str:
            flag = 1
    if flag == 0:
        # count += 1
        A1 = "A{}".format(count)+"-> "+"| ".join(values)
        production_list.append(A1)
    
    elif flag == 1:
        # count += 1
        A2 = 'A{}'.format(count)+" -> "
        for prod in values:
            if type(prod) is str:
                A2 += " | "+prod + " | "
            if type(prod) is dict:
                A3=''
                for key, value in prod.items():
                    count += 1
                    A2 += key +"A{}".format(count)
                    A3 += "A{} -> ".format(count) + "| ".join(value)
                production_list.append(A3)    
        production_list.append(A2)
    count += 1
final_production.extend(no_match)
print("A -> ", end='')
for item in final_production:
    print(item,end='')
print()
for item in production_list:
    print(item)