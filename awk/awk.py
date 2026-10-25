#!/usr/python3 

def empty_line(line : str):
    line = line.strip()
    return line == ""


def awk(file: str , idx: int , fs:str = " ") -> list:
    col = []
    with open(file,"r") as f :
        data = f.readlines()
    
    for line in data:
        if not empty_line(line) :
            l = line.strip()
            parts = l.split(fs)
            if len(parts) >= idx:
                col.append(parts[idx - 1])
        else:
            col.append(line)
    
    return col

