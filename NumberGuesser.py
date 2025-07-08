import random
print("***Welcome to number guesser game!***")
print("To exit the game enter -1")


r = random.randint(0,100)
number = 101
step = 0

while number != r:
  try:
        number = int(input("Guess a number between 0 and 100: "))
  except ValueError:
        print("Invalid input. Please enter a whole number.")
        continue


  if number == -1:
        print("Exiting game. Thanks for playing!")
        break

  if number<0 or number>100:
    print("Invalid number")
    continue

  step += 1
  if number == r:
    print(f"You won after {step} steps")
  else:
    if number > r:
      print("too high!!","Try a number less than ", number )
    else:
      print("too low!!", "Try a number greater than ", number)


print(f"True number is {r}")