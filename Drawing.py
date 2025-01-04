# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 20:25:56 2024

@author: zaink
"""


# Import the turtle module
import turtle

import math

# Constants (you can change these)
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 450
WINDOW_TITLE = "String art"



# Set up the screen object

#turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen = turtle.Screen()
screen.title(WINDOW_TITLE)


t = turtle.Turtle()

screen.bgcolor("#c8fff8")




#variables

length=0
string_color="#690a7a"
nail_color="#0a7a6c"

""" user inputing the number of nails that they want"""

num_nail= int(screen.numinput("Nails number","How many nails your art needs?" ))



"""fist nail that """

nail_x1= screen.numinput("X","Where is the X?" )
nail_y1= screen.numinput("Y","Where is the Y?" )
t.color(nail_color)
t.penup()
t.goto(nail_x1, nail_y1)
t.pendown()
t.stamp()

privous_x1, privous_y1= nail_x1,nail_y1

""" loop of the other nails"""

for i in range(num_nail-1):
    
    nail_x= screen.numinput("X","Where is the X?" )
    nail_y= screen.numinput("Y","Where is the Y?" )
    
    
    t.goto(nail_x, nail_y)
    t.pendown()
    t.color(nail_color)
    t.stamp()
    t.color(string_color)
    t.goto(privous_x1,privous_y1)
    
    #calculating the length of the string

    length= math.sqrt((privous_x1 -nail_x)**2 + ( privous_y1-nail_y)**2) +length
    
    privous_x1, privous_y1= nail_x, nail_y 

"""going back to the first nail"""

t.color(string_color)   
t.goto(nail_x1,nail_y1) 
t.color(nail_color)
t.stamp()
length= math.sqrt((privous_x1 -nail_x1)**2 + ( privous_y1-nail_y1)**2) +length
        
    
""" calculating the prices""" 
length= length/32  #converting legth from px to meters
   
string_price= length*0.07 #0.07 price of meter string
nails= num_nail*0.12 #0.12 price of nail price
board = 5
total= string_price+nails+ board


 


""" printing the price on the screen """

x= str(f"${total:.2f}")

t.color("black")
t.penup()
t.goto(-350,-125 )     #move the turtle to the place of writing
t.pendown()

t.write("This is your total price " + x , align="left")




###code ends!!


    


    
    
    

    

