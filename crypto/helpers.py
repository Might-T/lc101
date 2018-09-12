def alphabet_position(letter):
    alphaL="abcdefghijklmnopqrstuvwxyz"
    alphaU="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for cx in letter:
        if cx in alphaL:
            return alphaL.index(cx)
        else:
            return alphaU.index(cx)            

def rotate_character(char,rot):
    alphaL="abcdefghijklmnopqrstuvwxyz"
    alphaU="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if char in alphaL:
        pos_num = alphabet_position(char) + rot
        if pos_num < 26:
            return alphaL[pos_num]
        else:
            return alphaL[pos_num%26]
    elif char in alphaU:
        pos_num = alphabet_position(char) + rot
        if pos_num < 26:
            return alphaU[pos_num]
        else:
            return alphaU[pos_num % 26]            
    else:
        return char

