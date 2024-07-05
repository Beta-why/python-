# -*- coding: UTF-8 -*-
#!/usr/bin/python3
#py++ beta1.2.0  written in python  by Creeper_beta
print(">>>py++ beta1.2.0")

import run_time_pyadd as r

print(">>>File directory:")
code_line_len = 1
file_path = input(">>>").replace("\\","/")
with open(file_path,encoding="utf-8") as f:
    for line in f.readlines():
        r.run((line.replace("\n","")),(code_line_len))
        code_line_len+=1
