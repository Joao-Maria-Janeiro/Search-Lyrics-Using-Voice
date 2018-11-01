## Search Lyrics Using Voice

Python program that allows users to search for a song only by saying the artist name and the track name

## Built With

* [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) - The Sound Recorder
* [Houndify](https://www.houndify.com/dashboard) - Speech Recognition
* [Musixmatch](https://developer.musixmatch.com) - Gives the lyrics

## How does it work?
* We use PyAudio to record audio and generate a wave audio file
* Afterwards we use the generated audio file and the houndify API to recognize what the user said and we extract the text from the json response from the API
* Then we do a request to the musixmatch API to get the lyrics for the track

# How to run
### Installation of requirments

##### Try running:

```
$ pip install -r requirements.txt
```

##### If that does't work:

##### Windows
###### First you need to install pyaudio:
* Install the c++ Build Tools if you don't have them already:
[Build Tools](https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=15)
* After that simply run
```
$ python -m pip install pyaudio
```

###### Then simply install requests with pip:
```
$ pip install requests
```

##### Linux(Ubuntu)
###### First you need to install pyaudio:
* Clone the repo:
```
$ git clone https://people.csail.mit.edu/hubert/git/pyaudio.git
```
* Then install pythonaudio:
```
$ sudo apt-get install python-pyaudio python3-pyaudio
```

###### Then simply install requests with pip:
```
$ pip install requests
```

##### MacOS
###### First you need to install pyaudio:
```
$ brew install portaudio 
$ pip install pyaudio
```
###### Then simply install requests with pip:
```
$ pip install requests
```

### To execute it simply do:
```
$ python main.py
```
