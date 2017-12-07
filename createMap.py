import random

cols_count = 40
rows_count = 40

map = [[0 for x in range(cols_count)] for x in range(rows_count)]
numRooms = 3

def start():

    # fill map with . chars
    for row in range(cols_count):
        for col in range(rows_count):
            map[row][col] = '.'


    # Draw rooms
    i = 0
    while i < numRooms:
        drawRoom()
        i+=1

        print str(i)+ " : " + str(numRooms)




def drawRoom():
    f = open('map.txt', 'w+')

    # random height and width for each room
    height = random.randint(5, 10)
    width = random.randint(7, 10)


    # no overlapping rooms
    overlap = True

    num = 0

    # random x and  y position
    col_pos = random.randint(1, 39)
    row_pos = random.randint(1, 39)

    while col_pos+width >= cols_count:
        width -= 1
        col_pos -= 1

    while row_pos+height >= rows_count:
        height -= 1
        row_pos -= 1




    draw = True

    # check for overlapping
    for row in range(row_pos-1, row_pos+height+1):
        for col in range(col_pos-1, col_pos+width+1):

            if map[row][col] == '#':
                draw = False





    # add on to the number of rooms to make the initial iterations correct.
    if draw == False:
        global numRooms
        numRooms += 1

    if draw == True:
        print "draw"
        # top row
        # xpos > xpos+width
        for col in range(col_pos, col_pos+width):
            row = row_pos
            map[row][col] = '#'

        # bottom row
        # xpos+heigh > xpos+width
        for col in range(col_pos, col_pos+width+1):
            row = row_pos+height
            map[row][col] = '#'

        # left col
        # ypos > ypos+height
        for row in range(row_pos, row_pos+height):
            col = col_pos
            map[row][col] = '#'



        # right column
        # xpos+height > xpos+width
        for row in range(row_pos, row_pos+height):
            col = col_pos+width
            map[row][col] = '#'




    # write to text file
    for i in range(0, 40):
        for j in range(0, 40):
            f.write(map[i][j])
        f.write('\n')



start()
