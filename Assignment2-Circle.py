from turtle import*
radius=100
numside=360
degree=1
color("green","yellow")
begin_fill()
for i in range(numside):
    forward(2*radius*3.14/numside)
    left(degree)
end_fill()
    
