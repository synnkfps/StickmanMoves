raw = r"""
          O    
+-------+   +---+
|  m            |
|               |
+---------------+
"""

map = [] 
sizes = []

for i in raw.splitlines(): 
    sizes.append(len(i))
    map.append(list(i))

raw2 = """"""
for i in raw.splitlines():
    while len(i) != max(sizes):
        i += ' '
    else:
        raw2 += i + '\n'
    
raw=raw2
print(raw)
print(sizes, max(sizes))
builder = """"""""

print(builder)

def renderMap():
    global builder 

    builder = """"""

    for fileira in map:
        linha = ''
        for coluna in fileira:
            linha += coluna
        else:
            builder += linha + '\n'
    else:
        print('Finished rendering the map')

renderMap() # renderiza pela primeira vez

rawPositions = [0, 0]
def getPlayerPos():
    global rawPositions

    colunaAtual = 0 # X
    fileiraAtual = 0 # Y

    for y, fileira in enumerate(map):
        for x, coluna in enumerate(fileira):
            if coluna == 'O': # player
                colunaAtual = x
                fileiraAtual = y
                break
        
    return (colunaAtual, fileiraAtual) # retornar uma tupla com o X e o Y (x, y)

# função movePlayer(x,y): move o player de acordo com os parâmetros dados
def movePlayer(x, y):
    playerX = getPlayerPos()[0]
    playerY = getPlayerPos()[1]

    print(playerX, playerY)
    nextPos = map[playerY+y][playerX+x]
    if nextPos == ' ':
        map[playerY][playerX], map[playerY+y][playerX+x] = map[playerY+y][playerX+x], map[playerY][playerX]
    else:
        if nextPos == 'm':
            print('Found a chest!')
            map[playerY][playerX], map[playerY+y][playerX+x] = ' ', map[playerY][playerX]
        
        print('I can\'t walk.')

    renderMap()
    print(builder)

while True:
    newPos = input('W/A/S/D\n> ').lower()

    for i in newPos:
        if i == 'd':
            movePlayer(1, 0)
        if i == 'a':
            movePlayer(-1, 0)
        if i == 'w':
            movePlayer(0, -1)
        if i == 's':
            movePlayer(0, 1)

#  ☺
# -┼-
# / \          
