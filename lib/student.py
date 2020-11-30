
def lec1_challenge1_implementation() -> str:
    pass

def lec1_challenge2_implementation(x,y) -> int:
    ### TODO 
    result = 0 #inital
    result = x+y
    return result

def hw1_implementation(level):
    result = []
    for i in range(level):
        row = ""
        for j in range(level-i):
            row += " "
        for j in range(i*2+1):
            row += "*"
        result.append(row)
    return result