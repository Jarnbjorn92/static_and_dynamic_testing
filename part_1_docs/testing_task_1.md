### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:

# Only one equals is to asign a value. It should be double equals to check value.
# Else requires a colon
  def check_for_ace(self, card):
    if card.value = 1:
      return True
    else
      return False
   

# No comma between card1 and card2 in function parameters
# Spelling error. Should be def instead of dif
# Card is not defined. Should be "return card1"
# If statement not indented correctly
  dif highest_card(self, card1 card2):
  if card1.value > card2.value:
    return card
  else:
    return card2
  

# Total is unassigned
# Return has to be indented under the 'for' loop before returning
# The 'total' will have to be converted to a string to be concatenated
def cards_total(self, cards):
  total
  for card in cards:
    total += card.value
    return "You have a total of" + total
  
```
