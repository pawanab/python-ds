import turtle
import calendar as cal


def square():
    new_turtle = turtle.Turtle()
    new_turtle.forward(100)
    new_turtle.right(90)
    new_turtle.forward(100)
    new_turtle.right(90)
    new_turtle.forward(100)
    new_turtle.right(90)
    new_turtle.forward(100)


if __name__ == "__main__":
    # square()

    # print(cal.weekheader(4))
    # print()

    print(cal.month(2020, 5, 3, 1))
    print()
    
    # array of month
    # for i in range(1, 12):
    #     print(cal.monthcalendar(2020, i))
    #     print()