import tkinter as tk
from brain import Data
from PIL import Image, ImageTk

# Initialisation fo Objects
dt = Data()
root = tk.Tk()

# background colors for frames
BG_1 = '#B8E8FC'

# set the tile and window size
root.title(" Weather App ")
root.minsize(width=500, height=800)

# Initialisation of the chosen city variable which would be modified in the load frame1 method
chosen_city = ''


def clear_widgets(f):
    """select all frame widgets and delete them"""
    for widget in f.winfo_children():
        widget.destroy()


def load_frame1():
    """ This function contains and loads all the widgets needed for frame 1"""

    clear_widgets(f2)
    # stack frame 2 above frame 1
    f1.tkraise()
    # prevents the widgets from modifying the frame
    f1.grid_propagate(False)

    bg_img = Image.open("images/Weather.png")
    bg_img = ImageTk.PhotoImage(bg_img)
    bg_label = tk.Label(f1, image=bg_img, borderwidth=0)
    bg_label.image = bg_img
    bg_label.grid(row=0, column=0, pady=50)

    instruction = tk.Label(f1, text="Enter the name of the City:", fg="#FF577F", bg=BG_1,
                           font=('Helvetica', 20))
    instruction.grid(row=1, column=0, pady=20)

    city_entry = tk.Entry(f1, highlightbackground=BG_1)
    city_entry.grid(row=2, column=0, pady=20)

    def get_city_entry():
        global chosen_city
        """This function gets the city entered and calls the next frame"""

        # gets the city name entry from the Entry widget
        chosen_city = city_entry.get()

        # calls the method that requests the data from the Api
        dt.get_city(chosen_city)

        # gets the time based on tz_id to be used in frame 2
        dt.get_time()

        load_frame2()

    enter_button = tk.Button(f1, text='Enter', highlightcolor='black', fg="black", command=get_city_entry,
                             highlightbackground=BG_1, cursor='hand', activebackground="#badee2",
                             activeforeground="black")
    enter_button.grid(row=3, column=0, pady=20)


def load_frame2():
    """ This function contains and loads all the widgets needed for frame 2"""

    clear_widgets(f1)
    # stack frame 1 above frame 2
    f2.tkraise()
    # prevents the widgets from modifying the frame
    f2.grid_propagate(False)

    # change the bg colour depending on the result of the method
    f2.config(bg=dt.get_bg_colour())

    date_label = tk.Label(f2, text=f'{dt.date}', bg=dt.get_bg_colour(), fg='white', font=('Helvetica', 25))
    date_label.grid(row=0, column=0, pady=10, columnspan=4)

    time_label = tk.Label(f2, text=f'{dt.time}', bg=dt.get_bg_colour(), fg='white', font=('Helvetica', 35))
    time_label.grid(row=1, column=0, pady=10, columnspan=4)

    city_name = tk.Label(f2, text=f'{dt.city_name}', bg=dt.get_bg_colour(), fg="white", font=('Helvetica', 25))
    city_name.grid(row=2, column=0, pady=20, columnspan=4)

    weather_img = Image.open(f'{dt.weather_symbol(chosen_city, size="big")}')
    weather_img = ImageTk.PhotoImage(weather_img)
    weather_img_label = tk.Label(f2, image=weather_img, bg=dt.get_bg_colour())
    weather_img_label.image = weather_img
    weather_img_label.grid(row=3, column=0, pady=15, columnspan=4)

    temp_label = tk.Label(f2, text=f"{dt.current_temp}", font=("Arial", 75), bg=dt.get_bg_colour(), fg="white")
    temp_label.grid(row=4, column=0, columnspan=4)

    divisor_line_label = tk.Label(frame, text="_________________________________________________________", fg="white",
                                  bg=dt.get_bg_colour())
    divisor_line_label.grid(row=5, column=0, columnspan=5)

    six_am_label = tk.Label(frame, text="6am", fg="white", bg=dt.get_bg_colour())
    six_am_label.grid(row=6, column=0)
    nine_am_label = tk.Label(frame, text="9am", fg="white", bg=dt.get_bg_colour())
    nine_am_label.grid(row=6, column=1)
    twelve_pm_label = tk.Label(frame, text="12pm", fg="white", bg=dt.get_bg_colour())
    twelve_pm_label.grid(row=6, column=2)
    three_pm_label = tk.Label(frame, text="3pm", fg="white", bg=dt.get_bg_colour())
    three_pm_label.grid(row=6, column=3)

    six_am_img = dt.weather_symbol(current_weather=f'{dt.six_am}', size='small')
    six_am_weather_img = Image.open(six_am_img)
    six_am_weather_img = ImageTk.PhotoImage(six_am_weather_img)
    six_am = tk.Label(f2, image=six_am_weather_img, bg=dt.get_bg_colour())
    six_am.img = six_am_weather_img
    six_am.grid(row=7, column=0)

    nine_am_img = dt.weather_symbol(current_weather=f'{dt.nine_am}', size='small')
    nine_am_weather_img = Image.open(nine_am_img)
    nine_am_weather_img = ImageTk.PhotoImage(nine_am_weather_img)
    nine_am = tk.Label(f2, image=nine_am_weather_img, bg=dt.get_bg_colour())
    nine_am.img = nine_am_weather_img
    nine_am.grid(row=7, column=1)

    twelve_pm_img = dt.weather_symbol(current_weather=f'{dt.twelve_pm}', size='small')
    twelve_pm_weather_img = Image.open(twelve_pm_img)
    twelve_pm_weather_img = ImageTk.PhotoImage(twelve_pm_weather_img)
    twelve_pm = tk.Label(f2, image=twelve_pm_weather_img, bg=dt.get_bg_colour())
    twelve_pm.img = twelve_pm_weather_img
    twelve_pm.grid(row=7, column=2)

    three_pm_img = dt.weather_symbol(current_weather=f'{dt.three_pm}', size='small')
    three_pm_weather_img = Image.open(three_pm_img)
    three_pm_weather_img = ImageTk.PhotoImage(three_pm_weather_img)
    three_pm = tk.Label(f2, image=three_pm_weather_img, bg=dt.get_bg_colour())
    three_pm.img = three_pm_weather_img
    three_pm.grid(row=7, column=3)

    back_button = tk.Button(f2, text='Back', highlightcolor='black', fg="black", command=load_frame1,
                            highlightbackground=dt.get_bg_colour())
    back_button.grid(row=8, column=0, padx=215, columnspan=4)


# initialisation of the frames
f1 = tk.Frame(root, width=500, height=800, bg='#B8E8FC')
f2 = tk.Frame(root, width=500, height=800, bg=dt.get_bg_colour())

# place frame widgets in window
for frame in (f1, f2):
    frame.grid(row=0, column=0, sticky="nesw")

# load first frame
load_frame1()

root.mainloop()



