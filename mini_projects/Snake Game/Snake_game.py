"""Snake game using turtle"""
import turtle
import time
import random

#make a delay function
delay=0.1

#make segment for body
segments=[]

#setup the screen
wn=turtle.Screen()

#give the title to it
wn.title("MY Snake game")

#set the background color
wn.bgcolor("green")

#set up the window size
wn.setup(width=600,height=600)

#turn off the animation
wn.tracer(0)

#create the head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction="stop"

##functions to move
def move():
    if (head.direction == "up"):
        y=head.ycor()
        head.sety(y+20)
    elif (head.direction == "down"):
        y=head.ycor()
        head.sety(y-20)
    elif (head.direction == "left"):
        x=head.xcor()
        head.setx(x-20)
    elif (head.direction == "right"):
        x=head.xcor()
        head.setx(x+20)    

def go_up():
    if(head.direction!="down"):
        head.direction="up"

def go_down():
    if(head.direction!="up"):    
        head.direction="down"

def go_left():
    if(head.direction!="right"):
        head.direction="left"

def go_right():
    if(head.direction!="left"):
        head.direction="right"        

#main key bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

#making the snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#create a scoring method
pen = turtle.Turtle()
pen.speed(0)
pen.shape("circle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score : 0 , High Score : 0",align="center" , font=("Courier",24,"normal"))

#variables for score
score=0
high_score=0

#main game loop
while True:
    wn.update()
    #check for overshooting from cornesr
    if(head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290):
        time.sleep(1)
        score=0
        pen.clear()    
        pen.write("Score: {}  high_score: {}".format(score,high_score),align="center" , font=("Courier",24,"normal"))
        head.goto(0,0)
        head.direction='stop'
        
        #send the segmesnts away
        for segment in segments:
            segment.goto(1000,1000)
        
        #empty the segments list
        segments.clear()
    
    #move the food to a random spot
    if(head.distance(food)<20):
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
    
        #make a new segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
        #add score
        score+=10
        if(high_score<score):
            high_score=score
        pen.clear()    
        pen.write("Score: {}  high_score: {}".format(score,high_score),align="center" , font=("Courier",24,"normal"))    
    
    #mave the segments in reverse order
    for i in range(len(segments)-1,0,-1):
        x=segments[i-1].xcor()
        y=segments[i-1].ycor()
        segments[i].goto(x,y)
        
    if(len(segments)>0):
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y) 
    move()
    
    #checking for collision with the body
    for segment in segments:
        if (head.distance(segment)<20):
            time.sleep(1)
            head.goto(0,0)
            head.direction='stop'
            for i in segments:
                i.goto(1000,1000)
            score=0    
            segments.clear()  
            pen.clear()    
            pen.write("Score: {}  high_score: {}".format(score,high_score),align="center" , font=("Courier",24,"normal"))
    
    time.sleep(delay)
wn.mainloop()