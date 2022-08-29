# 1.
# Question 1
# In this scenario, two friends are having dinner at a restaurant. I got $47.28 on my bill. After adding a 15% tip for the service, the two friends decide to split the amount evenly. Calculate the tip and the total amount you need to pay, and the amount that each friend will have to share, and print the message 'Each person needs to pay: ' and the resulting value after it.
# bill = 47.28
# tip = bill * 0.15
# total = bill + tip
# share = total / 2
# print("Each person needs to pay:", "$" + format(share, ",.2f")) Formatado mas não é aceito como resposta correta
bill = 47.28
tip = bill * 0.15
total = bill + tip
share = total / 2
# Resposta que é aceita como correta
print("Each person needs to pay:" + f"{share}")


# 2.
# Question 2
# This code is supposed to take two numbers, divide one into the other, and display the result on the screen so that the result is 1. There is an error in the code. Find and correct errors so that the output is accurate.
numerator = 10
denominator = 10
result = numerator / denominator
print(round(result))

# 3.
# Question 3
# Combine variables to 'How do you like Python so far?' (How is Python so far?) Please indicate the sentence:
word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"

print(f'{word1} {word2} {word3} {word4} {word5} {word6} {word7}')

# 4.
# Question 4
# This code should display '2 + 2 = 4' on the screen, but there is an error. Find and correct errors in your code to ensure that the output is accurate.
print("2 + 2 = " + str(2 + 2))
