from random import randint

SEA=' '
LAND='+'
CITY='O'
AIRPORT='='
LAUNCHER='^'
DESTROYED='X'

def create_map(size,land_count,city_count,airport_count,launcher_count):
    land_map=[[SEA]*size for i in range(size)]
    create_land(land_map,size,land_count)
    create_cities(land_map,size,city_count)
    create_airports(land_map,size,airport_count)
    create_rocket_launchers(land_map,size,launcher_count)
    return land_map

def create_land(land_map,size,land_count):
    i=0
    while i<land_count:
        x=randint(1,size-4)
        y=randint(1,size-4)
        x1=x
        while x1<x+randint(1,3):
            y1=y
            while y1<y+randint(1,3):
                land_map[x1][y1]=LAND
                y1+=1
            x1+=1
        i+=1
    return land_map

def create_cities(land_map,size,city_count):
    i=0
    while i<city_count:
        x=randint(1,size-2)
        y=randint(1,size-2)
        if land_map[x][y]==LAND:
            land_map[x][y]=CITY
            i+=1
    return land_map

def create_airports(land_map,size,airport_count):
    i=0
    while i<airport_count:
        x=randint(1,size-2)
        y1=randint(1,size-4)
        y2=y1+1
        y3=y2+1
        if land_map[x][y1]==LAND and land_map[x][y2]==LAND and land_map[x][y3]==LAND:
            land_map[x][y1]=AIRPORT
            land_map[x][y2]=AIRPORT
            land_map[x][y3]=AIRPORT
            i+=1
    return land_map

def create_rocket_launchers(land_map,size,launcher_count):
    i=0
    while i<launcher_count:
        x=randint(1,size-2)
        y=randint(1,size-2)
        if land_map[x][y]==LAND:
            land_map[x][y]=LAUNCHER
            i+=1
    return land_map

def show_map(land_map):
    i=0
    height=len(land_map)
    width=len(land_map[0])    
    print('#'+'#'*width+'#')
    while i<height:
        j=0
        print('#',end='')
        while j<width:
            print(land_map[i][j],end='')
            j+=1
        print('#')
        i+=1
    print('#'+'#'*width+'#')
    print("# Legenda : + - Ląd, O - Miasto, === - Lotnisko, ^ - Wyrzutnia, X - Zniszczony teren")
    print((width+2)*'#')

def map_generator():
    print("Dostosuj tworzenie ladu.")
    size=int(input("Wprowadz wielkosc mapy (20-60) : "))
    while size>60 or size<20 :
        size=int(input("Wprowadz poprawna wielkosc mapy : "))
    land_count=int(input("Wprowadz ilosc ladu (50-200) : "))
    while land_count>200 or land_count<50 :
        land_count=int(input("Wprowadz poprawna ilosc ladu : "))
    city_count=int(input("Wprowadz ilosc miast (1-15) : "))
    while city_count>15 or city_count<1 :
        city_count=int(input("Wprowadz poprawna ilosc miast : "))
    airport_count=int(input("Wprowadz ilosc lotnisk (1-5) : "))
    while airport_count>5 or airport_count<1 :
        airport_count=int(input("Wprowadz poprawna ilosc lotnisk : "))
    launcher_count=int(input("Wprowadz ilosc wyrzutni (1-10) : "))
    while launcher_count>10 or launcher_count<1 :
        launcher_count=int(input("Wprowadz poprawna ilosc wyrzutni : "))
    land_map=create_map(size,land_count,city_count,airport_count,launcher_count)
    show_map(land_map)
    return land_map

