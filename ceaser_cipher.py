def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

print("Welcome to the Caesar Cipher Tool!")

while True:
    mode = input("\nType 'encrypt' to encrypt, 'decrypt' to decrypt, or 'exit' to quit: ").lower()
    if mode == 'exit':
        print("Goodbye!")
        break
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid option. Please try again.")
        continue

    message = input("Enter your message: ")
    shift = int(input("Enter shift key (can be negative): "))

    if mode == 'decrypt':
        shift = -shift  # reverse shift for decryption

    output = caesar_cipher(message, shift)
    print(f"Result: {output}")
