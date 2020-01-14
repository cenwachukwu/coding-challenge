# write a program that determines each sequence of ship positions and reports the final position of the ship

def take_inputs () :
    # ask for input

    #  input1: 
    # grid point coordinates (x, y) = ints < 50  
    # # first line of input is the top right (y (north), x (east))
    # # lower-left (or south-west) coordinates are assumed to be( y(south) = 0, x(west) = 0)
    northEast = str(input("Type in grid point coordinates i.e. X Y: "))
    northEastList = ''.join(northEast).split() 
    print(northEastList)

    # input2: ship position ((grid point coordinates (x, y) + (ship orientation))
    # # orientation (N, S, E, W) = string, Uppercase
    shipPosition = str(input("Type in grid point coordinates and ship orientation i.e. X Y N: ")).upper()
    shipPositionList = ''.join(shipPosition).split() 

    # collect grid point coordinates into integers of X & Y
    X = int(shipPositionList[0])
    Y = int(shipPositionList[1])
    # collect ship orientation string in ship position
    shipOrientation = str(shipPositionList[2])
    print(f'Input: {X} {Y} {shipOrientation}')


    # input 3: Ship instruction (2 lines per ship)
    # ship instruction : string of the letters "L", "R", and "F" on one line, < 100 characters 
    shipInstruction = str(input("Type in Ship instructions i.e. LRF: ")).upper()
    shipInstructionList = ' '.join(shipInstruction).split()   
    print(shipInstructionList)

    # analyze ship instructions
    for i in shipInstructionList:
    # # R: the ship turns right 90 degrees and remains on the current grid point.
    # # if R, N --> E 
    # # if R, E --> S 
    # # if R, S --> W 
    # # if R, W --> N 
        if (i == "R"):
            if (shipOrientation == "N") :
                shipOrientation = "E"
            elif (shipOrientation == "E") :
                shipOrientation = "S"
            elif (shipOrientation == "S") :
                shipOrientation = "W"
            elif (shipOrientation == "W") :
                shipOrientation = "N"
            print (shipOrientation)
    # # L: the ship turns left 90 degrees and remains on the current grid point.
    # # if L, N --> W
    # # if L, W --> S
    # # if L, S --> E
    # # if L, E --> N
        elif (i == "L"):
            if (shipOrientation == "N") :
                shipOrientation = "W"
            elif (shipOrientation == "W") :
                shipOrientation = "S"
            elif (shipOrientation == "S") :
                shipOrientation = "E"
            elif (shipOrientation == "E") :
                shipOrientation = "N"
            print (shipOrientation)
    # # Forward: the ship moves forward one grid point in the direction of the current orientation and maintains the same orientation. The direction North corresponds to the direction from grid point (x, y) to grid point (x, y+1) and the direction east corresponds to the direction from grid point (x, y) to grid point (x+1, y).
    # # if F, X = X+1
    # # if F, Y = Y+1
        elif (i == "F"):
            if (shipOrientation == "N") :
                Y = Y + 1
            elif (shipOrientation == "W") :
                X = X - 1
            elif (shipOrientation == "S") :
                Y = Y - 1
            elif (shipOrientation == "E") :
                X = X + 1
    # see if it works:
    if (X and Y >= 50):
        print(f'{X} {Y} {shipOrientation} LOST')
    elif (X and Y < 50):
        print(f'{X} {Y} {shipOrientation}')



take_inputs()
