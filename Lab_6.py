alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Part 1

def vigenere_sq(alphabet):
    print(" ", end="")
    for letter in alphabet:
        print(letter + " ", end="")
    print()

    for row in range(len(alphabet)):
        print(alphabet[row], end="")

        for column in range(len(alphabet)):
            index = (row + column) % len(alphabet)
            print(alphabet[index], end="")

        print()

# Part 2

def letter_to_index(letter, alphabet):
    letter = letter.upper()

    if letter in alphabet:
        return alphabet.index(letter)
    else:
        return -1

def index_to_letter(index, alphabet):
    return alphabet[index]

def vigenere_index(key_letter, plain_letter, alphabet):
    key_index = letter_to_index(key_letter, alphabet)
    plain_letter_index = letter_to_index(plain_letter, alphabet)

    cipher_index = (key_index + plain_letter_index) % len(alphabet)

    return index_to_letter(cipher_index, alphabet)

def encrypt_vigenere(key, plain_letter, alphabet):
    key = key.upper()
    plain_letter = plain_letter.upper()

    encrypted_text = ""
    key_position = 0

    for letter in plain_letter:
        if letter in alphabet:
            key_letter = key[key_position % len(key)]

            encrypted_letter = vigenere_index(letter, alphabet, key_letter)

            encrypted_text += encrypted_letter
            key_position += 1
        else:
            encrypted_letter += letter

    return encrypted_text

vigenere_sq(alphabet)

key = "DAVINCI"
plaintext = "THE EAGLE HAS LANDED"

ciphertext = encrypt_vigenere(key, plaintext, alphabet)

print()
print(f"Keyword: {key}")
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")


