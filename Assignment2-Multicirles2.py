from turtle import*
radius=80
numside=360
degree=1
color("green","white")
for i in range(36):
    left(10)
    for y in range(numside):
        forward(2*radius*3.14/numside)
        left(degree)
