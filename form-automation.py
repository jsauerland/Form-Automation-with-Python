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
next_item()
respond_no() # Question
next_item()
respond_no() # Question
next_item()
respond_yes() # Question
next_item()
respond_no() # Question
next_item()
respond_no() # Question
next_item()
respond_yes() # Question
next_item()
respond_no() # Question
next_item()
respond_no() # Question
next_item()
respond_no() # Question


pg.press('tab',presses=28,interval=0.05)



## Additional Questions 1


pg.click(x=203, y=254)
time.sleep(0.1)
pg.press('tab',presses=2)
time.sleep(0.1)
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