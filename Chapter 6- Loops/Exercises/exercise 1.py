#ex-1
prompt = "What topping would you like on your pizza?\n"
prompt += "\nEnter 'quit' when you are finished: \n"

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break