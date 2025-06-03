import random as random

def say_something(name):
  greetings = [ 'Hello', 'Hi', 'Hey','Good afternoon','Good morning']
  greeting = random.choice(greetings)
  print(f'{greeting}, {name}!')


  
say_something("Sam")
say_something("Julia")