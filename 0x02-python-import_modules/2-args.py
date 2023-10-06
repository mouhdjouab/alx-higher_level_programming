#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arry=sys.argv
    if len(arry)==1:
        print("0 arguments.")
    elif len(arry)==2:
        print("1 argument:")
    else:
        print(f"{len(arry)-1} arguments:")
    for i,j in enumerate(arry):
        print(f"{i+1}: {j+1}")
