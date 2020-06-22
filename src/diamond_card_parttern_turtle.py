from turtle import *

fillcolor( 'darkgreen' )
speed(20)

side = 5
distance = 50

begin_fill()
for i in range(50 * side):
    #   distance += 20
    forward(distance)
    right(2 * 360.0 / side - 1)
    distance += 5

end_fill()
mainloop()