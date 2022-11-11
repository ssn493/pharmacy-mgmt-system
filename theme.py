import tkinter as tk
from tkinter import ttk

colorscheme = {
    "dark": "#0f1012",
    "darkh": "#1c1d22",
    "grey": "#22242a",
    "lightgrey": "#e4e0dd",
    "light": "#fffeff",
    "lighth": "#f6f2f6",
    "accent": "#ff6376",
    "accenth": "#fa5972",
    "hover": "#fad4da",
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
        "TButton",
        background=[
            ("active", colorscheme["lighth"]),
            ("disabled", colorscheme["lightgrey"]),
        ],
        lightcolor=[("pressed", colorscheme["darkh"])],
        darkcolor=[("pressed", colorscheme["darkh"])],
        bordercolor=[("pressed", colorscheme["light"])],
        focuscolor=[("pressed", colorscheme["light"])],
    )
    style.map(
        "accent.TButton",
        background=[
            ("active", colorscheme["accenth"]),
            ("disabled", colorscheme["lightgrey"]),
        ],
        lightcolor=[("pressed", colorscheme["darkh"])],
        darkcolor=[("pressed", colorscheme["darkh"])],
        focuscolor=[("pressed", colorscheme["accent"])],
        bordercolor=[("pressed", colorscheme["dark"])],
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

    style.element_create("Plain.Notebook.tab", "from", "clam")
    style.layout(
        "TNotebook.Tab",
        [
            (
                "Plain.Notebook.tab",
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
                                                    {"side": "top", "sticky": ""},
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
        darkcolor=colorscheme["light"],
        lightcolor=colorscheme["light"],
        tabposition="n",
    )
    style.configure(
        "ribbon.TNotebook",
        tabposition="wn",
        bordercolor=colorscheme["light"],
        padding=10,
    )
    style.configure(
        "TNotebook.Tab",
        background=colorscheme["light"],
        bordercolor=colorscheme["lightgrey"],
        focuscolor=colorscheme["light"],
        font=bold
        # borderwidth=20,
    )
    style.map("TNotebook", background=[("selected", "green")])

    style.configure(
        "TMenubutton",
        bordercolor=colorscheme["grey"],
        borderwidth=2,
        background=colorscheme["lighth"],
        padding=(6, 6),
        darkcolor=colorscheme["light"],
        lightcolor=colorscheme["light"],
        relief="flat",
        font=font,
    )
    print(style.element_options("TMenubutton"))

    return style
