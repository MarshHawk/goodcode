import pretty_midi
import pretty_midi as pm
import copy

# Create a PrettyMIDI object
good_chord = pm.PrettyMIDI()

# Create an Instrument instance for a cello instrument
#print(pm.constants.INSTRUMENT_MAP)

lead_program = pm.instrument_name_to_program('Electric Guitar (muted)')
lead = pm.Instrument(name='lead', program=lead_program)

strings_program = pm.instrument_name_to_program('Synth Strings 1')
strings = pm.Instrument(name='strings', program=strings_program)

bass_program = pm.instrument_name_to_program('Fretless Bass')
bass = pm.Instrument(name='bass', program=bass_program)

motives = [
    ['F#4', 'C#4', 'B3', 'F#4', 'E4', 'B4'],
    ['A4', 'E4', 'D4', 'A4', 'G4', 'D5'],
    ['C5', 'G5', 'F5', 'C5', 'Bb4', 'F5'],
    ['D#5', 'A#5', 'G#5', 'D#5', 'C#5', 'G#4']
]

chords = [
    ['G3', 'B4', 'C#5', 'F#5'],
    ['Bb3', 'D5', 'E5', 'A5'],
    ['Db4', 'F4', 'G4', 'C5'],
    ['E3', 'G#4', 'A#4', 'D#5'],
]

bass_line = [
    ['E5', 'D5', 'G4'], ['G4', 'F4', 'Bb3'], ['Bb3', 'Ab3', 'Db3'], ['C#3', 'B3', 'E4'],
]

def notes_to_motif(index=0):
    for items in motives:
        for note_name in items:
            note_number = pm.note_name_to_number(note_name)
            note = pretty_midi.Note(
                velocity=100, pitch=note_number, start=index, end=index+.5)
            index += .5
            lead.notes.append(note)

    s_start = 0
    for items in chords:
        for note_name in items:
            note_number = pm.note_name_to_number(note_name)
            note = pretty_midi.Note(
                velocity=100, pitch=note_number, start=s_start, end=s_start+2)
            strings.notes.append(note)
        s_start+=3

    b_start = 0
    for items in bass_line:
        bass.notes.append(pretty_midi.Note(
            velocity=100, pitch=pm.note_name_to_number(items[0]), start=b_start, end=b_start+.5))
        bass.notes.append(pretty_midi.Note(
            velocity=100, pitch=pm.note_name_to_number(items[1]), start=b_start+1, end=b_start+1.5))
        bass.notes.append(pretty_midi.Note(
            velocity=100, pitch=pm.note_name_to_number(items[2]), start=b_start+2, end=b_start+3))
        b_start+=3
            

notes_to_motif()

def transpose_notes(lead_notes, strings_notes, bass_notes, index=0):
    if index < 12:
        next_lead = copy.deepcopy(lead_notes)
        next_strings = copy.deepcopy(strings_notes)
        next_bass = copy.deepcopy(bass_notes)
    
        for note in next_lead:
            note.pitch += 1
            note.start += 12
            note.end += 12
            lead.notes.append(note)

        for note in next_strings:
            note.pitch += 1
            note.start += 12
            note.end += 12
            strings.notes.append(note)

        for note in next_bass:
            note.pitch += 1
            note.start += 12
            note.end += 12
            bass.notes.append(note)
        
        transpose_notes(next_lead, next_strings, next_bass, index=index+1)

transpose_notes(lead.notes, strings.notes, bass.notes)

good_chord.instruments.append(lead)
good_chord.instruments.append(strings)
good_chord.instruments.append(bass)

good_chord.write('goodcode.mid')
