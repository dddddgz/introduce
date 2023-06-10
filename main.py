from rich.console import Console
from time import sleep
from os import system

system("cls")

console = Console()
print = console.print

s = """\
    d      d      d      d      d
    d      d      d      d      d
 dddd   dddd   dddd   dddd   dddd   ggg   zzzzz
d   d  d   d  d   d  d   d  d   d  g   g    zz
d   d  d   d  d   d  d   d  d   d  g   g   zz
ddddd  ddddd  ddddd  ddddd  ddddd   gggg  zzzzz
                                       g
                                    gggg
"""
colors = ["blue", "red", "green"]
di, gi, zi = 0, 1, 2
while True:
    di += 1
    di %= 3
    gi += 1
    gi %= 3
    zi += 1
    zi %= 3
    dc, gc, zc = colors[di], colors[gi], colors[zi]
    for line in s.splitlines():
        for each in line:
            if each == "d":
                each = f"[{dc}]{each}[/]"
            elif each == "g":
                each = f"[{gc}]{each}[/]"
            elif each == "z":
                each = f"[{zc}]{each}[/]"
            print(each, end='')
        print()
    sleep(0.1)
    print("\033c")
