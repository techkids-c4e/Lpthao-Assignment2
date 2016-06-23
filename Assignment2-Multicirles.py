from turtle import*
radius=50
numside=360
degree=1
color("green","white")
for i in range(6):
    left(60)
    for y in range(numside):
        forward(2*radius*3.14/numside)
        left(degree)
