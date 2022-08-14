from question import *
from constants import *
import random

class IdentifiyProgressionModes(Question):

    def __init__(self, root, mode, num_chords) -> None:
        super().__init__()
        self.root = root
        self.mode = mode
        self.notes = ALL_MODES[root][mode]
        self.num_chords = num_chords
        self.chord_numbers = random.sample(range(1, 8), num_chords)
        self.answer = [self.notes[i - 1] + MODES_CHORDS[mode][i - 1] for i in self.chord_numbers]
        self.prompt = "In " + self.root + " " + self.mode + ", what chords make up the " + str(self.chord_numbers) + " progression?"

    def make_verbose(self):
        print("Root Note: " + self.root + "\nMode: " + self.mode + "\nNotes: " + str(self.notes) + "\nProgression: " + str(self.chord_numbers) + "\nAnswer: " + str(self.answer))

