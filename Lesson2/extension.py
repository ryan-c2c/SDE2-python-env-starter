#import party people file as a nickname
import partyguests as pg

#store imported lists as variables
guest_list = pg.guest_list
rsvp_list = pg.rsvp_list

#ask the user for their name
name = input('What is your name? ').lower()

#check if their name is on the guest list
if name.isalpha in guest_list:
  #if true, check if their name isn't already on the RSVP list
  if name not in rsvp_list:
    #if true, add their name to the RSVP list 
    rsvp_list.append(name)
    print('Thanks! Glad you can make it! ')
    #otherwise, print a message that they've already RSVPd
  else:
    print('You have already RSVPd')
#if the name isn't on the guest list, ask the user how they know you 
elif not name.isalpha():
  name = input('You can only use letters. What is your name? ').lower()

else:
  explain = input('How do we know each other? ') 