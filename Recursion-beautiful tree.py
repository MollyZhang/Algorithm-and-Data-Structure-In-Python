import turtle
import random

def tree(branchLen,t):
    if branchLen > 5:
        if branchLen < 20:
            t.color("red")
        angle = random.randint(15,40)
        shorter = random.randint(5,20)
        t.forward(branchLen)
        t.right(angle)
        tree(branchLen-shorter,t)
        t.left(2*angle)
        tree(branchLen-shorter,t)
        t.right(angle)
        t.backward(branchLen)
        t.color("green")

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    t.speed(0)
    tree(75,t)
    myWin.exitonclick()

main()