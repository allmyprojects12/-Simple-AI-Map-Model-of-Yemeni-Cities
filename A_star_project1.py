import tkinter as tk
import random
import heapq

Cities = ["صنعاء","عدن","تعز","إب","ذمار","الحديدة","حجة","المحويت",
          "عمران","صعدة","مأرب","البيضاء","لحج","أبين","شبوة",
          "حضرموت","المهرة","الضالع","ريمة"]

city_coords = {
    "صنعاء": (390, 170),
    "عدن": (300, 440),
    "تعز": (260, 360),
    "إب": (300, 310),
    "ذمار": (340, 250),
    "الحديدة": (180, 270),
    "حجة": (160, 190),
    "المحويت": (220, 220),
    "عمران": (300, 160),
    "صعدة": (280, 80),
    "مأرب": (480, 200),
    "البيضاء": (420, 280),
    "لحج": (260, 400),
    "أبين": (360, 390),
    "شبوة": (560, 330),
    "حضرموت": (750, 280),
    "المهرة": (940, 260),
    "الضالع": (320, 340),
    "ريمة": (260, 250)

}

Cities_map = {
    "صنعاء":{"عمران":100,"ذمار":80,"مأرب":150,"ريمة":130,"البيضاء":200},
    "عدن":{"لحج":60,"أبين":80,"شبوة":100,"حضرموت":120,"المهرة":150},
    "تعز":{"إب":50,"الحديدة":120,"الضالع":70,"صنعاء":200,"البيضاء":180},
    "إب":{"تعز":50,"ذمار":70,"الحديدة":100,"صنعاء":180,"عمران":120},
    "ذمار":{"صنعاء":80,"إب":70,"عمران":60,"ريمة":110,"البيضاء":170},
    "الحديدة":{"تعز":120,"إب":100,"حجة":80,"المحويت":90,"صنعاء":200},
    "حجة":{"الحديدة":80,"صعدة":130,"المحويت":70,"صنعاء":220,"ذمار":150},
    "المحويت":{"حجة":70,"عمران":90,"صعدة":110,"الحديدة":90,"صنعاء":120},
    "عمران":{"صنعاء":100,"ذمار":60,"المحويت":90,"إب":120,"صعدة":130},
    "صعدة":{"حجة":130,"المحويت":110,"عمران":130,"ذمار":140,"صنعاء":150},
    "مأرب":{"صنعاء":150,"البيضاء":120,"ذمار":170,"إب":180,"حضرموت":250},
    "البيضاء":{"مأرب":120,"تعز":180,"إب":160,"صنعاء":200,"ريمة":190},
    "لحج":{"عدن":60,"أبين":50,"الضالع":70,"تعز":220,"شبوة":150},
    "أبين":{"عدن":80,"لحج":50,"شبوة":60,"حضرموت":180,"الضالع":220},
    "شبوة":{"عدن":100,"أبين":60,"حضرموت":120,"المهرة":200,"لحج":150},
    "حضرموت":{"شبوة":120,"المهرة":150,"مأرب":250,"عدن":220,"أبين":180},
    "المهرة":{"حضرموت":150,"شبوة":200,"عدن":250,"أبين":220,"لحج":280},
    "الضالع":{"تعز":70,"لحج":70,"إب":90,"أبين":120,"شبوة":150},
    "ريمة":{"ذمار":110,"صنعاء":130,"البيضاء":190,"صعدة":160,"إب":180}
}

city_coords = {
    "صنعاء": (390, 170),
    "عدن": (300, 440),
    "تعز": (260, 360),
    "إب": (300, 310),
    "ذمار": (340, 250),
    "الحديدة": (180, 270),
    "حجة": (160, 190),
    "المحويت": (220, 220),
    "عمران": (300, 160),
    "صعدة": (280, 80),
    "مأرب": (480, 200),
    "البيضاء": (420, 280),
    "لحج": (260, 400),
    "أبين": (360, 390),
    "شبوة": (560, 330),
    "حضرموت": (750, 280),
    "المهرة": (940, 260),
    "الضالع": (320, 340),
    "ريمة": (260, 250)

}

Cities_map = {
    "صنعاء":{"عمران":100,"ذمار":80,"مأرب":150,"ريمة":130,"البيضاء":200},
    "عدن":{"لحج":60,"أبين":80,"شبوة":100,"حضرموت":120,"المهرة":150},
    "تعز":{"إب":50,"الحديدة":120,"الضالع":70,"صنعاء":200,"البيضاء":180},
    "إب":{"تعز":50,"ذمار":70,"الحديدة":100,"صنعاء":180,"عمران":120},
    "ذمار":{"صنعاء":80,"إب":70,"عمران":60,"ريمة":110,"البيضاء":170},
    "الحديدة":{"تعز":120,"إب":100,"حجة":80,"المحويت":90,"صنعاء":200},
    "حجة":{"الحديدة":80,"صعدة":130,"المحويت":70,"صنعاء":220,"ذمار":150},
    "المحويت":{"حجة":70,"عمران":90,"صعدة":110,"الحديدة":90,"صنعاء":120},
    "عمران":{"صنعاء":100,"ذمار":60,"المحويت":90,"إب":120,"صعدة":130},
    "صعدة":{"حجة":130,"المحويت":110,"عمران":130,"ذمار":140,"صنعاء":150},
    "مأرب":{"صنعاء":150,"البيضاء":120,"ذمار":170,"إب":180,"حضرموت":250},
    "البيضاء":{"مأرب":120,"تعز":180,"إب":160,"صنعاء":200,"ريمة":190},
    "لحج":{"عدن":60,"أبين":50,"الضالع":70,"تعز":220,"شبوة":150},
    "أبين":{"عدن":80,"لحج":50,"شبوة":60,"حضرموت":180,"الضالع":220},
    "شبوة":{"عدن":100,"أبين":60,"حضرموت":120,"المهرة":200,"لحج":150},
    "حضرموت":{"شبوة":120,"المهرة":150,"مأرب":250,"عدن":220,"أبين":180},
    "المهرة":{"حضرموت":150,"شبوة":200,"عدن":250,"أبين":220,"لحج":280},
    "الضالع":{"تعز":70,"لحج":70,"إب":90,"أبين":120,"شبوة":150},
    "ريمة":{"ذمار":110,"صنعاء":130,"البيضاء":190,"صعدة":160,"إب":180}
}


