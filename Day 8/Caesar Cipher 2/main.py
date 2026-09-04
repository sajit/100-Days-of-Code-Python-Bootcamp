alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text.lower():
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print(f"Here is the encoded result: {cipher_text}")

def encrypt(original_text, shift_amount):
    result = ""
    for char in original_text:
        if char.isalnum():
            result += alphabet[(alphabet.index(char)  + shift_amount)%len(alphabet)]
        else:
            result+=char
    return result

def decrypt(original_text, shift_amount):
    result = ""
    for char in original_text:
        if char.isalnum():
            shifted_position = alphabet.index(char) - shift_amount
            if shifted_position < 0:
                shifted_position += len(alphabet)
            shifted_position %= len(alphabet)
            result += alphabet[shifted_position]
        else:
            result+=char
    return result

#text2 = "If he had anything confidential to say, he wrote it in cipher, that is, by so changing the order of the letters of the alphabet, that not a word could be made out."
#cipher2 = "pm ol ohk hufaopun jvumpkluaphs av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba."
def caesar_cipher(text, shift, choice):
    if choice == "encode":
        cipher = encrypt(original_text=text, shift_amount=shift)
        print(f"Encrypted message: {cipher}")
    elif choice == "decode":
        decrypted = decrypt(original_text=text,shift_amount=shift)
        print(f"Decrypted message: {decrypted}")
    else:
        cipher = encrypt(original_text=text, shift_amount=shift)
        decrypted = decrypt(original_text=cipher,shift_amount=shift)
        print(f"Encrypted message: {cipher} \n Decrypted message: {decrypted}")
caesar_cipher(text=text, shift=shift,choice=direction)




