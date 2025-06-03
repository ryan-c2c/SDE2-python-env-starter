user_string = input('Enter a string. ').lower()

def count_vowels(string):
  #initiliaze count variable
  vowel_count = 0
  for letter in string:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
      #if True
      vowel_count += 1
  #check if any vowel found

  return print(vowel_count)
  """
  if vowel_count == 0:
    print('No vowels found')
  else:
    print(f'Total vowels are : {vowel_count}.')
  """

count_vowels(user_string)