import tkinter as tk
from tkinter import ttk

colorscheme = {
    "dark": "#0f1012",
    "darkh": "#22242a",
    "grey": "#4c494a",
    "lightgrey": "#d8dada",
    # "lightgrey": "#dfe2e7",
    "light": "#fffefe",
    "lighth": "#f1f3f3",
    "accent": "#fc6373",
    "accenth": "#ff5577",
    "hover": "#dfe2e7",
    "ahover": "#fc647e",
}


def style(root):
    style = ttk.Style(root)
    style.theme_use("clam")

    # style definitions
    # Button:
    font = ("Inter Light", 11)
    bold = ("Inter", 11)
    header = ("Inter", 12)
    bigfont = ("Inter", 13)
    smallfont = ("Inter Light", 9)

    style.configure(".", bg=colorscheme["light"], font=font)
    style.configure(
        "TButton",
        background=colorscheme["light"],
        lightcolor=colorscheme["lightgrey"],
        darkcolor=colorscheme["lightgrey"],
        foreground=colorscheme["dark"],
        bordercolor=colorscheme["dark"],
        focuscolor=colorscheme["light"],
        focusthickness=1,
        borderwidth=2,
        # relief=tk.FLAT,
    )
    style.map(
        "TButton",
        background=[
            ("pressed", colorscheme["hover"]),
            ("active", colorscheme["lighth"]),
            ("disabled", colorscheme["lightgrey"]),
        ],
        lightcolor=[("pressed", colorscheme["lighth"])],
        darkcolor=[("pressed", colorscheme["lighth"])],
        bordercolor=[("pressed", colorscheme["grey"])],
        focuscolor=[("pressed", colorscheme["light"])],
    )
    style.configure(
        "accent.TButton",
        background=colorscheme["accent"],
        lightcolor=colorscheme["accent"],
        darkcolor=colorscheme["accent"],
        foreground=colorscheme["light"],
        bordercolor=colorscheme["dark"],
        focuscolor=colorscheme["accent"],
        borderwidth=2,
        font=header,
    )
    style.map(
        "accent.TButton",
        background=[
            ("pressed", colorscheme["ahover"]),
            ("active", colorscheme["accenth"]),
            ("disabled", colorscheme["lightgrey"]),
        ],
        lightcolor=[("pressed", colorscheme["accenth"])],
        darkcolor=[("pressed", colorscheme["accenth"])],
        focuscolor=[("pressed", colorscheme["accent"])],
        bordercolor=[("pressed", colorscheme["dark"])],
    )
    style.configure(
        "dark.TButton",
        foreground=colorscheme["light"],
        background=colorscheme["dark"],
        lightcolor=colorscheme["dark"],
        darkcolor=colorscheme["dark"],
        bordercolor=colorscheme["dark"],
        focuscolor=colorscheme["darkh"],
        borderwidth=2,
        padding=(6, 2),
        font=header,
    )
    style.map(
        "dark.TButton",
        background=[
            ("pressed", colorscheme["dark"]),
            ("active", colorscheme["darkh"]),
            ("disabled", colorscheme["lightgrey"]),
        ],
        foreground=[
            ("disabled", colorscheme["lighth"]),
        ],
        lightcolor=[("pressed", colorscheme["darkh"])],
        darkcolor=[("pressed", colorscheme["darkh"])],
        focuscolor=[("pressed", colorscheme["darkh"])],
        bordercolor=[("pressed", colorscheme["darkh"])],
    )

    style.configure(
        "TLabel",
        foreground=colorscheme["dark"],
        background=colorscheme["light"],
        borderwidth=0,
        sticky=tk.CENTER,
        relief=tk.SOLID,
        # padding=(10, 2),
    )
    style.map(
        "TLabel",
        foreground=[
            ("disabled", colorscheme["lightgrey"]),
        ],
    )
    style.configure("big.TLabel", font=bigfont, padding=6, anchor=tk.CENTER)
    style.configure("small.TLabel", font=smallfont, padding=(0, 6, 0, 0))

    style.configure(
        "TFrame",
        background=colorscheme["light"],
        borderwidth=2,
        bd=0,
    )
    style.configure(
        "border.TFrame",
        background=colorscheme["light"],
        lightcolor=colorscheme["dark"],
        darkcolor=colorscheme["dark"],
        bordercolor=colorscheme["dark"],
    )
    style.configure(
        "border.TFrame.border",
        borderwidth=2,
        bordercolor=colorscheme["dark"],
    )
    style.configure(
        "hr.TFrame",
        background=colorscheme["grey"],
        lightcolor=colorscheme["light"],
        darkcolor=colorscheme["light"],
        bordercolor=colorscheme["light"],
        width=3
    )

    style.configure(
        "TPanedwindow",
        background=colorscheme["light"],
        bd=0,
        borderwidth=0,
    )

    style.configure(
        "TEntry",
        fieldbackground=colorscheme["light"],
        bordercolor=colorscheme["dark"],
        lightcolor=colorscheme["lighth"],
        darkcolor=colorscheme["lighth"],
        insertcolor=colorscheme["accent"],
        insertwidth=2,
        borderwidth=4,
        bd=0,
        padding=(6, 6),
        relief=tk.FLAT,
    )
    style.map(
        "TEntry",
        bordercolor=[
            ("focus", colorscheme["accent"]),
            ("disabled", "#c2c4ca"),
        ],
        lightcolor=[("focus", colorscheme["accent"])],
    )

    style.layout(
        "TCheckbutton",
        [
            (
                "Checkbutton.padding",
                {
                    "sticky": "nswe",
                    "children": [
                        (
                            "Checkbutton.indicator",
                            {"side": "top", "sticky": "s"},
                        ),
                        (
                            "Checkbutton.focus",
                            {
                                "side": "top",
                                "sticky": "nswe",
                            },
                        ),
                    ],
                },
            )
        ],
    )

    style.configure(
        "TCheckbutton",
        relief=tk.FLAT,
        indicatorforeground=colorscheme["accent"],
        indicatorbackground=colorscheme["light"],
        upperbordercolor=colorscheme["dark"],
        lowerbordercolor=colorscheme["dark"],
        background=colorscheme["light"],
        focuscolor=colorscheme["light"],
        indicatorsize=10,
        padding=(4, 2),
    )

    style.layout("Notebook", [])
    style.element_create("Plain.Notebook.tab", "from", "clam")
    style.layout(
        "TNotebook.Tab",
        [
            (
                "Plain.Notebook.tab",
                {
                    "children": [
                        (
                            "Notebook.border",
                            {
                                "children": [
                                    (
                                        "Notebook.padding",
                                        {
                                            "side": "top",
                                            "children": [
                                                (
                                                    "Notebook.focus",
                                                    {
                                                        "side": "top",
                                                        "children": [
                                                            (
                                                                "Notebook.label",
                                                                {
                                                                    "side": "top",
                                                                    "sticky": "ns",
                                                                },
                                                            )
                                                        ],
                                                        "sticky": "nswe",
                                                    },
                                                )
                                            ],
                                            "sticky": "nswe",
                                        },
                                    )
                                ],
                                "sticky": "nswe",
                            },
                        )
                    ],
                    "sticky": "nswe",
                },
            )
        ],
    )

    style.configure(
        "TNotebook",
        bordercolor=colorscheme["lightgrey"],
        borderwidth=0,
        background=colorscheme["light"],
        padding=(6, 10),
        bd=0,
        lightcolor=colorscheme["lighth"],
        darkcolor=colorscheme["light"],
        tabposition="n",
    )

    style.configure(
        "TNotebook.Tab",
        background=colorscheme["lighth"],
        bordercolor=colorscheme["lightgrey"],
        focuscolor=colorscheme["light"],
        font=bold,
        relief="flat",
        # borderwidth=20,
    )
    style.map("TNotebook.Tab", background=[("selected", colorscheme["light"])])

    style.configure(
        "ribbon.TNotebook",
        tabposition="wn",
        bordercolor=colorscheme["light"],
        padding=(6),
        tabmargins=0,
    )
    style.configure(
        "ribbon.TNotebook.Tab",
        background=colorscheme["lightgrey"],
        bordercolor=colorscheme["light"],
        lightcolor=colorscheme["dark"],
        darkcolor=colorscheme["dark"],
        focuscolor=colorscheme["light"],
        font=bold,
        bd=0,
        borderwidth=6,
        padding=0,
    )
    style.map(
        "ribbon.TNotebook.Tab",
        background=[("selected", colorscheme["light"])],
        padding=[("selected", 0)],
    )

    style.configure(
        "TMenubutton",
        bordercolor=colorscheme["grey"],
        borderwidth=2,
        background=colorscheme["lighth"],
        padding=(4, 4),
        darkcolor=colorscheme["light"],
        lightcolor=colorscheme["light"],
        relief="flat",
        font=font,
    )
    style.configure(
        "Treeview",
        background=colorscheme["light"],
        fieldbackground=colorscheme["lighth"],
        bordercolor=colorscheme["grey"],
        font=font
    )

    style.configure(
        "menubtn.TButton",
        borderwidth=0,
        bordercolor=colorscheme["light"],
        foreground=colorscheme["light"],
        background=colorscheme["dark"],
        lightcolor=colorscheme["dark"],
        darkcolor=colorscheme["dark"],
        focuscolor=colorscheme["darkh"],
    )
    style.map(
        "menubtn.TButton",
        background=[
            ("active", colorscheme["grey"]),
            ("pressed", colorscheme["grey"]),
            ("disabled", colorscheme["lightgrey"]),
        ],
        foreground=[
            ("disabled", colorscheme["lighth"]),
        ],
        lightcolor=[("pressed", colorscheme["grey"])],
        darkcolor=[("pressed", colorscheme["grey"])],
        focuscolor=[("pressed", colorscheme["grey"])],
        bordercolor=[("pressed", colorscheme["grey"])],
    )

    style.configure(
        "verticalNavMenu.TButton",
        background=colorscheme["lightgrey"],
        foreground=colorscheme["dark"],
        darkcolor=colorscheme["lightgrey"],
        lightcolor=colorscheme["lightgrey"],
        bordercolor=colorscheme["lightgrey"],
        focusthickness=0,
        borderwidth=2,
        # relief=tk.FLAT,
    )
    style.map(
        "verticalNavMenu.TButton",
        background=[
            ("active", colorscheme["lighth"]),
            ("disabled", colorscheme["lightgrey"]),
            ("pressed", colorscheme["light"]),
        ],
        lightcolor=[
            ("pressed", colorscheme["light"]),
            ("active", colorscheme["lighth"]),
        ],
        darkcolor=[
            ("pressed", colorscheme["light"]),
            ("active", colorscheme["lighth"]),
        ],
        bordercolor=[
            ("pressed", colorscheme["light"]),
            ("active", colorscheme["lighth"]),
        ],
        focuscolor=[
            ("pressed", colorscheme["lighth"]),
            ("active", colorscheme["light"]),
        ],
    )
    style.configure(
        "verticalNavMenu.TFrame",
        background=colorscheme["lightgrey"],
        lightcolor=colorscheme["lightgrey"],
        darkcolor=colorscheme["lightgrey"],
        bordercolor=colorscheme["grey"],
        highlightcolor=colorscheme["grey"],
        borderwidth=2,
    )

    return style


if __name__ == "__main__":
    root = tk.Tk()
    s = style(root)
    print(s.layout("Treeview.Heading"))

    root.mainloop()
