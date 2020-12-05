# Our next aim is to build a simple app that will 
# accept user input and show useful output. 
# Our app will be a penguin classifier: input some 
# measurements of a penguin, and the classifier will
# make an educated guess about the penguin's species. 
# This means that we'll need to find a way to bring in
# our machine learning expertise "under the hood" of the app.
# Fortunately, that's actually quite easy to do. 
# This time, our focus is simply on acquiring user input. 

import tkinter as tk

# see previous lecture for reminders about what these
# lines do. 
window = tk.Tk() 
window.geometry("600x300") 
window.title("Penguin Classifier") 
window.minsize(width=300, height=300) 

frame_header = tk.Frame(window, 
                        borderwidth=2, 
                        pady=2, 
                        bg = "black")

frame_header.grid(row=0, 
                  column=0)

label_header = tk.Label(frame_header, 
                        text = "Woo penguins",
                        bg='white', 
                        fg='black', 
                        height=2, 
                        width = 35, 
                        font=("Helvetica 16 bold"))

label_header.grid(row=0, column=0)

frame_center = tk.Frame(window, 
                        borderwidth=2, 
                        pady=2, 
                        bg = "black")

frame_center.grid(row=1, column=0)

frame_bottom = tk.Frame(window, 
                        borderwidth=2, 
                        pady=2, 
                        bg = "black")

frame_bottom.grid(row=2, column=0)

# we are going to create three input fields, each corresponding 
# to a column used by our machine learning model. 
# To do this, it's helpful to add a frame for each
# input field.

frame_main_1 = tk.Frame(frame_center, 
                        borderwidth=2)

frame_main_2 = tk.Frame(frame_center, 
                        borderwidth=2)

frame_main_3 = tk.Frame(frame_center, 
                        borderwidth=2)

var1_label = tk.Label(frame_main_1, 
                      text = "Island: ")

var2_label = tk.Label(frame_main_2, 
                      text = "Body Mass (g): ")

var3_label = tk.Label(frame_main_3, 
                      text = "Culmen Length (mm): ")

# pack is like grid, but it's useful for when we want to ensure
# that certain elements are placed nearby and side-by-side. 

frame_main_1.pack(fill='x', pady=2)
frame_main_2.pack(fill='x', pady=2)
frame_main_3.pack(fill='x', pady=2)

var1_label.pack(side='left')
var2_label.pack(side='left')
var3_label.pack(side='left')

# now we'll do the same thing for the spot that will hold the "answer"

frame_answer = tk.Frame(frame_bottom, 
                        borderwidth=2, 
                        relief='sunken')

frame_answer.pack(fill='x', pady=0)

# So, we are beginning to see the outlines of an interface. 
# We still don't have a way to actually acquire or store 
# information provided by the user though, so that's next. 
# the tk.StringVar() object is what tracks and holds this 
# information. 
# We then acquire that info from the user. 
# For the first variable, we'll use a dropdown menu,
# while for the other two variables we'll use simple text entry. 
# Lots of other kinds of data entry mechanisms are also possible. 
# For that, we use tk.Entry(). We need to supply 
# both the frame in which the entrybox should live 
# and the variable to which the entrybox is bound

var1 = tk.StringVar()

var1_entry = tk.OptionMenu(frame_main_1, 
                           var1, 
                           "Torgersen", 
                           "Biscoe", 
                           "Dream")

var1_entry.pack(side='right', padx=1)

var2 = tk.StringVar()

var2_entry = tk.Entry(frame_main_2, 
                      textvariable = var2, 
                      width=10)

var2_entry.pack(side='right', padx=1)

var3 = tk.StringVar()

var3_entry = tk.Entry(frame_main_3, 
                      textvariable = var3, 
                      width=10)

var3_entry.pack(side='right', padx=1)

# We are now able to accept input from the user. 
# Let's just check for now that we are able to "remember" 
# this information by placing the resulting StringVars 
# within labels. 

# We'll replace this in a future letter with something more interesting
answer_label = tk.Label(frame_answer, 
                        font=('arial', 16, 'bold'), 
                        bd=16, 
                        anchor="w", 
                        textvariable=var1)   

answer_label.grid(row=0, column=0)

# Ok, looks like we are able to acquire and store user input! 
# Next time we'll see how to use buttons to trigger events, allowing us 
# to perform arbitrary operations on the input. 

window.mainloop()

