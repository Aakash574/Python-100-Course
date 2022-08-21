import random


Rock = print()
Paper = print()
Scissors = print()

RSP = ["""
      _______
  ---'   ____)____
            ______)
        __________)
        (____)
---.__(___)
    """, """
      _______
 ---'    ____)____
            ______)
            _______)
            _______)
    ---.__________)
    """, """
            _______
        ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)
        """]
userChoose = int(input("""What do U choose?
1 for Scissors
2 for Paper
3 for Rock
"""))
computerChoose = random.randint(1, 3)
print(
    f"You Choose {userChoose}\n {RSP[userChoose]}\n Computer Choose {computerChoose}\n {RSP[computerChoose]}")

if userChoose == computerChoose:
    print("Draw")
elif userChoose == 1 and computerChoose == 2:
    print("You Win")
elif userChoose == 1 and computerChoose == 3:
    print("You Loose")
elif userChoose == 2 and computerChoose == 1:
    print("You Loose")
elif userChoose == 2 and computerChoose == 3:
    print("You Win")
elif userChoose == 3 and computerChoose == 1:
    print("You Win")
else:
    print("You loose")
