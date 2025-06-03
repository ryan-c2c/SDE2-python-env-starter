def say_something(name, greeting="Hello"):
  print(f'{greeting}, {name}!')


def catchingUp():
  print("""
  How have you been?
  How’s your family?
  What’s new in your life?      
  """)

def salutations():
  print("""
  It was nice to catch up.
  Take care!
  Goodbye!
    
  """)


#say_something("Sam")
#say_something("Julia","Good afternoon")
#catchingUp()
#salutations()


chitchat=[say_something, catchingUp,salutations]

chitchat[0]("Emma")
chitchat[1]()
chitchat[2]()