from colorama import Fore as cl
raw = r"""
+-----------+
| O         |
+------+    +
|           |
|    m      |
+-----------+
"""

map = [] 
sizes = []

for i in raw.splitlines(): 
    sizes.append(len(i))
    map.append(list(i))

raw2 = r""""""
for i in raw.splitlines():
    while len(i) != max(sizes):
        i += ' '
    else:
        raw2 += i + '\n'
else:
    print(f'Finished adjusting the map size! (found ideal size: {max(sizes)})')

map.clear()
for i in raw2.splitlines():
    map.append(list(i))

raw=raw2
builder = """"""""

print(builder)

def renderMap():
    global builder 

    builder = """"""

    for fileira in map:
        linha = ''
        for coluna in fileira:
            linha += coluna.replace('O', f'{cl.GREEN}O{cl.RESET}')
        else:
            builder += linha + '\n'
    #else:
    #    print('Finished rendering the map')

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

    try:
        nextPos = map[playerY+y][playerX+x]

        def moveToNextPredict(): map[playerY][playerX], map[playerY+y][playerX+x] = map[playerY+y][playerX+x], map[playerY][playerX]

        if nextPos == ' ':
            moveToNextPredict()
        else:
            if nextPos == 'm':
                print('Found a chest!')
                map[playerY][playerX], map[playerY+y][playerX+x] = ' ', map[playerY][playerX]

            print('I can\'t walk.')
    except:
        pass 

    renderMap()

while True:
    newPos = input('W/A/S/D\n> ').lower()

    for i in newPos:
        if i == 'd': movePlayer(1, 0)
        if i == 'a': movePlayer(-1, 0)
        if i == 'w': movePlayer(0, -1)
        if i == 's': movePlayer(0, 1)
    else:
        print(builder)

#  ☺
# -┼-
# / \          
