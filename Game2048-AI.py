import numpy as np
import tkinter as tk
from interface import Interface
import random

class Game2048_AI:

    def on_exit(self):
        pass

    def __init__(self):
        self.grid = np.zeros((4,4))
        self.point = 0
        pass

    def random_box(self):
        pass


    def main(self):
        root = tk.Tk()
        root.title("2048-AI Game")
        GUI = Interface(root)
        GUI.menu()

        # Ana döngüyü başlat
        root.mainloop()
if __name__ == "__main__":
    game = Game2048_AI()
    game.main()