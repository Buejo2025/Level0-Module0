import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    Toby45 = turtle.Turtle()
    # Make your turtle's shape 'turtle', .shape('turtle')
    Toby45.shape("turtle")
    # Set your turtle's speed using .speed(2)
    Toby45.speed(8)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    Toby45.color("Blue")
    # Move your turtle forward using .forward(100)
    # TEST    Did your turtle move forward?
    for i in range(4):
        Toby45.forward(100)
    # Move your turtle left or right using .left(90) or .right(90)
        Toby45.right(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    Toby45.goto(20, 60)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    # TEST    Did your turtle draw a circle?
    Toby45.circle(radius=30, steps=38)

    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below
    Toby45.color("Red")
    Toby45.begin_fill()
    Toby45.circle(radius=40, steps=60)
    Toby45.end_fill()
    # Draw 3 more shapes with different fill colors!
    Toby45.color("Orange")
    Toby45.color("Green")
    Toby45.color("Blue")
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
