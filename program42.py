#Name: Shahida Hoque
#Email: shahida.hoque03@myhunter.cuny.edu
#Date: April 23, 2020

import turtle
import pandas as pd

def setup(windowTitle):
   
    screen = turtle.Screen()
    screen.title(windowTitle)
    screen.setup(800, 404)
    screen.setworldcoordinates(-180,-90,180,90)

    screen.bgpic("mapNASA.gif")
    t = turtle.Turtle()
    t.pensize(1)
    t.color('red')
    t.penup()

    return t,screen

def animate(t,lat,lon,wind):
    t.goto(lon,lat)
    t.pendown()
    if wind > 157:
        t.pensize(5)
        t.color('red')
    elif wind > 130 and wind < 156:
        t.pensize(4)
        t.color('orange')
    elif wind > 111 and wind < 129:
        t.pensize(3)
        t.color('yellow')
    elif wind > 96 and wind < 110:
        t.pensize(2)
        t.color('green')
    elif wind > 74 and wind < 95:
        t.pensize(1)
        t.color('blue')
    else:
        t.pensize(1)
        t.color('white')
    return(t)

def main():
    """Animates the path of hurricane from file:
    """
    hFile = input('Enter file name: ')
    t, wn = setup(hFile)

    df = pd.read_csv(hFile)
    for index,row in df.iterrows():
        lat = int(row["Lat"])
        lon = int(row["Lon"])
        wind = row["Wind"]
        print(lat,lon,wind)
        animate(t,lat,lon,wind)

if __name__ == "__main__":
    main()
