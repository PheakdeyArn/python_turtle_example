from turtle import *
color('red', 'yellow')
speed(20)
bgcolor('black')
begin_fill()
while True:
    forward(350)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
mainloop()