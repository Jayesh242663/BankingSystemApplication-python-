import tkinter as tk

class HoverButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        tk.Button.__init__(self, master, **kwargs)
        self.default_fg_color = kwargs.get('fg', 'gray')
        self.hover_fg_color = 'Black'
        self.default_bg_color = kwargs.get('bg', self.master['bg'])
        self.hover_bg_color = '#FFFFFF'
        self.config(
            font=("Tahoma", 16, "bold"),
            relief=tk.FLAT,
            bd=2
        )
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        self.config(fg=self.hover_fg_color, bg=self.hover_bg_color)

    def on_leave(self, event):
        self.config(fg=self.default_fg_color, bg=self.default_bg_color)
