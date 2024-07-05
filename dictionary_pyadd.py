# -*- coding: UTF-8 -*-
#!/usr/bin/python3
variable_list = []
#函数
def find(list,thing):#寻找
    in_it = False
    line = 0
    for i in list:
        if thing in i:
            in_it = True
            return line
        line+=1
    if in_it == False:
        return "not"
#字典
def add(a,b):
    return int(a) + int(b)

def sub(a,b):
    return int(a) - int(b)

def mul(a,b):
    return int(a) * int(b)

def div(a,b):
    return int(a) / int(b)

def divisible(a,b):
    return int(a) // int(b)

def remainder(a,b):
    return int(a) % int(b)

def power(a,b):
    return int(a) ** int(b)
 
def printx(a):
    print(">>>"+str(a))

def create_assignment(variable,thing):
    try:string = '"' in thing
    except:string = False
    v_find_mode = find(variable_list,variable)
    if v_find_mode != "not":
        if string:
            variable_list[v_find_mode][1] = thing.replace('"',"")
        else:
            variable_list[v_find_mode][1] = thing
    else:
        len_list = len(variable_list)
        variable_list.append([])
        variable_list[len_list].append(variable)
        if string:
            variable_list[len_list].append(thing.replace('"',""))
        else:
            variable_list[len_list].append(thing)
