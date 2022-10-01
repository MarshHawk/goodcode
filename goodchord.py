import pretty_midi
import pretty_midi as pm
# Create a PrettyMIDI object
good_chord = pm.PrettyMIDI()

# Create an Instrument instance for a cello instrument
#print(pm.constants.INSTRUMENT_MAP)

#instruments = ['Electric Guitar (muted)', 'Overdriven Guitar', 'Distortion Guitar', 'Guitar Harmonics', 'Acoustic Bass', 'Electric Bass (finger)', 'Electric Bass (pick)', 'Fretless Bass', 'Slap Bass 1', 'Slap Bass 2', 'Synth Bass 1', 'Synth Bass 2', 'Violin', 'Viola', 'Cello', 'Contrabass', 'Tremolo Strings', 'Pizzicato Strings', 'Orchestral Harp', 'Timpani', 'String Ensemble 1', 'String Ensemble 2',
#               'Synth Strings 1', 'Synth Strings 2', 'Choir Aahs', 'Voice Oohs', 'Synth Choir', 'Orchestra Hit', 'Trumpet', 'Trombone', 'Tuba', 'Muted Trumpet', 'French Horn', 'Brass Section', 'Synth Brass 1', 'Synth Brass 2', 'Soprano Sax', 'Alto Sax', 'Tenor Sax', 'Baritone Sax', 'Oboe', 'English Horn', 'Bassoon', 'Clarinet', 'Piccolo', 'Flute', 'Recorder', 'Pan Flute', 'Blown bottle', 'Shakuhachi', 'Whistle', 'Ocarina']
#q1 = ['Electric Guitar (muted)', 'Fretless Bass', 'Violin', 'Electric Piano 1']
#quartet = [pm.Instrument(program=pm.instrument_name_to_program('Cello')) for instrument_name in q1]

lead_program = pm.instrument_name_to_program('Electric Guitar (muted)')
lead = pm.Instrument(name='lead', program=lead_program)

strings_program = pm.instrument_name_to_program('Synth Strings 1')
strings = pm.Instrument(name='strings', program=strings_program)

motives = [
    ['F#3', 'C#4', 'B3', 'F#4', 'E4', 'B4'],
    ['A4', 'E4', 'D4', 'A4', 'G4', 'D5'],
    ['C5', 'G5', 'F5', 'C5', 'Bb4', 'F5']
]

chords = [
    ['G2', 'B3', 'C#4'],
    ['Bb2', 'D3', 'E4'],
    ['Db3', 'F3', 'G3']
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



notes_to_motif()

good_chord.instruments.append(lead)
good_chord.instruments.append(strings)
good_chord.write('sixer.mid')
