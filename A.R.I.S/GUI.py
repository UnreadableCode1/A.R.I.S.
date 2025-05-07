import threading
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import builtins
import core

def wake_daughter():
    core.main

def setup_gui():
    root = tk.Tk()
    root.title("A.L.-1.S.")
    root.geometry("600x400")

    text_area = ScrolledText(root, wrap=tk.WORD, state=tk.NORMAL)
    text_area.pack(expand=True, fill=tk.BOTH)
    text_area.insert(tk.END, f"Waking A.L.-1.S. up...\n")
    text_area.see(tk.END)

    original_speak = core.speak
    def gui_speak(text):
        name = getattr(core, 'wake_word', 'A.L.-1.S.')
        text_area.insert(tk.END, f"{name}: {text}\n")
        text_area.see(tk.END)
        original_speak(text)
    core.speak = gui_speak

    original_print = builtins.print
    def gui_print(*args, **kwargs):
        original_print(*args, **kwargs)
        sep = kwargs.get('sep', ' ')
        end = kwargs.get('end', '\n')
        msg = sep.join(str(a) for a in args) + end
        text_area.insert(tk.END, msg)
        text_area.see(tk.END)
    builtins.print = gui_print

    core_thread = threading.Thread(target=wake_daughter, daemon=True)
    core_thread.start()

    root.mainloop()

if __name__ == "__main__":
    setup_gui()
