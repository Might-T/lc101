from helpers import alphabet_position, rotate_character

def encrypt(text,rot):
    encry_text = ""
    for x in text:
        encry_text = encry_text + rotate_character(x,rot)
    return encry_text
#print(encrypt("Hello, World!",5))    

def main():
    text = input("Type a message: ")
    print(text)
    rot = int(input("Rotate by: "))
    print(rot)
    print(encrypt(text,rot))
if __name__ == "__main__":
    main()