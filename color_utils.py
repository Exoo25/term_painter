# term_painter/color_utils.py

def hex_to_rgb(hex_color: str) -> tuple:
    """#ff00ff -> (255, 0, 255)"""
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_ansi(r: int, g: int, b: int) -> str:
    """Return ANSI escape code for RGB color."""
    return f"\033[38;2;{r};{g};{b}m"

def gradient_colors(start_hex: str, end_hex: str, steps: int):
    """Generate RGB colors for a gradient."""
    start = hex_to_rgb(start_hex)
    end = hex_to_rgb(end_hex)
    return [
        (
            int(start[0] + (end[0] - start[0]) * i / (steps - 1)),
            int(start[1] + (end[1] - start[1]) * i / (steps - 1)),
            int(start[2] + (end[2] - start[2]) * i / (steps - 1)),
        )
        for i in range(steps)
    ]
