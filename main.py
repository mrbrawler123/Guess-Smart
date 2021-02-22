import time
import random
print("GUESS SMART")
time.sleep(2)
print(
    "You will be given some balance. I will think of a number. You have to guess a number. Then, the AI Bot will guess. The difference between the number I thought of and the number you and the AI Bot guessed will be subtracted from both players' balance. The first one to reach zero or go below it, loses. If both reach zero or go below it at the same time, then the one with higher points wins."
)
time.sleep(2)
balance = int(input("Enter the Starting Balance: "))
time.sleep(1)
limit = int(input("Enter the Limit for Numbers Possible: "))
ai_balance = balance
number = 0
possible_numbers = list(range(limit + 1))
while ai_balance > 0 and balance > 0:
	number = random.choice(possible_numbers)
	player_answer = int(input("Enter your guess: "))
	while player_answer > limit or player_answer < 0:
		player_answer = int(input(f"Enter a number from 0 to {limit}: "))
	time.sleep(1)
	ai_answer = random.choice(possible_numbers)
	print(f"AI Bot's Guess: {ai_answer}")
	time.sleep(1)
	print(f"The answer is {number}")
	if player_answer > number:
		player_points = player_answer - number
	if player_answer < number:
		player_points = number - player_answer
	if player_answer == number:
		player_points = 0
	if ai_answer > number:
		ai_points = ai_answer - number
	if ai_answer < number:
		ai_points = number - ai_answer
	if ai_answer == number:
		ai_points = 0
	balance = balance - player_points
	ai_balance = ai_balance - ai_points
	print(f"Your Balance: {balance}")
	time.sleep(1)
	print(f"AI Bot's Balance: {ai_balance}")
if balance > 0:
	print("Congratulations, you have won!")
if ai_balance > 0:
	print("The AI Bot has won!")
if ai_balance < 1 and balance < 1:
	if ai_balance == balance:
		print("It's a draw!")
	if ai_balance > balance:
		print("The AI Bot has won!")
	if balance > ai_balance:
		print("Congratulations, you have won!")