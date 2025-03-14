"""
PDF ve Word Dönüştürücü Uygulaması
Ana başlatıcı modül
"""

import tkinter as tk
import ttkbootstrap as ttk
from ui.app import FileConverterApp
from config.settings import APP_THEME, APP_TITLE

def main():
    """Ana uygulamayı başlatır"""
    root = ttk.Window(themename=APP_THEME)
    root.title(APP_TITLE)
    root.geometry("700x700")
    app = FileConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main() 