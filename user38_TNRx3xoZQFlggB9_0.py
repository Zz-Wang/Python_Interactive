# miniproject for "Stopwatch: The Game"
# Zhizheng Wang

import simplegui

# define global variables
width = 600
height = 400
interval = 100
time = 0
position1 = [200, 200]
position2 = [525, 50]
stop_counter = 0
stop_lovecounter = 0
stop = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    sec = t % 600
    min = (t-sec)/600
    a = str(min)
    milisec = sec % 10
    d = str(milisec)
    z = ((sec-milisec)/10)
    b = str(z)
    if z < 10:
        return a + ":0" + b + "." + d
    else:
        return a + ":" + b + "." + d
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    global stop
    timer.start()
    stop = True
  
def Stop():
    global stop_counter, stop_lovecounter, stop
    timer.stop()
    if stop:
        stop_counter = stop_counter + 1
        if time % 10 == 0:
            stop_lovecounter = stop_lovecounter + 1
    stop = False

def Reset():
    global time, stop_counter, stop_lovecounter
    time = 0
    stop_counter = 0
    stop_lovecounter = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time = time + 1
    #print time

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), position1, 72, "White")
    canvas.draw_text(str(stop_lovecounter)+'/'+str(stop_counter), position2, 36, "Red")
    
# create frame
frame = simplegui.create_frame("Stopwatch", width, height)


# register event handlers
frame.add_button("Start", Start, 100)
frame.add_button("Stop", Stop, 100)
frame.add_button("Reset", Reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)

# start frame
frame.start()


# Please remember to review the grading rubric
