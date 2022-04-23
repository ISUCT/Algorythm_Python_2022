#
# Quake light flickering
# Styles from https://github.com/id-Software/Quake/blob/master/qw-qc/world.qc
#

from time import sleep as delay

FLICKER_TIME = 100 / 1000                                   # Flicker time = 100 ms
LIGHT_STYLES = [
    'm',                                                    # 0  normal
    'mmnmmommommnonmmonqnmmo',                              # 1  flicker (first variety)
    'abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba',  # 2  slow strong pulse
    'mmmmmaaaaammmmmaaaaaabcdefgabcdefg',                   # 3  candle (first variety)
    'mamamamamama',                                         # 4  fast strobe
    'jklmnopqrstuvwxyzyxwvutsrqponmlkj',                    # 5  GENTLE pulse 1
    'nmonqnmomnmomomno',                                    # 6  flicker (second variety)
    'mmmaaaabcdefgmmmmaaaammmaamm',                         # 7  candle (second variety)
    'mmmaaammmaaammmabcdefaaaammmmabcdefmmmaaaa',           # 8  candle (third variety)
    'aaaaaaaazzzzzzzz',                                     # 9  slow strobe (fourth variety)
    'mmamammmmammamamaaamammma',                            # 10 fluorescent flicker
    'abcdefghijklmnopqrrqponmlkjihgfedcba',                 # 11 slow pulse not fade to black
]
STYLES_COUNT = len(LIGHT_STYLES)

def remap(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def run_light(style):
    value = 0
    for char in LIGHT_STYLES[style]:
        value = ord(char) - ord('a')                        # Get the value from 'a' to 'z' from the string array minus 'a'
        value = remap(value, 0, 25, 0, 255)                 # Convert from 0 - 25 to 0 - 255
        print(value)
        delay(FLICKER_TIME)                                 # Wait the time for one step

if __name__ == '__main__':
    for style in range(STYLES_COUNT):
        print(style)
        run_light(style)