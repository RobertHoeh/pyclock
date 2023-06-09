import time as t
"""provides a simple clock interface
might implement customizable text size/ fancy text."""

class clock:
    def __init__(self, w, h12):
        self.w = w
        self.format = h12

    def disp(self):
        return [
                {
                "content": t.strftime("%I"),
                "x": 2,
                "y": 5
            }
        ]
    def input(self):
        return [{}]