def evento2(): 
    print(1 + 'Manzana') 
    
def evento1(): 
    try: 
        evento2() 
    except TypeError: 
        print('try interno') 
try: 
    evento1() 
except TypeError: 
    print('try externo') 