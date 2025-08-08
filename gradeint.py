# term_painter/gradient.py
from .color_utils import gradient_colors, rgb_to_ansi

RESET = "\033[0m"

def gradient(text: str, start: str, end: str) -> str:
    """Return text with gradient colors applied."""
    colors = gradient_colors(start, end, len(text))
    return "".join(
        f"{rgb_to_ansi(r, g, b)}{char}"
        for char, (r, g, b) in zip(text, colors)
    ) + RESET
