alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(plain_text,shift_key):
    cipher_text=""
    for i in plain_text:
        if i in alphabet:
            position=alphabet.index(i)
            new_position=(position+shift_key)%26
            cipher_text+=alphabet[new_position]
        else:
            cipher_text+=i
    print(f"Here is the textafter encryption: {cipher_text}")    
    
def decryption(cipher_text,shift_key):
    plain_text=""
    for i in cipher_text:
        if i in alphabet:
              
          position=alphabet.index(i)
          new_position=(position-shift_key)%26
          plain_text+=alphabet[new_position]
        else:
            cipher_text+=i
    print(f"Here is the textafter decryption: {plain_text}")    
    
Wanna_End=False
while not Wanna_End:

    what_to_do=input("Type 'encrypt' for encryption  Type'decrypt' for decryption:-\n")
    text=input("Type your message\n").lower()
    shift=int(input("Enter shift key\n"))
    if what_to_do=="encrypt":
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do=="decrypt":    
        decryption(text,shift)
    play_again=input("Type'Yes' for continue And 'NO' for Exit\n")
    if play_again=='No':
        Wanna_End=True
        print("Have a nice day! Bye....")