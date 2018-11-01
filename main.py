import record
import musixmatch
import sample_wave

print("Say The artist name: ")
record.execute()
artist = sample_wave.execute()
print("Say the track name: ")
record.execute()
track = sample_wave.execute()
musixmatch.execute(artist, track)
