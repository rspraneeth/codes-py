from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo)
is_continuing = True
while is_continuing:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message(anything other than alpha won't be ciphered):\n").lower()
    shift = int(input("Type the shift number:\n"))


    def caesar(txt, shf, drx):
        cip = ""
        for i in txt:
            if i in alphabet:
                ind = alphabet.index(i)
                if drx == 'encode':
                    if shf + ind > 25:
                        cip += alphabet[shf + ind - 26]
                    else:
                        cip += alphabet[shf + ind]
                elif drx == 'decode':
                    cip += alphabet[ind - shf]
            else:
                cip += i
        print(cip)


    if shift > 26:
        shift = shift % 26

    caesar(text, shift, direction)

    if input("Do you want to cipher again Y/N ").lower() == 'y':
        is_continuing = True
    else:
        is_continuing = False
        print("tata bye-bye")
