from tkinter import ALL
from question import *
from constants import *
import random

class IdentifiyProgressionModes(Question):

    def __init__(self, root, mode, num_chords) -> None:
        self.root = root
        self.mode = mode
        self.notes = ALL_MODES[self.root][self.mode]
        self.num_chords = num_chords
        self.chord_numbers = random.sample(range(1, 8), self.num_chords)

        answer = [self.notes[i - 1] + MODES_CHORDS[self.mode][i - 1] for i in self.chord_numbers]
        prompt = "In " + self.root + " " + self.mode + ", what chords make up the " + str(self.chord_numbers) + " progression?"
        answer_inputs = [LIST_OF_NOTES, MODES_CHORDS[self.mode]]

        super().__init__(prompt, answer, answer_inputs)

class IdentifyNotesMode(Question):

    def __init__(self, root, mode) -> None:
        self.root = root
        self.mode = mode

        answer = ALL_MODES[self.root][self.mode]
        prompt = "Given the mode " + self.root + " " + self.mode + ", what are the notes of this mode?"
        answer_inputs = LIST_OF_NOTES

        super().__init__(prompt, answer, answer_inputs)

class IdentifyModeGivenNotes(Question):

    def __init__(self, root, mode) -> None:
        self.root = root
        self.notes = ALL_MODES[root][mode]

        answer = mode
        prompt = "Given the notes " + str(self.notes) + ", what is the associated mode of " + self.root + "?"
        answer_inputs = LIST_OF_MODES

        super().__init__(prompt, answer, answer_inputs)

class IdentifyNoteWithTones(Question):

    def __init__(self, note, num_semi_tones) -> None:
        self.note = note
        self.num_semi_tones = num_semi_tones
        initial_index = LIST_OF_NOTES.index(self.note)
        new_index = (initial_index + num_semi_tones) % 12


        answer = LIST_OF_NOTES[new_index]
        prompt = "Which note is +" + str(round(self.num_semi_tones / 2)) + " tones away from " + self.note + "?"
        answer_inputs = LIST_OF_NOTES
        super().__init__(prompt, answer, answer_inputs)

print("\n\n")
test = IdentifiyProgressionModes("A", "Ionian", 4)
test.make_verbose()
print("\n\n")

test = IdentifyNotesMode("A", "Ionian")
test.make_verbose()
print("\n\n")

test = IdentifyModeGivenNotes("A", "Ionian")
test.make_verbose()
print("\n\n")

test = IdentifyNoteWithTones("A", 4)
test.make_verbose()
print("\n\n")