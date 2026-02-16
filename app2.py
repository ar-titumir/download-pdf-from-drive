import tkinter as tk
from gui import PDFDownloaderGUI


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFDownloaderGUI(root)
    root.mainloop()