cut_roads = []

def CutRoad(city1, city2):
    global cut_roads
    if city2 in Cities_map[city1]:
        del Cities_map[city1][city2]
        cut_roads.append((city1, city2))
    if city1 in Cities_map[city2]:
        del Cities_map[city2][city1]
        if (city2, city1) not in cut_roads:
            cut_roads.append((city2, city1))
    last_cut_label.config(text=f"آخر طريق مقطوع: {city1} ↔ {city2}")

def heuristic(city1, city2):
    x1, y1 = city_coords[city1]
    x2, y2 = city_coords[city2]
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def astar_solution(Cities_map, start, end):
    open_set = []
    heapq.heappush(open_set, (0, start, [start], 0))
    visited = set()
    while open_set:
        f, current_city, path, g = heapq.heappop(open_set)
        if current_city == end:
            return path, g
        if current_city in visited:
            continue
        visited.add(current_city)
        for neighbor, dist in Cities_map[current_city].items():
            if neighbor not in visited:
                g_new = g + dist
                f_new = g_new + heuristic(neighbor, end)
                heapq.heappush(open_set, (f_new, neighbor, path + [neighbor], g_new))
    return None, float('inf')

def draw_map(path=None):
    interface.delete("all")
    interface.create_rectangle(20,20,980,480, outline="black", width=2)
    for city,(x,y) in city_coords.items():
        interface.create_oval(x-15,y-15,x+15,y+15, fill="lightblue")
        interface.create_text(x,y, text=city, font=("Arial",8))
    if path:
        for i in range(len(path)-1):
            x1,y1 = city_coords[path[i]]
            x2,y2 = city_coords[path[i+1]]
            interface.create_line(x1,y1,x2,y2, fill="blue", width=3)
    for c1,c2 in cut_roads:
        if c1 in city_coords and c2 in city_coords:
            x1,y1 = city_coords[c1]
            x2,y2 = city_coords[c2]
            interface.create_line(x1,y1,x2,y2, fill="red", width=3, dash=(5,5))
            interface.create_oval(x1-3,y1-3,x1+3,y1+3, fill="red")
            interface.create_oval(x2-3,y2-3,x2+3,y2+3, fill="red")
    interface.create_line(820,50,880,50, fill="blue", width=3)
    interface.create_text(890,50, text=": طريق مفتوحة", anchor="w", font=("Arial",10))
    interface.create_line(820,70,880,70, fill="red", width=3, dash=(5,5))
    interface.create_oval(820-3,70-3,820+3,70+3, fill="red")
    interface.create_oval(880-3,70-3,880+3,70+3, fill="red")
    interface.create_text(890,70, text=": طريق مقطوعة", anchor="w", font=("Arial",10))

def counting_the_path():
    start = start_point.get()
    end = end_point.get()
    path, dist = astar_solution(Cities_map, start, end)
    draw_map(path)
    if path:
        result_label.config(text=f"المسار: {path}\nالمسافة: {dist} كم")
    else:
        result_label.config(text="!... لا يوجد طريق")

def btn_random_cut():
    path, _ = astar_solution(Cities_map, start_point.get(), end_point.get())
    if not path or len(path)<2:
        result_label.config(text="!... لا يوجد طريق لقطع عقبة")
        return
    i = random.randint(0,len(path)-2)
    city1,city2 = path[i], path[i+1]
    CutRoad(city1,city2)
    result_label.config(text=f"!... تم قطع الطريق بين {city1} و {city2}")
    counting_the_path()

def clear_all():
    global cut_roads
    cut_roads = []
    result_label.config(text="!... تم إعادة ضبط الخريطة")
    last_cut_label.config(text="آخر طريق مقطوع: لا يوجد")
    draw_map()

Main_form = tk.Tk()
Main_form.title(" A* خريطة اليمن مع خوارزمية ")

interface = tk.Canvas(Main_form, width=1000, height=500, bg="white")
interface.pack()

tk.Label(Main_form, text=": البداية").pack()
start_point = tk.StringVar(value="صنعاء")
tk.Entry(Main_form, textvariable=start_point).pack()

tk.Label(Main_form, text=": النهاية").pack()
end_point = tk.StringVar(value="عدن")
tk.Entry(Main_form, textvariable=end_point).pack()

buttons_frame = tk.Frame(Main_form)
buttons_frame.pack(pady=5)

tk.Button(buttons_frame, text="حساب المسار", command=counting_the_path, width=15).pack(side="right", padx=5)
tk.Button(buttons_frame, text="توليد عقبة", command=btn_random_cut, width=15).pack(side="right", padx=5)
tk.Button(buttons_frame, text="تنظيف الكل", command=clear_all, width=15).pack(side="right", padx=5)

result_label = tk.Label(Main_form, text=": ... المسار", font=("Arial",8,"bold"), fg="black")
result_label.pack(pady=5)

last_cut_label = tk.Label(Main_form, text="آخر طريق مقطوع: لا يوجد", font=("Arial",8), fg="red")
last_cut_label.pack(pady=5)

draw_map()
Main_form.mainloop()
