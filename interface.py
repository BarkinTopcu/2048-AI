import tkinter as tk
from tkinter import ttk


""" 
This class is created todraw game interface and some game info such as game status.

Author: Recep Barkın Topcu
Date: January 31, 2025
Version: 1.0

"""

class Interface:


    def __init__(self,root):
        self.root = root
        self.selected_agent = None
        self.selected_mode = None
        self.game_status = None
        self.shape_colors = {
            2: ["#EEE4DA", "#776E65"],
            4: ["#EDE0C8", "#776E65"],
            8: ["#F2B179", "#F9F6F2"],
            16: ["#F59563", "#F9F6F2"],
            32: ["#F67C5F", "#F9F6F2"],
            64: ["#F65E3B", "#F9F6F2"],
            128: ["#EDCF72", "#F9F6F2"],
            256: ["#EDCC61", "#F9F6F2"],
            512: ["#EDC850", "#F9F6F2"],
            1024: ["#EDC53F", "#F9F6F2"],
            2048: ["#EDC22E", "#F9F6F2"],
            "above_2048": ["#3C3A32", "#F9F6F2"],
            0: "#CDC1B4"
        }
        self.grid_numbers = None
    
    def game_start(self):
        self.game_status = "Start"
        self.canvas.forget()
        self.mode_frame.place_forget()
        self.agent_frame.place_forget()
        self.start_button.place_forget()
        self.single_game()
        

    def menu(self):
        """ The function that draw the main menu components """
        #Game Welcome Message
        self.canvas = tk.Canvas(self.root, width=500, height=700, bg="white")
        self.canvas.pack()
        self.canvas.create_rectangle(50, 50, 450, 150, fill="lightblue")
        self.canvas.create_text(250, 100, text="Welcome to 2048 - AI Game", font=("Arial", 16))

        #Mode selection frame
        self.mode_frame = tk.Frame(self.root, bg="white")
        self.mode_frame.place(x=50, y=180, width=400, height=40)

        mode_label = ttk.Label(self.mode_frame, text="Mode:", font=("Arial", 14),background="white")
        mode_label.grid(row=1, column=0, padx=5, pady=5)
        mode_combo= tk.StringVar()
        mode_dropdown = ttk.Combobox(self.mode_frame, textvariable=mode_combo, font=("Arial", 12), state="readonly")
        mode_dropdown['values'] = ("Single","Agent","Competition")
        mode_dropdown.grid(row=1, column=1, padx=5, pady=5)

        #AI agent frame
        self.agent_frame = tk.Frame(self.root, bg="white")
        self.agent_frame.place(x=50, y=220, width=400, height=40)
        AI_label = ttk.Label(self.agent_frame, text="AI Agent:", font=("Arial", 14),background="white")
        AI_label.grid(row=1, column=0, padx=5, pady=5)
        AI_combo_var = tk.StringVar()
        AI_dropdown = ttk.Combobox(self.agent_frame, textvariable=AI_combo_var, font=("Arial", 12), state="readonly")
        AI_dropdown['values'] = ("AI - 1", "AI - 2", "AI - 3", "AI - 4")
        AI_dropdown.grid(row=1, column=1, padx=5, pady=5)

        #Start button
        self.start_button = ttk.Button(self.root, text="Start Game", command=self.game_start)
        self.start_button.place(x=200, y=270)
    
    def single_game(self):
        numbers = [2,4,8,16,32,64,128,256,1024,2048,2,2,2,2,2,2]
        tile_size = 60
        left_padding = 125
        top_padding = 80
        box_padding = 3
        self.grid_frame = tk.Frame(self.root, bg="#a38b79")
        self.grid_frame.place(x=left_padding-box_padding*2, y=top_padding-box_padding*2, width=tile_size*4+6*box_padding, height=tile_size*4+5*box_padding)

        labels = []
        for row in range(4):
            for col in range(4):
                value = numbers[row * 4 + col]
                bg_color = self.shape_colors[value][0]
                font_color = self.shape_colors[value][1]
                label = tk.Label(
                    self.root,
                    text=str(value),
                    font=("Arial", 16, "bold"),
                    width=4,
                    height=2,
                    borderwidth=2,
                    relief="ridge",
                    bg=bg_color,
                    fg=font_color
                )
                label.place(x=col * (tile_size + box_padding) + left_padding, 
                            y=row * (tile_size + box_padding) + top_padding)
                labels.append(label)
        pass




    