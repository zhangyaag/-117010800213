
# coding: utf-8

# In[1]:


import turtle
turtle.setup(960,550,120,120)
turtle.penup()
turtle.fd(-320)
turtle.pendown()
turtle.pensize(20)
turtle.pencolor("seashell")
turtle.seth(-55)
for i in range(5):
    turtle.circle(55,90)
    turtle.pencolor("peru")
    turtle.circle(-55,80)
    turtle.pencolor("wheat")
turtle.circle(55,95/2)
turtle.fd(55)
turtle.circle(20,180)
turtle.pencolor("green")
turtle.fd(45*2/3)

