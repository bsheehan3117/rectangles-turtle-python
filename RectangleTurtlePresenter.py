import turtle
from Rectangle import Rectangle

def draw_rectangle(t,x,y,width,height,color):
    t.penup()
    t.goto(x,y)
    t.setheading(0)
    t.pendown()
    t.color(color,color)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.end_fill()
    


def draw_rectangles():
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.getscreen().setup(600,600)

    list_rectangles = [Rectangle(-100,100,60,30),Rectangle(-60,120,40,40),\
                       Rectangle(0,100,60,50),Rectangle(20,120,20,20),\
                       Rectangle(100,100,60,30),Rectangle(140,150,40,40)]

    for index in range(0,len(list_rectangles),2):
        #draw first rectangle
        draw_rectangle(t,list_rectangles[index].get_x(),\
                       list_rectangles[index].get_y(),\
                       list_rectangles[index].get_width(),\
                       list_rectangles[index].get_height(),\
                       'red')

        #draw second rectangle
        draw_rectangle(t,list_rectangles[index+1].get_x(),\
                       list_rectangles[index+1].get_y(),\
                       list_rectangles[index+1].get_width(),\
                       list_rectangles[index+1].get_height(),\
                       'green')
        if list_rectangles[index].overlap(list_rectangles[index+1]):
            #draw intersection
            intersect = list_rectangles[index].intersect(list_rectangles[index+1])
            draw_rectangle(t,intersect.get_x(),\
                           intersect.get_y(),\
                           intersect.get_width(),\
                           intersect.get_height(),\
                           'yellow')
 
def draw_random_rectangles():
    import random
    


    list_rectangles = []
    r_colors = []
    colors = ['red','green','blue']
    for index in range(10):
        r = Rectangle(random.randint(-300,300),random.randint(-300,300),random.randint(100,250),random.randint(100,250))
        list_rectangles.append(r)
        c = random.randint(0,len(colors)-1)
        r_colors.append(colors[c])

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.getscreen().setup(800,800)    

    for i in range(len(list_rectangles)):
        #draw rectangle
        draw_rectangle(t,list_rectangles[i].get_x(),\
                       list_rectangles[i].get_y(),\
                       list_rectangles[i].get_width(),\
                       list_rectangles[i].get_height(),\
                       r_colors[i])

    #draw all intersections in yellow
    for i in range(0,len(list_rectangles)):
        for j in range(i+1,len(list_rectangles)):
            if list_rectangles[i].overlap(list_rectangles[j]):
                intersect = list_rectangles[i].intersect(list_rectangles[j])
                draw_rectangle(t,intersect.get_x(),\
                           intersect.get_y(),\
                           intersect.get_width(),\
                           intersect.get_height(),\
                           'yellow')

        

def main():
    draw_rectangles()

if __name__ == "__main__":
    main()
