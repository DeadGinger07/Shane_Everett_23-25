from tkinter import HIDDEN, NORMAL, Tk, Canvas
root = Tk()
import random

#for canvas
c = Canvas(root, width=400, height=400)
c.configure(bg='#FF91AF', highlightthickness=0)

#for body
c.body_color = '#CC9911'
body = c.create_oval (35, 20, 365, 350, outline=c.body_color, fill=c.body_color)
ear_left = c.create_polygon(75, 80, 75, 10, 165, 70, outline='#FCCB4F', fill='#FCCB4F')
ear_right = c.create_polygon(255, 45, 325, 10, 320, 70, outline='#592720', fill='#592720')
foot_left = c.create_oval(65, 320, 145, 360, outline='#947706', fill='#947706')
foot_right = c.create_oval(250, 320, 330, 360, outline='#4EA809', fill='#4EA809')
eye_left = c.create_oval(130, 110, 160, 170, outline='#F6F6FF', fill='#F6F6FF')
pupil_left = c.create_oval(140, 145, 150, 155, outline='#08B07C', fill='#08B07C')
eye_right = c.create_oval(230, 110, 260, 170, outline='#F6F6FF', fill='#F6F6FF')
pupil_right = c.create_oval(240, 145, 250, 155, outline='#FFCC88', fill='#FFCC88')
mouth_normal = c.create_line(170, 250, 230, 250,  smooth=1, width=5, state=NORMAL, fill='#738678')
mouth_happy = c.create_line(170, 250, 200, 432, 230, 250,  smooth=1, width=5, state=HIDDEN, fill='#B05923')
mouth_sad = c.create_line(170, 250, 200, 232, 230, 250,  smooth=1, width=5, state=HIDDEN, fill='#A55')
cheek_left = c.create_oval(70, 180, 120, 230, outline='#615649', fill='#6082B6', state=HIDDEN)
cheek_right = c.create_oval(280, 180, 330, 230, outline='#615649', fill='#6082B6', state=HIDDEN)
tongue_main = c.create_rectangle(170, 250, 230, 290, outline='#860111', fill='#860111', state=HIDDEN)
tongue_tip = c.create_oval(170, 285, 230, 300, outline='#deface', fill='#deface', state=HIDDEN)

#defines color
def change_color():
    pet_colors = ['#CC0605', '#343E40', '#497E76', '#6A5F31', '#D84B20', '#1D334A']
    c.body_color = random.choice(pet_colors)
    c.itemconfigure(body, outline=c.body_color, fill=c.body_color)
    c.itemconfigure(ear_left, outline=c.body_color, fill=c.body_color)
    c.itemconfigure(ear_right, outline=c.body_color, fill=c.body_color)
    c.itemconfigure(foot_left, outline=c.body_color, fill=c.body_color)
    c.itemconfigure(foot_right, outline=c.body_color, fill=c.body_color)
    root.after(3000, change_color)

#define multiple body functions
def toggle_eyes():
    current_color = c.itemcget(eye_left, 'fill')
    new_color = '#AA0022' if current_color == '#E3256B' else '#E3256B'
    current_state = c.itemcget(pupil_left, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(pupil_right, state=new_state)
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)

def blink():
    toggle_eyes()
    root.after(250, toggle_eyes)
    root.after(3000, blink)
    
#toggles the wink function below
def toggle_left_eye():
    current_color = c.itemcget(eye_left, 'fill')
    new_color = c.body_color if current_color == '#F6F6FF' else '#F6F6FF'
    current_state = c.itemcget(pupil_left, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(eye_left, fill=new_color)

def wink(event):
    toggle_left_eye()
    root.after(250, toggle_left_eye)

#part of the eyes
def toggle_pupils():
    if not c.eyes_crossed:
        c.move(pupil_left, 10, -5)
        c.move(pupil_right, -10, -5)
        c.eyes_crossed = True
    else:
        c.move(pupil_left, -10, 5)
        c.move(pupil_right, 10, 5)
        c.eyes_crossed = False
        
# for mouths
def toggle_tongue():
    if not c.tongue_out:
        c.itemconfigure(tongue_tip, state=NORMAL)
        c.itemconfigure(tongue_main, state=NORMAL)
        c.tongue_out = True
    else:
        c.itemconfigure(tongue_tip, state=HIDDEN)
        c.itemconfigure(tongue_main, state=HIDDEN)
        c.tongue_out = False

#for cheeks
def cheeky(event):
    toggle_tongue()
    toggle_pupils()
    hide_happy(event)
    root.after(1000, toggle_tongue)
    root.after(1000, toggle_pupils)
    return

#for mood functions
def show_happy(event):
    if (20 <= event.x <=350) and (20 <= event.y <=350):
        c.itemconfigure(cheek_left, state=NORMAL)
        c.itemconfigure(cheek_right, state=NORMAL)
        c.itemconfigure(mouth_happy, state=NORMAL)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=HIDDEN)
        c.happy_level = 10
    return

def hide_happy(event):
        c.itemconfigure(cheek_left, state=HIDDEN)
        c.itemconfigure(cheek_right, state=HIDDEN)
        c.itemconfigure(mouth_happy, state=HIDDEN)
        c.itemconfigure(mouth_normal, state=NORMAL)
        c.itemconfigure(mouth_sad, state=HIDDEN)
        return

def sad():
    if c.happy_level == 0:
        c.itemconfigure(mouth_happy, state=HIDDEN)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=NORMAL)
    else:
        c.happy_level -= 1
    root.after(5000, sad)

#binds all functions to something
c.pack()
c.bind('<Motion>', show_happy)
c.bind('<Leave>', hide_happy)
c.bind('<Double-1>', cheeky)
c.bind('<Button-2>', wink)
c.happy_level = 10
c.eyes_crossed = False
c.tongue_out = False
root.after(1000, blink)
root.after(5000, sad)
root.after(3000, change_color)
root.mainloop()
