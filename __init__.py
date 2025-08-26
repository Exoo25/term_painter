from .color_utils import *
from .gradeint import *
from .rainbow import *
from pyfiglet import *
import sys
import os
import msvcrt
import curses 
# Reset
RESET = "\x1b[0m"

# Styles
BOLD      = "\x1b[1m"
DIM       = "\x1b[2m"
UNDERLINE = "\x1b[4m"
BLINK     = "\x1b[5m"
REVERSE   = "\x1b[7m"
HIDDEN    = "\x1b[8m"

# Normal Colors
BLACK   = "\x1b[30m"
RED     = "\x1b[31m"
GREEN   = "\x1b[32m"
YELLOW  = "\x1b[33m"
BLUE    = "\x1b[34m"
MAGENTA = "\x1b[35m"
CYAN    = "\x1b[36m"
WHITE   = "\x1b[37m"

# Bright Colors
BRIGHT_BLACK   = "\x1b[90m"
BRIGHT_RED     = "\x1b[91m"
BRIGHT_GREEN   = "\x1b[92m"
BRIGHT_YELLOW  = "\x1b[93m"
BRIGHT_BLUE    = "\x1b[94m"
BRIGHT_MAGENTA = "\x1b[95m"
BRIGHT_CYAN    = "\x1b[96m"
BRIGHT_WHITE   = "\x1b[97m"

# Background Colors
BG_BLACK   = "\x1b[40m"
BG_RED     = "\x1b[41m"
BG_GREEN   = "\x1b[42m"
BG_YELLOW  = "\x1b[43m"
BG_BLUE    = "\x1b[44m"
BG_MAGENTA = "\x1b[45m"
BG_CYAN    = "\x1b[46m"
BG_WHITE   = "\x1b[47m"

# Bright Background Colors
BG_BRIGHT_BLACK   = "\x1b[100m"
BG_BRIGHT_RED     = "\x1b[101m"
BG_BRIGHT_GREEN   = "\x1b[102m"
BG_BRIGHT_YELLOW  = "\x1b[103m"
BG_BRIGHT_BLUE    = "\x1b[104m"
BG_BRIGHT_MAGENTA = "\x1b[105m"
BG_BRIGHT_CYAN    = "\x1b[106m"
BG_BRIGHT_WHITE   = "\x1b[107m"
def color_text(text: str, *styles):
    """
    Colorize text with given ANSI codes.
    Example:
        color_text("Hello", BRIGHT_RED, BOLD)
    """
    return "".join(styles) + text + RESET
def heading(text: str, font: str, *styles : tuple):
    """
    Create a heading using pyfiglet and colorize it.
    Example:
        heading("Hello", "slant", BRIGHT_BLUE, BOLD)
    """
    figlet_text = figlet_format(text, font=font)
    print(color_text(figlet_text, *styles))
def button(text: str, *styles: tuple, function=None, bg_color=BLACK):
    """
    Create a clickable button in the terminal with text and background color.
    Example:
        button("Click Me", BRIGHT_GREEN, BOLD, function=lambda: print("Button Pressed!"), bg_color=BG_BLACK)
    """
    def draw_button(selected=False):
        os.system('cls' if os.name == 'nt' else 'clear')
        if selected:
            # Highlight selection with REVERSE
            print(color_text(f" {text} ", *styles, bg_color, REVERSE))
        else:
            print(color_text(f" {text} ", *styles, bg_color))

    selected = False
    draw_button(selected)

    while True:
        key = msvcrt.getch()
        if key == b'\r':  # Enter key
            if function:
                function()
            break
        elif key in (b'\x1b', b'q'):  # Esc or 'q' to quit
            break
        elif key == b'\t':  # Tab key to toggle selection
            selected = not selected
            draw_button(selected)
def entry(prompt: str, *styles: tuple, bg_color=BG_WHITE):
    """
    Create a styled input prompt in the terminal.
    Example:
        name = entry("Enter your name: ", BRIGHT_CYAN, BOLD, bg_color=BG_BLACK)
    """
    styled_prompt = color_text(prompt, *styles, bg_color)
    return input(styled_prompt)
