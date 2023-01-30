mport random
import time
import string

def generate_phrase(length):
    letters = string.ascii_letters + string.punctuation + string.digits + " "
    return "".join(random.choice(letters) for i in range(length))

def speed_test(length):
    print("Starting speed test...")
    phrase = generate_phrase(length)
    print(f"Type the following phrase as fast as you can: {phrase}")
    start_time = time.time()
    user_input = input()
    end_time = time.time()
    total_time = end_time - start_time
    print(f"You typed the sentence in {total_time:.2f} seconds.")

def display_menu():
    print("Speed Typing Test")
    print("-----------------")
    print("1. Start Test (20 characters)")
    print("2. Start Test (40 characters)")
    print("3. Start Test (60 characters)")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice

def main():
    while True:
        choice = display_menu()
        if choice == "1":
            speed_test(20)
        elif choice == "2":
            speed_test(40)
        elif choice == "3":
            speed_test(60)
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
