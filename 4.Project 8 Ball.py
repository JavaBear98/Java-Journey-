import random
question = input("Ask me a question: ")
response = random.randint(1, 9)
if response == 1:
   print("Yes - definitely")
elif response== 2:
  print("It is decidedly so")
elif response == 3:
   print("Without a doubt.")
elif response == 4:
   print("Reply hazy, try again.")
elif response == 5:
   print("Ask again later.")
elif response == 6:
   print("Better not tell you now.")
elif response == 7:
   print("My sources say no.")
elif response == 8:
   print("Outlook not so good.")
else:
   print("Very doubtful.")
