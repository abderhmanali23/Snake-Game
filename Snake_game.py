from turtle import *
from collections import deque
import keyboard
from random import randint
import time 
 
s = Screen()
global maxgamecsore
maxgamescore = [0]
 
def final():    # recall function
    s.clear()
    main()
 
def main(lst = maxgamescore):
    s.title("Snake Game")    # Screen setup 
    s.setup(1500,750)
    s.tracer(0)
    s.bgcolor("light blue")

    t = Turtle()     # The head of the snake
    t.color("black","green")
    t.shape("turtle")
    t.shapesize(1)
    t.up()
    t.speed(8)
 
 # Some functions to make it easy ....

    def ToRight():
        now = int(t.heading())
        if now == 90:
            t.right(90)
        elif now == 270:
            t.left(90)
 
    def ToLeft():
        now = int(t.heading())
        if now == 90:
            t.lt(90)
        elif now == 270:
            t.rt(90)
 
    def ToUp():
        now = int(t.heading())
        if now == 180:
            t.rt(90)
        elif now == 0:
            t.lt(90)
 
    def ToDown():
        now = int(t.heading())
        if now == 180:
            t.lt(90)
        elif now == 0:
            t.rt(90)
    
    def writes(string , position1 , font , align1 = "center"): # To write any thing just give it the sting and position 
        wr = Turtle()
        wr.hideturtle()
        wr.up()
        wr.goto(position1)
        wr.write(string , align= align1 , font = font) 
        return wr

    def pause(): # To pause and unpause the game when the gamer want

        while True:
            if keyboard.is_pressed("Space"):  
                break
            elif keyboard.is_pressed("BackSpace"):
                s.bye()
 
            time.sleep(0.1)
 
    # --------- Keys onpress setup -------

    onkeypress(ToLeft,"Left")
    onkeypress(ToRight,"Right")
    onkeypress(ToUp,"Up")
    onkeypress(ToDown,"Down")
    onkeypress(pause,"Escape")

    s.listen()
    # ------------------------------------- #
    
    def start(): # Start Screen setup 

        t.write("                                             Click Enter to play \n\n "
                +"                                  Play with UP , Down , Left , Right \n\n"
                +"Esc for pausing , Space for unpausing , Backspace for end program",align="center" , font=("Arial" , 33 ,"bold"))
        
        onkeypress(play,"Return") # on press enter it will start the game
    # -----------------------------------------------------------------------#
    def new_piece_of_tail(pos): # To make a new piece of tail 

        s =  Turtle("circle")
        s.hideturtle()
        s.color("black","light green")
        s.speed(100)
        s.shapesize(1)
        s.up()
        s.goto(pos)
        s.showturtle()
        return s
    # ----------------------------------------------------------#
    def food_move(f, lst, x = 0 , y = 0 ): # To move the food to the new position 
        x , y = randint(-640,640),randint(-290,240)
        
        while True: # while loop to make the food away from blocks
            for i in lst:
                if check((x,y),i,False): # Check function comes next  
                    x , y = randint(-640,640),randint(-290,240)
                    break
            else:
                 break        
        f.goto(x ,y)
        return(x , y)
    # ----------------------------------------------------------------#
    def check(pos , pos1 , food = True ):# food = True if it food otherwise False 
        # Give it two positions head and food or block 
        # It helps fiding if the head is on food \ block or not 

        if not food:
            if abs(pos[1] - pos1[1]) < 19 and  abs(pos[0] - pos1[0]) < 109 :
                return True
            else:
                return False
 
        return True if abs(pos- pos1) < 20 else False
    # ------------------------------------------------------------- #
    def boarder(): # To make Game screen
        border = Turtle()
        border.up()
        border.pensize(12)
        border.hideturtle()
        border.goto(-650,250)
        border.down()
        for i in range(4):
            if i % 2 :
                border.fd(550)
                border.rt(90)
            else:
                border.fd(1300)
                border.rt(90)
    # ----------------------------------------------------------# 
    def blocks_body(n,positions): # To make a block on given position 
        n = Turtle()
        n.up()
        n.shape("square")
        n.shapesize(1 , 10)
        n.goto(positions)
    # --------------------------------------------------------------#
    def makes_blocks(): # Make block position and give it to block_body function
        dielst = []
        lnx = 0
        lny = 100
        for i in range(4):
            if i % 2: 
                lnx -= 100
                lny -= 40
            x = 550 - lnx 
            y = 250 - lny
            lnx += 433
            lny += 150
            dielst.append((x,y))
            blocks_body(i , (x ,y))
        return dielst
    # ------------------------------------------------------------#
    def Currentscore(score): # Shows Current Score
        score_now = writes(f"Current score : {score}",(-550,260),("Arail",20,"bold"))
        return score_now
    # --------------------------------------------------------------#
    def maxscore(lst): # Shows the maximum score of the gamer 
        mx = max(lst)
        max_score = writes(f"Max score : {mx}",(550,260),("Arail",20,"bold"))
        return max_score
    # --------------------------------------------------------------#
    def play(lst = lst):
        t.clear() # To delete start screen text

        writes("Esc for pausing , Enter for ending the game",(0 , 260),("Arial",22,"bold"))
        boarder() # Show the boarder on screen 

        maxscore(lst) # Show max score
        
        current_score = Currentscore(0) # Show the current position with value 0

        onkeypress(s.bye,"Return") # Make the enter click to end the game 

        dielst = makes_blocks() # Make the list of block's position 

        positions = deque() # list of head's positions that will be followed by tail
        positions.append(t.position()) # append the start value os head

        tail_pieces = [new_piece_of_tail(positions.popleft())] # make the first piece of tail 
        # ------ food turtle -------#
        f = Turtle("square")
        f.shapesize(.6)
        f.speed(100)
        f.up()
        food = food_move(f,dielst)
        #----------------------------#
        l = 0.07 # start speed of snake
        score = 0

        while True: # Game loop
            pos = t.position()
            in_block = False

            for i in dielst: # check if the head on block or not  
                in_block = check(pos,i ,False)

                if in_block == True:
                    break

            # if snake eating himself or it is on one block or out of boarders then hard luck 
            if pos in positions or in_block or abs(int(pos[0])) >= 650 or int(pos[1]) <= -300 or int(pos[1]) >= 250  :
                writes("        Game Over !! \n\n"
                           +"Click left Shift to replay" ,(-10,-50) ,font=("Arial",50,"bold"))
 
                break
 
            positions.append(pos) # if not append the current position to the deque

            for i in range(len(tail_pieces)): # Make every piece starts with the last piece to move to the next position 
                tail_pieces[i].goto(positions[i])
 
            if check(t.position(),food) : # if head's position == food position 
                tail_pieces.append(new_piece_of_tail((positions[0]))) # make a new piece of tail 
                food = food_move(f,dielst) # mave the food to the next position  

                score += 1       # increase the current score 
                maxgamescore .append(score)    # append the new score to maxscore list

                current_score.clear()      
                current_score = Currentscore(score)   # To show the new score

                if l > 0.01 :  # increase the speed 
                    l -= 0.005

            else:  # if it is not eating .. so just remove the first positon from the left
                positions.popleft()

            t.fd(10)    # snake step
            s.update()
            time.sleep(l)
 
    onkeypress(final,"Shift_L")  # make left shift to restart the game
    start()
 
main()
done()