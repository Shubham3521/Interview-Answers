

a_dict = {"x":{"y":{"z":"a"}}}
keys = "z"
 
def iterate(dictionary): 
    for key, value in dictionary.items(): 
        if isinstance(value, dict): 
            iterate(value) 
            continue
    if key==keys:
        print(value)
 
iterate(a_dict)
