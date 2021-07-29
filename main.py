import tkinter as tk
import weather

api = '857da17a4a663a880b6369b38ecd6501'

root = tk.Tk()
root.title('Weather')
canvas = tk.Canvas(root, height=400, width=400)
canvas.pack()

img = tk.PhotoImage(file='./images/sky.png')
img_label = tk.Label(root, image=img)
img_label.place(relheight=1, relwidth=1)
ask_label = tk.Label(root, text="Enter your city below", bg='#2AB0E7', font=('courier', 20))
ask_label.place(anchor='c', relx=0.5, rely=0.15)
get_entry = tk.Entry(root)
get_entry.place(anchor='c', relheight=0.08,  relwidth=0.8, relx=0.5, rely=0.25)
out_label = tk.Label(root, bg='#ffffff')
out_label.place(anchor='c', relwidth=0.8, relheight=0.4, relx=0.5, rely=0.725)

def get_weather_init(location):
    get_weather = weather.Weather(location, api)#, units='metric')
    output = get_weather.quick_run()
    out_label.config(text=output)

run_button = tk.Button(root, text='Get weather', bg='#2AB0E7', font=('courier', 15), command=lambda:get_weather_init(get_entry.get()))
run_button.place(anchor='c', relx=0.5, rely=0.4)

def test(msg):
    out_label.config(text=f'Worked\nmessage: {msg}')

get_entry.bind('<Return>', lambda i:get_weather_init(get_entry.get()))

get_entry.focus()

root.mainloop()
