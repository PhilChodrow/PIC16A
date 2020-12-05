import tkinter as tk

# create the main window that holds the entire interface 
window = tk.Tk() 

# give it a title
window.title("Hello, widget!") 

# specify the size of the window in pixels. Because
# of some weird specifics with Tkinter, the size must be
# specified as a string of the form  "widthxheight" 
window.geometry("600x300") 

# maybe you'd like a resizable window! 
window.resizable(width=True, height=True)

# if your user resizes the window too small, it might be 
# impossible to read what's going on. You can define a 
# minimum width and height to prevent this issue. 
window.minsize(width=300, height=300) 

########################################################################  
# LABELS
########################################################################  

# labels are just text, and are our first example of a widget
# "Widgets" are just "the stuff" that goes in the interface: 
# text, buttons, images, etc. When constructing a widget, 
# you need to pay attention to: 
# 1. What is the widget contained in? For now, we'll just put widgets 
#    directly in the overall window. 
# 2. What are the properties of the widget itself? How should it look 
#    and behave? 
# 3. How should the widget be positioned inside its container? 
label1 = tk.Label(window, 
                  text = "Woo penguins", 
                  bg='firebrick', 
                  fg='white', 
                  height='2', 
                  font=("Helvetica 16 bold"))

label1.grid(row=0, column=0)

# we can add as many labels as we want, and position them on the grid
# as needed
for i in range(5):
    
    lab = tk.Label(window, 
                   text = "Woo penguins", 
                   bg='firebrick', 
                   fg='white', 
                   height='2', 
                   font=("Helvetica 16 bold"))
    
    lab.grid(row=i, column=i)

########################################################################  
# FRAMES
########################################################################  

# Frames are just rectangles that can hold stuff. 
# The are are ideal for keeping your app 
# organized. Let's make some sections: 

frame_header = tk.Frame(window, 
                        borderwidth=2, 
                        pady=2, 
                        bg = "gray")

frame_body   = tk.Frame(window, 
                        borderwidth=2, 
                        pady=2, 
                        bg = "white")

frame_footer = tk.Frame(window, 
                        borderwidth=2, 
                        pady=2, 
                        bg = "blue")

frame_header.grid(row=0, column=0)
frame_body.grid(row=1,column=0)
frame_footer.grid(row=2,column=0)

# the frames won't actually be visible until we put something in them. 
# note that we specify that the label header now lives within the frame_header
# not the entire window
label_header = tk.Label(frame_header, 
                        text = "Woo penguins", 
                        bg='firebrick', 
                        fg='white', 
                        height=2, 
                        width = 35, 
                        font=("Helvetica 16 bold"))

label_header.grid(row=0,column=0)

label_body = tk.Label(frame_body, 
                      text = "to boldly go where penguins have gone before", 
                      bg = "white", 
                      fg = "black")

label_body.grid(row=0, column=0)

label_footer = tk.Label(frame_footer, 
                        text = "all done", 
                        bg = "white", 
                        fg = "black")

label_footer.grid(row=0, column=0)

# finally, we run the mainloop() function of the main window to actually run the app. 
window.mainloop()