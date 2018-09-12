def get_initials (fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # TODO your code here  
    ini_0 = fullname[0]
    initials = ini_0 
    val = " "
    
    char_count = 0
    for i in fullname:
        if i == val:
            char_count += 1
    
    if char_count == 1:
        ini_num = fullname.index(" ") + 1
        ini_1 = fullname[ini_num]
        initials = ini_0 + ini_1

    elif char_count % 2 == 0:
        for char in fullname:    
            if char == val:
                ini_num = fullname.index(" ") + 1
                ini_1 = fullname[ini_num]
                x = fullname.rfind(" ") + 1
                ini_2 = fullname[x]
                initials = ini_0 + ini_1 +ini_2
  
    return initials    
    

def main (): 
    fullname = input("What is your name? ")
    initials = get_initials(fullname)
    new_ini = initials.upper()    
    print ("The initials of",fullname,"are", new_ini)

if __name__ == "__main__":
    main()
