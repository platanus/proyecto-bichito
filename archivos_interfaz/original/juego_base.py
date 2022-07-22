from tkinter import Tk, Canvas, Frame
from threading import Thread

WIDTH = 404
SCOREBOARD_HEIGHT = 70
HEIGHT = WIDTH + SCOREBOARD_HEIGHT
SIZE = 98
MARGIN = 12

FONT_SIZES = {1: '48', 2: '45', 3: '38', 4: '28', 5: '24', 6: '18'}
TILE_COLORS = {
    '0': ['#cdc1b5', '#cdc1b5'],
    '2': ['#eee4da', '#776e65'],
    '4': ['#ede0c8', '#776e65'],
    '8': ['#f2b179', '#f9f6f2'],
    '16': ['#f59563', '#f9f6f2'],
    '32': ['#f67c5f', '#f9f6f2'],
    '64': ['#f65e3b', '#f9f6f2'],
    '128': ['#edcf72', '#f9f6f2'],
    '256': ['#edcc61', '#f9f6f2'],
    '512': ['#edc850', '#f9f6f2'],
    '1024': ['#edc53f', '#f9f6f2'],
    '2048': ['#edc22e', '#f9f6f2'],
    'big': ['#3c3a32', '#f9f6f2'],
}


class Canvas(Canvas):
    def create_rounded_rectangle(self, x1, y1, x2, y2, r=10, **kwargs):
        points = [x1 + r, y1, x1 + r, y1, x2 - r, y1, x2 - r, y1, x2, y1, x2, y1 + r, x2, y1 + r,
                  x2, y2 - r, x2, y2 - r, x2, y2, x2 - r, y2, x2 - r, y2, x1 + r, y2, x1 + r, y2,
                  x1, y2, x1, y2 - r, x1, y2 - r, x1, y1 + r, x1, y1 + r, x1, y1]
        return self.create_polygon(points, **kwargs, smooth=True, outline='')


class Tile:
    def __init__(self, left, top, right, bottom, canvas, text=''):
        self.canvas = canvas
        text_offset = (right - left) / 2
        self.shape = self.canvas.create_rounded_rectangle(left, top, right, bottom, fill='#cdc1b5')
        self.text = self.canvas.create_text(left + text_offset, top + text_offset, text=text)

    @property
    def value(self):
        return int(self.canvas.itemcget(self.text, 'text') or 0)

    @value.setter
    def value(self, value):
        text, old_text = str(value), str(self.value)
        background, foreground = TILE_COLORS[text] if text in TILE_COLORS else TILE_COLORS['big']
        font_size = FONT_SIZES[len(text)] if len(text) in FONT_SIZES else FONT_SIZES['big']
        font = ('Clear Sans', font_size, 'bold')
        self.canvas.itemconfig(self.text, fill=foreground, text=text, font=font)
        self.canvas.itemconfig(self.shape, fill=background)


class Scoreboard:
    def __init__(self, left, top, right, bottom, canvas, score=0):
        self._score = score
        self.canvas = canvas
        self.score_title = self.canvas.create_text(
            left + (right - left) / 2,
            top + (bottom - top) / 2 - 1.2 * MARGIN,
            text='SCORE',
            fill='#eee4da',
            font=('Clear Sans', '14', 'bold')
        )
        self.score_text = self.canvas.create_text(
            left + (right - left) / 2,
            top + (bottom - top) / 2 + 0.8 * MARGIN,
            text=str(score),
            fill='#f9f6f2',
            font=('Clear Sans', '22', 'bold')
        )

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score
        self.canvas.itemconfig(self.score_text, text=str(score))


class Game(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tiles = []
        self.scoreboard = None
        self.last_key_pressed = None
        self.is_key_pressed = False
        self.protocol('WM_DELETE_WINDOW', self.handle_close)
        self.initialize()

    @property
    def values(self):
        return [i.value for i in self.tiles]

    @property
    def score(self):
        return self.scoreboard.score

    def initialize(self):
        self.title('Platanus - 2048')
        self.set_geometry()
        self.initialize_canvas()
        self.place_scoreboard()
        self.place_tiles()
        self.bind_keys()

    def handle_close(self):
        print('Exiting...')
        self.destroy()
        print('Bye')

    def set_geometry(self):
        x = self.winfo_screenwidth() // 2 - WIDTH // 2
        y = self.winfo_screenheight() // 2 - HEIGHT // 2
        self.geometry(f'{WIDTH}x{HEIGHT}+{x}+{y}')
        self.resizable(False, False)

    def initialize_canvas(self):
        self.canvas = Canvas(self, width=WIDTH, height=HEIGHT, bg='#bbada0', highlightthickness=0)
        self.canvas.pack()

    def place_scoreboard(self):
        self.scoreboard = Scoreboard(MARGIN, MARGIN, WIDTH - MARGIN, SCOREBOARD_HEIGHT, self.canvas)

    def place_tiles(self):
        for i in range(4):
            for j in range(4):
                left, top = j * SIZE + MARGIN, i * SIZE + MARGIN + SCOREBOARD_HEIGHT
                right, bottom = (j + 1) * SIZE, (i + 1) * SIZE + SCOREBOARD_HEIGHT
                self.tiles.append(Tile(left, top, right, bottom, self.canvas))

    def bind_keys(self):
        self.frame = Frame(self)
        self.frame.bind_all('<Key>', self.handler)

    def handler(self, event):
        self.last_key_pressed = event.keysym.lower()
        self.turn_function()

    def start(self, program):
        self.turn_function = program
        self.mainloop()

    def update_tiles(self, values):
        for i in range(len(values)):
            self.tiles[i].value = values[i]
        self.update_idletasks()

    def update_score(self, score):
        self.scoreboard.score = score


game = Game()


def obtener_valores():
    return game.values


def obtener_puntaje():
    return game.score


def tecla_apretada():
    return game.last_key_pressed


def actualizar_valores(values):
    game.update_tiles(values)


def actualizar_puntaje(score):
    game.update_score(score)


def iniciar(program):
    game.start(program)
