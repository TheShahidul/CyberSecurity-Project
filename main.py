from encryption_algorithms import caesar_cipher, aes_cipher, vigenere_cipher

# Define available algorithms
algorithms = {
    "Caesar Cipher": caesar_cipher,
    "AES": aes_cipher,
    "Vigenère Cipher": vigenere_cipher
}

def encrypt_flow():
    text = input("Enter your text to encrypt: ")
    while True:
        print("\nAvailable algorithms:")
        for i, algo in enumerate(algorithms.keys(), 1):
            print(f"{i}. {algo}")
        choice = input("Choose an algorithm (enter number): ")
        try:
            choice = int(choice)
            algorithm_name = list(algorithms.keys())[choice - 1]
            algo = algorithms[algorithm_name]
        except (ValueError, IndexError):
            print("Invalid choice. Try again.")
            continue

        key = input(f"Enter key for {algorithm_name}: ")
        text = algo.encrypt(text, key)

        print(f"Cipher Text: {text}")
        again = input("Do you want to encrypt it again? (yes/no): ").lower()
        if again != "yes":
            break
    return text

def decrypt_flow():
    text = input("Enter your cipher text to decrypt: ")
    while True:
        print("\nAvailable algorithms:")
        for i, algo in enumerate(algorithms.keys(), 1):
            print(f"{i}. {algo}")
        choice = input("Choose an algorithm (enter number): ")
        try:
            choice = int(choice)
            algorithm_name = list(algorithms.keys())[choice - 1]
            algo = algorithms[algorithm_name]
        except (ValueError, IndexError):
            print("Invalid choice. Try again.")
            continue

        key = input(f"Enter key for {algorithm_name}: ")
        text = algo.decrypt(text, key)

        print(f"Decrypted Text: {text}")
        again = input("Do you need to decrypt further? (yes/no): ").lower()
        if again != "yes":
            break
    return text

def main():
    print("Welcome to Multi-Level Encryption")
    while True:
        choice = input("\nDo you want to Encrypt or Decrypt? (enter 'e' or 'd', or 'exit' to quit): ").lower()
        if choice == 'e':
            encrypt_flow()
        elif choice == 'd':
            decrypt_flow()
        elif choice == 'exit':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
