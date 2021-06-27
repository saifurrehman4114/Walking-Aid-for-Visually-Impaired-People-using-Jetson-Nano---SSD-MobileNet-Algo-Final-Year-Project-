import board
import digitalio
import os 

button = digitalio.DigitalInOut(board.D4)
button.direction = digitalio.Direction.INPUT
# use an external pullup since we don't have internal PU's
button.pull = digitalio.Pull.UP

while True:
   print(button.value) # light when button is pressed!
 
