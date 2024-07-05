# -*- coding: UTF-8 -*-
#!/usr/bin/python3

import dictionary_pyadd as d

variables = d.variable_list
#解释库
codes_interpret_function = [[1,"printx","print"],[2,"create_assignment","="]]
codes_interpret_code_function = [d.printx,d.create_assignment]

codes_interpret_operation = [[2,"add","+","addition"],[2,"sub","-","subtraction"],\
                          [2,"mul","*","multiplication"],[2,"div","/","division"],\
                            [2,"divisible","//"],[2,"remainder","%"],[2,"power","**"],]
codes_interpret_code_operation = [d.add,d.sub,d.mul,d.div,d.divisible,d.remainder,d.power]


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
    
def parse_bracket(program):#编译器
    list = program.split('"')
    if len(list) != 1:
        list.pop()  
    return list
    
def parse_space(program):
    return program.split()


def f_s_function(function_find_mode,code_run_list):
    #判断函数需要的输入数量
    try:f_operation_find_mode = find(codes_interpret_operation,code_run_list[1])
    except:pass
    try:variable_find_mode = find(variables,code_run_list[1])
    except:pass
    try:s_operation_find_mode = find(codes_interpret_operation,code_run_list[2])
    except:pass
    if f_operation_find_mode != "not":
        code_run_s = "operation"
    elif variable_find_mode != "not":
        code_run_s = "variable"
    elif s_operation_find_mode != "not":           
        code_run_s = "s_operation"
    else:
        code_run_s = "error"
    #判断是否为f_operation函数
    if code_run_s == "operation":
        code_run_input = f_operation_interpret(code_run_list[1:],f_operation_find_mode)
    #判断是否为变量
    elif code_run_s == "variable":
        code_run_input = variables[variable_find_mode][1]
    #判断是否为s_operation函数
    elif code_run_s == "s_operation":
        code_run_input = s_operation_interpret(code_run_list[1:],s_operation_find_mode)
    return code_run_input

def o_v_mode(code_run_list):
    try:f_t_o_find_mode = find(codes_interpret_operation,code_run_list[2])
    except:pass
    try:s_t_o_find_mode = find(codes_interpret_operation,code_run_list[3])
    except:pass
    try:v_find_mode = find(variables,code_run_list[3])
    except:pass
    try:code_run_input2 = f_operation_interpret(code_run_list[2:],f_t_o_find_mode)
    except:pass
    try:code_run_input2 = s_operation_interpret(code_run_list[2:],s_t_o_find_mode)
    except:pass
    try:code_run_input2 = variables[v_find_mode][1]
    except:pass
    return code_run_input2

#初始函数
def run(program,code_line_len):
    #跳过空格
    if program == "":
        return
    #编译函数
    if len(parse_space(program)) != 1:
        string_mode =  False
    else:
        string_mode = True
    if string_mode:
        code_run_list = parse_bracket(program)
        f_function_find_mode = find(codes_interpret_function,code_run_list[0])
    else:
        code_run_list = parse_space(program)
        f_function_find_mode = find(codes_interpret_function,code_run_list[0])
    #运行函数
    if f_function_find_mode != "not":
        f_function_run_mode = []
        f_function_run_mode.append(True)
        f_function_run_mode.append(codes_interpret_function[f_function_find_mode][0])
        function_interpret(code_run_list,string_mode,f_function_find_mode,f_function_run_mode)
    else:
        s_function_find_mode = find(codes_interpret_function,code_run_list[1])
        if s_function_find_mode != "not":
            f_function_run_mode = []
            f_function_run_mode.append(False)
            f_function_run_mode.append(codes_interpret_function[s_function_find_mode][0])
            function_interpret(code_run_list,string_mode,s_function_find_mode,f_function_run_mode)
        else:
            f_operation_find_mode = find(codes_interpret_operation,code_run_list[0])
            s_operation_find_mode = find(codes_interpret_operation,code_run_list[0])
            #报错程序
            if f_operation_find_mode == "not" and\
                s_operation_find_mode == "not" and code_run_list[0] != "#":
                print(">>>Unknow code 未知代码")
                print(">>>line="+str(code_line_len),"'"+code_run_list[0]+"'")
                quit()

#函数解释器
def function_interpret(code_run_list,string_mode,function_find_mode,run_mode):
    #获得运行函数
    code_run_f = codes_interpret_code_function[function_find_mode]
    code_run_mode = codes_interpret_function[function_find_mode][0]
    if code_run_mode == 1:
        #判断第二位是否为函数
        if string_mode == False:
            code_run_input = f_s_function(function_find_mode,code_run_list)     
        else:
            code_run_input = code_run_list[1]
    elif code_run_mode == 2:
        if run_mode[0]:
            code_run_input1 = code_run_list[1]
            if len(code_run_list) == 3:
                code_run_input2 = code_run_list[2]
            else:
                code_run_input2 = o_v_mode(code_run_list)
        else:
            code_run_input1 = code_run_list[0]
            if len(code_run_list) == 3:
                code_run_input2 = code_run_list[2]
            else:
                code_run_input2 = o_v_mode(code_run_list)
    #运行函数
    if code_run_mode == 1:
        code_run_f(code_run_input)
    elif code_run_mode == 2:
        code_run_f(code_run_input1,code_run_input2)                      

#f运算字符解释器
def f_operation_interpret(code_run_input,find_mode):
    #获得运行函数
    code_run = codes_interpret_code_operation[find_mode]
    try:f_v_find_mode = find(variables,code_run_input[1])
    except:pass
    try:s_v_find_mode = find(variables,code_run_input[2])
    except:pass
    if f_v_find_mode == "not":
        f_code_run_input = code_run_input[0]
    else:
        f_code_run_input = variables[f_v_find_mode][1]
    if s_v_find_mode == "not":
        s_code_run_input = code_run_input[2]
    else:
        s_code_run_input = variables[s_v_find_mode][1]
    return code_run(f_code_run_input,s_code_run_input)

#s运算字符解释器
def s_operation_interpret(code_run_input,find_mode):
    #获得运行函数
    code_run = codes_interpret_code_operation[find_mode]
    try:f_v_find_mode = find(variables,code_run_input[0])
    except:pass
    try:s_v_find_mode = find(variables,code_run_input[2])
    except:pass
    if f_v_find_mode == "not":
        f_code_run_input = code_run_input[0]
    else:
        f_code_run_input = variables[f_v_find_mode][1]
    if s_v_find_mode == "not":
        s_code_run_input = code_run_input[2]
    else:
        s_code_run_input = variables[s_v_find_mode][1]
    return code_run(f_code_run_input,s_code_run_input)
