import pyautogui as pg
import time


## Functions


def next_item():
    time.sleep(0.1)
    pg.press('tab')
    time.sleep(0.1)


def next_page():
    pg.press('enter')
    time.sleep(7)


def respond_yes():
    pg.press('right')
    pg.press('down', presses=1)
    pg.press('enter')


def respond_no():
    pg.press('right')
    pg.press('down', presses=2)
    pg.press('enter')


def respond_3():
    pg.press('right')
    pg.press('down', presses=3)
    pg.press('enter')


time.sleep(2)

### First page of questions


pg.click(x=131, y=272) # click into the window
time.sleep(0.3)
pg.press('tab',presses=21,interval=0.05)

actions_list_1 = [
    next_item,
    respond_no,
    next_item,
    respond_no,
    next_item,
    respond_yes,
    next_item,
    respond_no,
    next_item,
    respond_no,
    next_item,
    respond_yes,
    next_item,
    respond_no,
    next_item,
    respond_no
]

# Iterate through the list and execute the actions in list_1
for action in actions_list:
    action()

pg.press('tab',presses=28,interval=0.05)



## Additional Questions 1


pg.click(x=203, y=254)
time.sleep(0.1)
pg.press('tab',presses=2)
time.sleep(0.1)
# Create a list of functions representing the actions
actions_list = [
    lambda: press_key('m'),               # Question
    next_item,
    lambda: press_key('y'),               # Question
    next_item,
    lambda: press_key('b'),               # Question
    next_item,
    lambda: press_key('8'),               # Question
    next_item,
    lambda: press_key('0'),
    next_item,
    lambda: press_key('y'),               # Question
    next_item,
    lambda: press_key('n'),               # Question
    next_item,
    lambda: press_key('y'),               # Question
    next_item,
    lambda: type_text('Earlier this year'),
    next_item,
    lambda: press_key('y'),               # Question
    next_item,
    lambda: type_text('acceptable use case'),  # Question
    next_item,
    lambda: press_key('n'),               # Question
    next_item,
    lambda: press_key('n'),               # Question
    next_item,
    lambda: press_key('n'),               # Question
    next_item,
    lambda: press_key('a'),               # Question
    next_item,
    lambda: press_key('n'),               # Question
    next_item,
    lambda: press_key('n'),               # Question
    next_item,
    lambda: press_key('n'),
    next_item,
    lambda: press_key('n'),
    time.sleep(0.1)
]

# Iterate through the list and execute the actions
for action in actions_list:
    action()
time.sleep(0.1)
pg.press('tab',presses=7)
time.sleep(0.1)
next_page() 


## Additional Questions 2


pg.click(x=203, y=254)
pg.press('tab',presses=2)
time.sleep(0.1)
pg.press('i')
next_item()
pg.press('w') #race
next_item()
pg.press('m') #gender
next_item()
next_item()
pg.press('space')
pg.press('tab',presses=7)
time.sleep(0.1)
next_page() # wait for webpage






## Identification questions




pg.click(x=203, y=254)
pg.press('tab',presses=3)
time.sleep(0.1)
pg.typewrite('jn ldsr - mhrbrt') 	# access code
pg.press('tab',presses=3)
time.sleep(0.1)
pg.press('space',presses=2,interval=0.5)
time.sleep(0.1)
pg.press('tab',5)
time.sleep(0.1)
pg.press('space')
time.sleep(0.1)
pg.press('tab',presses=7)
time.sleep(0.1)
next_page()




### Review questions and submit


pg.click(x=203, y=254)
pg.press('tab',presses=10)
time.sleep(0.5)
pg.press('enter') # SUBMIT 
