
import random

options = ["r", "p", "s"]
wins = 0
lost = 0
draw = 0

print("***********************************\nLet's play rock paper and scissors")
print("Just type the first letter of your choice, for example (s) for scissors\n************************************\n")
while True:
    choice = input("Type your choice ").lower()
    computer_pick = options[random.randint(0, 2)]
    if choice == 'q':
        break
    elif choice not in options:
        continue
    elif choice == 'r' and computer_pick == 's':
        wins += 1
        print("""
            _______
        ---'   ____)____
                  _______)
               __________)
              (____)
        ---.__(___)
        """)
    elif choice == 's' and computer_pick == 'p':
        wins += 1
        print("""
             _______
        ---'    ____)____
                   _________)
                  _________)
                 _________)
        ---._____________)
        """)
    elif choice == 'p' and computer_pick == 'r':
        wins += 1
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
    elif choice == 's' and computer_pick == 'r':
        lost += 1
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
    elif choice == 'p' and computer_pick == 's':
        lost += 1
        print("""
            _______
        ---'   ____)____
                  _______)
               __________)
              (____)
        ---.__(___)
        """)
    elif choice == 'r' and computer_pick == 's':
        lost += 1
        print("""
            _______
        ---'   ____)____
                  _______)
               __________)
              (____)
        ---.__(___)
        """)
    else:
        draw += 1
        print("Draw!\nಠ_ಠ")

print("\n*****************************\n"
      f"You won {wins} times, and lost {lost} times, and finally there were {draw} draws\n"
      "*****************************\n")
