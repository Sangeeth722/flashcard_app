BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random



try:
    df = pandas.read_csv("data/word_to_learn.csv",encoding='ISO-8859-1')

except FileNotFoundError:
    df = pandas.read_csv("data/french_words.csv")
    to_learn = df.to_dict(orient="records")
else:
    to_learn = df.to_dict(orient="records")



english_name = None
random_name = {}





def new_word():
    global english_name,random_name
    #global flip_timer

    #window.after_cancel(flip_timer)

    right_button["state"] = "disabled"
    wrong_button["state"] = "disabled"

    random_name = random.choice(to_learn)



    english_name = random_name["English"]
    canvas.itemconfig(canvas_image,image =card_front_img )
    random_french_name = random_name["French"]
    canvas.itemconfig(title,text = "French",fill = "Black")
    canvas.itemconfig(word,text = random_french_name,fill = "Black")


    flip_timer = window.after(3000, func=flip_card)




def flip_card():
    canvas.itemconfig(canvas_image, image = card_back_img)
    canvas.itemconfig(title,text = "English",fill = "White")
    canvas.itemconfig(word,text = english_name)
    canvas.itemconfig(word,fill = "White")
    right_button["state"] = "normal"
    wrong_button["state"] = "normal"

def to_know():
    new_word()
    to_learn.remove(random_name)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/word_to_learn.csv",index=False)





window = Tk()
window.minsize(width=900,height=900)
window.config(bg=BACKGROUND_COLOR)
window.config(padx=50,pady=50)

#flip_timer = window.after(3000, flip_card)

canvas = Canvas(height=526,width=800)

front_image_path = "images/card_front.png"
card_back_image_path = "images/card_back.png"

card_front_img =PhotoImage(file=front_image_path)
card_back_img = PhotoImage(file=card_back_image_path)
canvas_image = canvas.create_image(410,278,image = card_front_img)
canvas.grid(row=0,column=0,columnspan=2)


r_button_image = PhotoImage(file="images/right.png")
right_button = Button(image=r_button_image,highlightthickness=0,command=to_know)
right_button.grid(row=1,column=1)

wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image,highlightthickness=0,command=new_word)
wrong_button.grid(row=1,column=0)

title = canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
word = canvas.create_text(400,263,text="",font=("Ariel",60,"bold"))

new_word()

window.mainloop()



