# Automating a form with Python

While practicing data analysis and programming, there was a particular form that I needed to complete very often. This took a small amount of time (approx 5-10 mins), but multiplied by the number of times I was required to fill it out, became a huge process. 

So to save time, I automated it with Python using the package PyAutoGUI

#### Version 1 - form-automation-version-1.0.py

This was the initial version of the script. This was my first pass at the script, and admittedly, was a relic of a much older script I had used years prior when I barely knew any python. 

#### Version 2 - form-automation-version-1.1.py

This second version was the original, initial version of the automation script in Python. It was a major step up above the previous one due to the addition of functions that saved space, and drastically increased code readability. 

```
pg.press('m') # Question
next_item()
pg.press('y') # Question
next_item()
pg.press('b') # Question
next_item()
pg.press('8') # Question
next_item()
pg.press('0')
next_item()
pg.press('y') # Question
next_item()
pg.press('n') # Question
next_item()
pg.press('y') # Question
next_item()
pg.typewrite('Earlier this year')
next_item()
pg.press('y') # Question
next_item()
pg.typewrite('acceptable use case') # Question
next_item()
pg.press('n') # Question
next_item()
pg.press('n') # Question
next_item()
pg.press('n') # Question
next_item()
pg.press('a') # Question
next_item()
pg.press('n') # Question
next_item()
pg.press('n') # Question
next_item()
pg.press('n') 
next_item()
pg.press('n')  
time.sleep(0.1)
pg.press('tab',presses=7)
time.sleep(0.1)
next_page()
```

#### Version 3 - form-automation-version-1.2.py

This second version was included many enhancements, such as a list that I could loop through, which made the code a lot more readable. Anytime the script broke or something was out of place, or I needed to simply add extra steps, this made it a LOT EASIER. Adding the enhancements saved about 30% additional time, and even saved me from making a couple of errors. I also added some extra fancy things into it like lambdas because functionally, they just work a lot better. 

```
actions_list = [
    lambda: press_key('m'),               # Question
    next_item,
    lambda: press_key('y'),               # Question
    next_item,
    lambda: press_key('b'),               # Question
    next_item,
    lambda: press_key('8'),               # Question
    next_item,
```
