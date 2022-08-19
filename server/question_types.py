from tkinter import ALL
from question import *
from constants import *
import random

class IdentifiyProgressionModes(Question):

    def __init__(self) -> None:
        super().__init__()
        self.worth = 6

    def generate_random(self) -> None:
        root = random.choice(LIST_OF_NOTES)
        mode = random.choice(LIST_OF_MODES)
        notes = ALL_MODES[root][mode]
        number_of_chords = random.choice(range(3,8))
        progression = random.sample(range(1, 8), number_of_chords)

        self.answer = [notes[i - 1] + MODES_CHORDS[mode][i - 1] for i in progression]
        self.prompt = "In " + root + " " + mode + ", what chords make up the " + str(progression) + " progression?"
        self.answer_inputs = [LIST_OF_NOTES, MODES_CHORDS[mode]]

class IdentifyNotesMode(Question):

    def __init__(self) -> None:
        super().__init__()
        self.worth = 3
        
    def generate_random(self) -> None:
        root = random.choice(LIST_OF_NOTES)
        mode = random.choice(LIST_OF_MODES)

        self.answer = ALL_MODES[root][mode]
        self.prompt = "Given the mode " + root + " " + mode + ", what are the notes of this mode?"
        self.answer_inputs = LIST_OF_NOTES

class IdentifyModeGivenNotes(Question):

    def __init__(self) -> None:
        super().__init__()
        self.worth = 3

    def generate_random(self) -> None:
        root = random.choice(LIST_OF_NOTES)
        mode = random.choice(LIST_OF_MODES)
        notes = ALL_MODES[root][mode]

        self.answer = mode
        self.prompt = "Given the notes " + str(notes) + ", what is the associated mode of " + root + "?"
        self.answer_inputs = LIST_OF_MODES

class IdentifyNoteWithTones(Question):

    def __init__(self) -> None:
        super().__init__()
        self.worth = 1
    
    def generate_random(self) -> None:
        note = random.choice(LIST_OF_NOTES)
        semi_tones = random.randint(1, 12)
        start_index = LIST_OF_NOTES.index(note)
        end_index = (start_index + semi_tones) % 12

        self.answer = LIST_OF_NOTES[end_index]
        self.prompt = "Which note is +" + str(round(semi_tones / 2, 1)) + " tones away from " + note + "?"
        self.answer_inputs = LIST_OF_NOTES
