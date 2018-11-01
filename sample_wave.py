#!/usr/bin/env python3
import houndify
import sys
import time
import wave
import keys

def execute():
    CLIENT_ID = keys.houndify_client_id
    CLIENT_KEY = keys.houndify_client_key
    QUERY = 'output.wav'
    BUFFER_SIZE = 256

    AUDIO_FILE='output.wav'

    stringz = ''

    audio = wave.open(AUDIO_FILE)
    if audio.getsampwidth() != 2:
      print("%s: wrong sample width (must be 16-bit)" % fname)
      sys.exit()
    if audio.getframerate() != 8000 and audio.getframerate() != 16000:
      print("%s: unsupported sampling frequency (must be either 8 or 16 khz)" % fname)
      sys.exit()
    if audio.getnchannels() != 1:
      print("%s: must be single channel (mono)" % fname)
      sys.exit()


    audio_size = audio.getnframes() * audio.getsampwidth()
    audio_duration = audio.getnframes() / audio.getframerate()
    chunk_duration = BUFFER_SIZE * audio_duration / audio_size


    #
    # Simplest HoundListener; just print out what we receive.
    # You can use these callbacks to interact with your UI.
    #
    class MyListener(houndify.HoundListener):
      def onPartialTranscript(self, transcript):
        # print("Partial transcript: " + transcript)
        stringz = transcript
      def onFinalResponse(self, response):
        # print("Final response: " + str(response))
        stringz = response
      def onError(self, err):
        print("Error: " + str(err))


    client = houndify.StreamingHoundClient(CLIENT_ID, CLIENT_KEY, "test_user")
    client.setLocation(37.388309, -121.973968)
    client.setSampleRate(audio.getframerate())


    client.start(MyListener())


    while True:
      chunk_start = time.time()

      samples = audio.readframes(BUFFER_SIZE)
      if len(samples) == 0: break
      if client.fill(samples): break

      # # Uncomment the line below to simulate real-time request
      # time.sleep(chunk_duration - time.time() + chunk_start)

    result = client.finish() # returns either final response or error

    stringz = result.get("Disambiguation").get("ChoiceData")[0].get("Transcription")
    return stringz
