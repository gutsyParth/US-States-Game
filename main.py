import turtle
import pandas
screen=turtle.Screen()
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

data=pandas.read_csv("50_states.csv")


states=data["state"].tolist()

tim=turtle.Turtle()
tim.hideturtle()
tim.penup()

game_is_on=True
correct=0

while len(states)!=0:
    answer=screen.textinput(title=f"Current Score: {correct}/50",prompt="Enter the name of any US state")
    
    
    answer=answer.title()

    if answer=="Exit":
        missed_states={"Missed States":states}
        data=pandas.DataFrame(missed_states)
        data.to_csv("States Missed")
        break

    if answer in states:
        cord=data[data["state"]==answer]
        x=int(cord.x)
        y=int(cord.y)
        tim.goto(x,y)
        tim.write(answer)
        correct=correct+1
        states.remove(answer)

    if correct==50:
        game_is_on=False
    

screen.exitonclick()



