from helpers import alphabet_position, rotate_character

def encrypt (text,key_word):
    encry_text = ""  
    v = 0
    for x in text:
        if x.isalpha():
            y = alphabet_position(key_word[v % len(key_word)])
            encry_text = encry_text + rotate_character(x,y)
            v = v + 1
        else:
            encry_text = encry_text + x    
    return encry_text
def main():
    text = input("Type a message: ")
    print(text)
    key_word = input("What is the key: ")
    print(key_word)
    print(encrypt(text,key_word))
if __name__ == "__main__":
    main()  