# term_painter/rainbow.py
import time, sys
from .gradeint import gradient

def rainbow(text: str, speed: float = 0.05):
    """Continuously print text with rainbow colors."""
    colors = ["#ff0000", "#ff7f00", "#ffff00", "#00ff00", "#0000ff", "#4b0082", "#8b00ff"]
    while True:
        for i in range(len(colors)):
            start = colors[i]
            end = colors[(i + 1) % len(colors)]
            sys.stdout.write("\r" + gradient(text, start, end))
            sys.stdout.flush()
            time.sleep(speed)
