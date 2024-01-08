import random as r 

# n = r.randint(1, 11)
# guess = None
# count = 1

# while guess != n:
    
#     user_input = int(input('Guess the number between 1 - 10: '))
    
#     if user_input == n:
#         print("Correct! That's the number you were looking for.")
#         break
#     elif user_input < n:
#         print("The number you're looking for is larger.")
#         count = count + 1
#     else:
#         print("The number you're looking for is smaller")
#         count = count + 1
        
# print(f"You tried {count} times.")

# upper_bound = 100
# n = r.randint(1, upper_bound)
# guess = None
# count = 1

# while guess != n:
#     try:
#         guess = int(input(f"Guess the number between 1 and {upper_bound}: "))
#         if guess == n:
#             print(f"Richtig! Das ist die Zahl, die ich gesucht habe. Du hast {count} Versuche gebraucht.")
#             break
#         elif guess < n:
#             print("Die gesuchte Zahl ist größer als deine Vermutung.")
#             count += 1
#         else:
#             print("Die gesuchte Zahl ist kleiner als deine Vermutung.")
#             count += 1
#     except ValueError:
#         print("Das ist keine gültige Zahl. Bitte versuche es nochmal.")

# upper_bound = 100
# n = r.randint(1, upper_bound)
# count = 0

# while True:
#     try:
#         guess = int(input(f"Rate die Zahl zwischen 1 und {upper_bound}: "))
#         count += 1
#         if guess == n:
#             print(f"Richtig! Das ist die Zahl, die ich gesucht habe. Du hast {count} Versuche gebraucht.")
#             break
#         print("Die gesuchte Zahl ist größer" if guess < n else "Die gesuchte Zahl ist kleiner")
#     except ValueError:
#         print("Das ist keine gültige Zahl. Bitte versuche es nochmal.")
        
        
def main(upper_bound=100):
    n, count = r.randint(1, upper_bound), 0
    while True:
        try:
            guess = int(input(f"Rate die Zahl zwischen 1 und {upper_bound}: "))
            count += 1
            if guess == n: break
            print("Zu " + ("hoch." if guess > n else "niedrig."))
        except ValueError: print("Bitte eine Zahl eingeben.")
    print(f"Richtig! Die Zahl war {n}. Versuche: {count}")

if __name__ == "__main__":
    main()