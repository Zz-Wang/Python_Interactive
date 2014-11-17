# implementation of card game - Memory
# Zhizheng Wang

import simplegui
import random

# helper function to initialize globals
def new_game():
    global list1, exposed, state, index, counter
    list1 = range(0,8)
    list2 = list1
    list1.extend(list2)
    random.shuffle(list1)
    exposed = [False] * 16
    state = 0
    index = [False, False]
    counter = 0


# define event handlers
def mouseclick(pos):
    global exposed, state, l1, l2, index, counter
    ind = pos[0]/50
    if exposed[ind] == False:
        if state == 0:
            state = 1
            exposed[ind] = True
            index[0] = ind
            l1 = list1[index[0]]
            exposed[index[0]] = True
        elif state == 1:
            state = 2
            counter += 1
            index[1] = ind
            l2 = list1[index[1]]
            exposed[index[1]] = True
        else:
            state = 1
            if l1 != l2:
                exposed[index[0]] = False
                exposed[index[1]] = False
            index[0] = ind
            index[1] = False
            l1 = list1[index[0]]
            exposed[index[0]] = True

           
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed, counter
    for i in range(0, 16):
        if exposed[i]:
            rectangular_pos = [(50 * i, 0), (50 * (i+1) , 0), (50 * (i+1), 100), (50 * i, 100)]
            canvas.draw_polygon(rectangular_pos, 2, 'Grey', 'Black')
            text_pos = [15 + 50 * i,60]
            canvas.draw_text(str(list1[i]), text_pos, 40, 'White', 'monospace')
        else:
            rectangular_pos = [(50 * i, 0), (50 * (i+1) , 0), (50 * (i+1), 100), (50 * i, 100)]
            canvas.draw_polygon(rectangular_pos, 2, 'Grey', 'Green')
        i += 1
    label.set_text('Turns = ' + str(counter))


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)


# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric