import tkinter
import random 
import time
import operator

score = 0
keyboard = 0
square = []
store_square = []
position = []
store_position = []
store_dup_position = []
store_dup_square = []
store_dup_sq_color = []
store_dup_sq_po = []
store_old_key = []
store_color_score = []
color = ["yellow","orange","pink","aqua","green","red","ivory","purple","saddlebrown","royalblue","grey"]
position_x = [100,200,300,400]
position_y = [100,200,300,400]


for n in range(len(position_x)):
    for i in range(len(position_y)):
        position.append([position_x[n],position_y[i],color[0]])

frame = tkinter.Tk()

window = tkinter.Canvas(frame, bg= "white", height=430, width=430)

def key (event):
    global keyboard, square, score
    keyboard = event.keysym
    print (repr(event.keysym))
    if event.keysym == "Left":
            square = sorted(square, key = operator.itemgetter(1,0))
            window.delete('all')
            for i in range(len(square)):
                if square[i][0] != 100:
                    square[i][0] = 0
                    square[i][0] = 100
            process()

    elif event.keysym == "Right":
            store_old_key.append(event.keysym)
            square = sorted(square, key = operator.itemgetter(1,0), reverse = True)
            window.delete('all')
            for i in range(len(square)):
                if square[i][0] != 400:
                    square[i][0] = 0
                    square[i][0] = 400
            process()

    elif event.keysym == "Up":
            store_old_key.append(event.keysym)
            square = sorted(square, key = operator.itemgetter(0,1))
            window.delete('all')
            for i in range(len(square)):
                if square[i][1] != 100:
                    square[i][1] = 0
                    square[i][1] = 100
            process()

    elif event.keysym == "Down":
            store_old_key.append(event.keysym)
            square = sorted(square, key = operator.itemgetter(0,1),reverse=True)
            window.delete('all')
            for i in range(len(square)):
                if square[i][1] != 400:
                    square[i][1] = 0
                    square[i][1] = 400
            process()

    
def rand ():
    global square
    random.shuffle(position)
    square.append(position[0])
    position.pop(0)
    

def draw ():
    for i in range(len(square)):
        window.create_rectangle(square[i][0]-90,square[i][1]-90, square[i][0], square[i][1], fill = square[i][2])

def duplicate_sq():
    global score
    store_dup_square = []
    store_dup_sq_color = []
    store_dup_sq_po = []
    store_color_score = []

    for i in range(len(square)-1):
        if square[i] == square[i+1] and i not in store_dup_sq_color:
            store_dup_sq_color.append(i)
            store_dup_sq_color.append(i+1)
            store_dup_square.append(i)

    for m in range(len(store_dup_sq_color)):
                    square[store_dup_sq_color[m]][2] = color[color.index(square[store_dup_sq_color[m]][2])+1]
                    store_color_score.append(square[store_dup_sq_color[m]][2])     
    
    store_dup_square = sorted(store_dup_square, reverse=True)

    if len(store_dup_square) > 0:
        for i in range(len(store_dup_square)):
            score += 1
            square.pop(store_dup_square[i])

    
    for m in range(3):
        for i in range(len(square)):
            for n in range(len(square)):
                if square[i][0] == square[n][0] and square[i][1] == square[n][1]:
                    if i != n:
                        if keyboard == "Left" and square[n][0] < 400:
                            square[n][0] += 100
                        elif keyboard == "Right" and square[n][0] > 100:
                            square[n][0] -= 100
                        elif keyboard == "Up" and square[n][1] < 400:
                            square[n][1] += 100
                        elif keyboard == "Down"  and square[n][1] > 100:
                            square[n][1] -= 100

    if len(store_color_score) > 0:
        for i in range(len(store_color_score)):
            score = color.index(store_color_score[i])*2 + score 

def duplicate_po ():
    store_dup_position = []
    for i in range(len(position)):
        for n in range(len(square)):
            if position[i][:2] == square[n][:2]:
                store_dup_position.append(position[i])
    if len(store_dup_position) > 0:
        for i in range(len(store_dup_position)):
            position.remove(store_dup_position[i])

def refill():
    store_position = []
    store_refill = []
    for n in range(len(position_x)):
        for i in range(len(position_y)):
            store_position.append([position_x[n],position_y[i],color[0]])

    for i in range(len(square)):
        store_refill.append([square[i][2]])
        del square[i][2:]
    for k in range(len(store_position)):
        if store_position[k][:2] not in square and store_position[k] not in position:
                position.append(store_position[k])

    for i in range(len(store_refill)):
        square[i].extend(store_refill[i])

def end ():
    global square
    if len(position) == 0 or 9 in square:
        window.delete('all')
        del square[:]
        window.create_text(200,150, text=("End Game, Final score:",score),  font=65)
        window.create_text(200,200, text="Will Log out in 5 seconds, Bye",  font=65)
        window.after(3500, tkinter._exit)

def process ():
    global store_old_square
    duplicate_sq()
    duplicate_po()
    refill()
    rand()
    draw()
    var.set(score)
    end()
    print("")
    print("final sq:", square, len(square))
    print("")    
    

for i in range(2):
    rand()
    draw()

var = tkinter.StringVar()
label = tkinter.Label(textvariable = var, anchor = "n")
print("//The color represent the number sequence")
print("    2          4        8      16       32      64     128      256          512          1024       2048")
print(color)
frame.bind("<Key>", key)
label.pack()
window.pack()
frame.mainloop()



