import os
from datetime import datetime

def get_current_datetime():
    return f"{datetime.now().strftime('%d %B %Y, %I:%M %p')}\nChatbot: How else can I assist you?"


def validate_integer_list(input_str):
    try:
        int_list = [int(x) for x in input_str.split(',')]
        return int_list
    except ValueError:
        return None

def remove_duplicates(int_list):
    
    return list(set(int_list))

def generate_prime_numbers(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

def search_chat_history(history, keyword):
    results = [line for line in history if keyword.lower() in line.lower()]
    return results

def save_summary_to_file(commands_count, frequent_command,chat_history):
    filename = f"summary_{datetime.now().strftime('%m%d%Y')}.txt"
    summary = f"Commands Used: {commands_count}\nMost Frequent Command: {frequent_command}\nother history: {chat_history}\n"
    
    # Saving to file
    with open(filename, 'w') as f:
        f.write(summary)
    return filename

def chat():
    chat_history = []
    commands_count = 0
    most_frequent_command = None
    command_counter = {}

    print("Chatbot: Hello! I’m your assistant! How can I help you today?")
    while True:
        user_input = input("User: ").strip()
        chat_history.append(f"User: {user_input}")

        # Check for keyword mismatch
        if user_input.lower() in ["hello", "hi"]:
            print("Hi there! How can I help you today?")
            continue

        elif "date" in user_input.lower() or "time" in user_input.lower():
            print(f"{get_current_datetime()}")
            commands_count += 1
            most_frequent_command = "date/time"
            command_counter["date/time"] = command_counter.get("date/time", 0) + 1
            continue
            

        elif "list operations" in user_input.lower():
            print("Please enter a list of integers (comma-separated, integer):")
            int_list_str = input("User: ").strip()
            chat_history.append(f"User: {int_list_str}")
            int_list = validate_integer_list(int_list_str)

            if int_list is None:
                print("Error: The list must have integers only, separated by commas.")
                continue

            sum_of_list = sum(int_list)
            max_value = max(int_list)
            reversed_list = int_list[::-1]

            print(f"Sum: {sum_of_list}")
            print(f"Maximum: {max_value}")
            print(f"Reversed List: {reversed_list}")
            commands_count += 1
            most_frequent_command = "list operations"
            command_counter["list operations"] = command_counter.get("list operations", 0) + 1

            print("Would you like to remove duplicates? (yes/no)")
            user_response = input("User: ").strip().lower()
            # chat_history.append(f"User: {user_response}")

            if user_response == "yes":
                int_list = remove_duplicates(int_list)
                print(f"Updated List: {int_list}")
                print(f"Sum: {sum(int_list)}")
                print(f"Maximum: {max(int_list)}")
                print(f"Reversed List: {int_list[::-1]}")
                print(f"Chatbot: How else can I assist you?")
            continue

        elif "generate prime" in user_input.lower():
            print("Enter the range (start and end):")
            range_str = input("User: ").strip()
            chat_history.append(f"User: {range_str}")
            range_values = validate_integer_list(range_str)

            if range_values is None or len(range_values) != 2:
                print("Error: Please provide two integers separated by a comma (start and end).")
                continue

            start, end = range_values
            prime_numbers = generate_prime_numbers(start, end)
            chat_history.append(f"Chatbot: Prime Numbers: {prime_numbers}")     
            print(f"Prime Numbers: {prime_numbers}")
            commands_count += 1
            most_frequent_command = "generate prime"
            command_counter["generate prime"] = command_counter.get("generate prime", 0) + 1
            continue

        elif "search history" in user_input.lower():
            print("Enter the keyword to search in chat history:")
            keyword = input("User: ").strip()
            # chat_history.append(f"User: {keyword}")
            
            results = search_chat_history(chat_history, keyword)

            if results:
                print("Found the following lines:")
                for result in results:
                    print(f"   - {result}")
            else:
                print(f"No results found for '{keyword}'")
            commands_count += 1
            most_frequent_command = "search history"
            command_counter["search history"] = command_counter.get("search history", 0) + 1
            continue

        elif "bye" in user_input.lower():
            print(f"Here’s a summary of your session:")
            print(f"   - Commands Used: {commands_count}")
            print(f"   - Most Frequent Command: {most_frequent_command}")

            print("Do you want to save this summary? (yes/no)")
            user_response = input("User: ").strip().lower()
            chat_history.append(f"User: {user_response}")

            if user_response == "yes":
                saved_file = save_summary_to_file(commands_count, most_frequent_command,chat_history)
                print(f"Summary saved to {saved_file}")
            
            print("Bye, have a good day!!")
            break

        else:
            print("Error: Keyword mismatch message - 'Enter correct keyword'")
  
if __name__ == "__main__":
    chat()
