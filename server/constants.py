LIST_OF_NOTES = ["A", "A#/Bb", "B", "C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab"]
LIST_OF_MODES = ["Ionian", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Aeolian", "Locrian"]
MODES_TONES = {"Ionian": "TTSTTTS", "Dorian": "TSTTTST", "Phrygian": "STTTSTT", "Lydian": "TTTSTTS", 
               "Mixolydian": "TTSTTST", "Aeolian": "TSTTSTT", "Locrian": "STTSTTT"}
MODES_CHORDS = {"Ionian": ["M", "m7", "m7", "M7", "7", "m7", "Dim"], "Dorian": ["m7", "m7", "M7", "7", "m7", "Dim" "M"], 
                "Phrygian": ["m7", "M7", "7", "m7", "Dim", "M", "m7"], "Lydian": ["M7", "7", "m7", "Dim", "M", "m7", "m7"], 
                "Mixolydian": ["7", "m7", "Dim", "M", "m7", "m7", "M7"], "Aeolian": ["m7", "Dim", "M", "m7", "m7", "M7", "7"], 
                "Locrian": ["Dim", "M", "m7", "m7", "M7", "7", "m7"]}
ALL_MODES = {'A': {'Ionian': ['A', 'B', 'C#/Db', 'D', 'E', 'F#/Gb', 'G#/Ab'], 'Dorian': ['A', 'B', 'C', 'D', 'E', 'F#/Gb', 'G'], 'Phrygian': ['A', 'A#/Bb', 'C', 'D', 'E', 'F', 'G'], 'Lydian': ['A', 'B', 'C#/Db', 'D#/Eb', 'E', 'F#/Gb', 'G#/Ab'], 'Mixolydian': ['A', 'B', 'C#/Db', 'D', 'E', 'F#/Gb', 'G'], 'Aeolian': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'Locrian': ['A', 'A#/Bb', 'C', 'D', 'D#/Eb', 'F', 'G']}, 'A#/Bb': {'Ionian': ['A#/Bb', 'C', 'D', 'D#/Eb', 'F', 'G', 'A'], 'Dorian': ['A#/Bb', 'C', 'C#/Db', 'D#/Eb', 'F', 'G', 'G#/Ab'], 'Phrygian': ['A#/Bb', 'B', 'C#/Db', 'D#/Eb', 'F', 'F#/Gb', 'G#/Ab'], 'Lydian': ['A#/Bb', 'C', 'D', 'E', 'F', 'G', 'A'], 'Mixolydian': ['A#/Bb', 'C', 'D', 'D#/Eb', 'F', 'G', 'G#/Ab'], 'Aeolian': ['A#/Bb', 'C', 'C#/Db', 'D#/Eb', 'F', 'F#/Gb', 'G#/Ab'], 'Locrian': ['A#/Bb', 'B', 'C#/Db', 'D#/Eb', 'E', 'F#/Gb', 'G#/Ab']}, 'B': {'Ionian': ['B', 'C#/Db', 'D#/Eb', 'E', 'F#/Gb', 'G#/Ab', 'A#/Bb'], 'Dorian': ['B', 'C#/Db', 'D', 'E', 'F#/Gb', 'G#/Ab', 'A'], 'Phrygian': ['B', 'C', 'D', 'E', 'F#/Gb', 'G', 'A'], 'Lydian': ['B', 'C#/Db', 'D#/Eb', 'F', 'F#/Gb', 'G#/Ab', 'A#/Bb'], 'Mixolydian': ['B', 'C#/Db', 'D#/Eb', 'E', 'F#/Gb', 'G#/Ab', 'A'], 'Aeolian': ['B', 'C#/Db', 'D', 'E', 'F#/Gb', 'G', 'A'], 'Locrian': ['B', 'C', 'D', 'E', 'F', 'G', 'A']}, 'C': {'Ionian': ['C', 'D', 'E', 'F', 'G', 'A', 'B'], 'Dorian': ['C', 'D', 'D#/Eb', 'F', 'G', 'A', 'A#/Bb'], 'Phrygian': ['C', 'C#/Db', 'D#/Eb', 'F', 'G', 'G#/Ab', 'A#/Bb'], 'Lydian': ['C', 'D', 'E', 'F#/Gb', 'G', 'A', 'B'], 'Mixolydian': ['C', 'D', 'E', 'F', 'G', 'A', 'A#/Bb'], 'Aeolian': ['C', 'D', 'D#/Eb', 'F', 'G', 'G#/Ab', 'A#/Bb'], 'Locrian': ['C', 'C#/Db', 'D#/Eb', 'F', 'F#/Gb', 'G#/Ab', 'A#/Bb']}, 'C#/Db': {'Ionian': ['C#/Db', 'D#/Eb', 'F', 'F#/Gb', 'G#/Ab', 'A#/Bb', 'C'], 'Dorian': ['C#/Db', 'D#/Eb', 'E', 'F#/Gb', 'G#/Ab', 'A#/Bb', 'B'], 'Phrygian': ['C#/Db', 'D', 'E', 'F#/Gb', 'G#/Ab', 'A', 'B'], 'Lydian': ['C#/Db', 'D#/Eb', 'F', 'G', 'G#/Ab', 'A#/Bb', 'C'], 'Mixolydian': ['C#/Db', 'D#/Eb', 'F', 'F#/Gb', 'G#/Ab', 'A#/Bb', 'B'], 'Aeolian': ['C#/Db', 'D#/Eb', 'E', 'F#/Gb', 'G#/Ab', 'A', 'B'], 'Locrian': ['C#/Db', 'D', 'E', 'F#/Gb', 'G', 'A', 'B']}, 'D': {'Ionian': ['D', 'E', 'F#/Gb', 'G', 'A', 'B', 'C#/Db'], 'Dorian': ['D', 'E', 'F', 'G', 'A', 'B', 'C'], 'Phrygian': ['D', 'D#/Eb', 'F', 'G', 'A', 'A#/Bb', 'C'], 'Lydian': ['D', 'E', 'F#/Gb', 'G#/Ab', 'A', 'B', 'C#/Db'], 'Mixolydian': ['D', 'E', 'F#/Gb', 'G', 'A', 'B', 'C'], 'Aeolian': ['D', 'E', 'F', 'G', 'A', 'A#/Bb', 'C'], 'Locrian': ['D', 'D#/Eb', 'F', 'G', 'G#/Ab', 'A#/Bb', 'C']}, 'D#/Eb': {'Ionian': ['D#/Eb', 'F', 'G', 'G#/Ab', 'A#/Bb', 'C', 'D'], 'Dorian': ['D#/Eb', 'F', 'F#/Gb', 'G#/Ab', 'A#/Bb', 'C', 'C#/Db'], 'Phrygian': ['D#/Eb', 'E', 'F#/Gb', 'G#/Ab', 'A#/Bb', 'B', 'C#/Db'], 'Lydian': ['D#/Eb', 'F', 'G', 'A', 'A#/Bb', 'C', 'D'], 'Mixolydian': ['D#/Eb', 'F', 'G', 'G#/Ab', 'A#/Bb', 'C', 'C#/Db'], 'Aeolian': ['D#/Eb', 'F', 'F#/Gb', 'G#/Ab', 'A#/Bb', 'B', 'C#/Db'], 'Locrian': ['D#/Eb', 'E', 'F#/Gb', 'G#/Ab', 'A', 'B', 'C#/Db']}, 'E': {'Ionian': ['E', 'F#/Gb', 'G#/Ab', 'A', 'B', 'C#/Db', 'D#/Eb'], 'Dorian': ['E', 'F#/Gb', 'G', 'A', 'B', 'C#/Db', 'D'], 'Phrygian': ['E', 'F', 'G', 'A', 'B', 'C', 'D'], 'Lydian': ['E', 'F#/Gb', 'G#/Ab', 'A#/Bb', 'B', 'C#/Db', 'D#/Eb'], 'Mixolydian': ['E', 'F#/Gb', 'G#/Ab', 'A', 'B', 'C#/Db', 'D'], 'Aeolian': ['E', 'F#/Gb', 'G', 'A', 'B', 'C', 'D'], 'Locrian': ['E', 'F', 'G', 'A', 'A#/Bb', 'C', 'D']}, 'F': {'Ionian': ['F', 'G', 'A', 'A#/Bb', 'C', 'D', 'E'], 'Dorian': ['F', 'G', 'G#/Ab', 'A#/Bb', 'C', 'D', 'D#/Eb'], 'Phrygian': ['F', 'F#/Gb', 'G#/Ab', 'A#/Bb', 'C', 'C#/Db', 'D#/Eb'], 'Lydian': ['F', 'G', 'A', 'B', 'C', 'D', 'E'], 'Mixolydian': ['F', 'G', 'A', 'A#/Bb', 'C', 'D', 'D#/Eb'], 'Aeolian': ['F', 'G', 'G#/Ab', 'A#/Bb', 'C', 'C#/Db', 'D#/Eb'], 'Locrian': ['F', 'F#/Gb', 'G#/Ab', 'A#/Bb', 'B', 'C#/Db', 'D#/Eb']}, 'F#/Gb': {'Ionian': ['F#/Gb', 'G#/Ab', 'A#/Bb', 'B', 'C#/Db', 'D#/Eb', 'F'], 'Dorian': ['F#/Gb', 'G#/Ab', 'A', 'B', 'C#/Db', 'D#/Eb', 'E'], 'Phrygian': ['F#/Gb', 'G', 'A', 'B', 'C#/Db', 'D', 'E'], 'Lydian': ['F#/Gb', 'G#/Ab', 'A#/Bb', 'C', 'C#/Db', 'D#/Eb', 'F'], 'Mixolydian': ['F#/Gb', 'G#/Ab', 'A#/Bb', 'B', 'C#/Db', 'D#/Eb', 'E'], 'Aeolian': ['F#/Gb', 'G#/Ab', 'A', 'B', 'C#/Db', 'D', 'E'], 'Locrian': ['F#/Gb', 'G', 'A', 'B', 'C', 'D', 'E']}, 'G': {'Ionian': ['G', 'A', 'B', 'C', 'D', 'E', 'F#/Gb'], 'Dorian': ['G', 'A', 'A#/Bb', 'C', 'D', 'E', 'F'], 'Phrygian': ['G', 'G#/Ab', 'A#/Bb', 'C', 'D', 'D#/Eb', 'F'], 'Lydian': ['G', 'A', 'B', 'C#/Db', 'D', 'E', 'F#/Gb'], 'Mixolydian': ['G', 'A', 'B', 'C', 'D', 'E', 'F'], 'Aeolian': ['G', 'A', 'A#/Bb', 'C', 'D', 'D#/Eb', 'F'], 'Locrian': ['G', 'G#/Ab', 'A#/Bb', 'C', 'C#/Db', 'D#/Eb', 'F']}, 'G#/Ab': {'Ionian': ['G#/Ab', 'A#/Bb', 'C', 'C#/Db', 'D#/Eb', 'F', 'G'], 'Dorian': ['G#/Ab', 'A#/Bb', 'B', 'C#/Db', 'D#/Eb', 'F', 'F#/Gb'], 'Phrygian': ['G#/Ab', 'A', 'B', 'C#/Db', 'D#/Eb', 'E', 'F#/Gb'], 'Lydian': ['G#/Ab', 'A#/Bb', 'C', 'D', 'D#/Eb', 'F', 'G'], 'Mixolydian': ['G#/Ab', 'A#/Bb', 'C', 'C#/Db', 'D#/Eb', 'F', 'F#/Gb'], 'Aeolian': ['G#/Ab', 'A#/Bb', 'B', 'C#/Db', 'D#/Eb', 'E', 'F#/Gb'], 'Locrian': ['G#/Ab', 'A', 'B', 'C#/Db', 'D', 'E', 'F#/Gb']}}




