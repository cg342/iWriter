'''
https://hashedin.com/blog/how-to-convert-different-language-audio-to-text-using-python/

Step 1: Import speech_recognition as speechRecognition. #import library

Step 2: speechRecognition.Recognizer() # Initializing recognizer class in order to recognize the speech. We are using google speech recognition.

Step 3: recogniser.recognize_google(audio_text) # Converting audio transcripts into text.

Step 4: Converting specific language audio to text.

'''


import speech_recognition as sr

r = sr.Recognizer()

def getLanguage(argument):
    switcher = {
        1: "en-IN",
        2: "hi-IN",
        3: "kn-IN"
    }
    return switcher.get(argument, 0)


def getSelection():
    
    try: 
        userInput = int(input())
        if (userInput<1 or userInput>3):
            print("Not an integer! Try again.")
            
    except ValueError:
        print("not an integer! Try again.")
        
    else:
        return userInput
           

# Reading Audio File as source
# output stored in audio_text variable
def startConvertion(path, lang = 'en-IN'):
    with sr.AudioFile(path) as source:
        print('Fetching File')
        audio_text = r.listen(source)

        try:
            print('Converting audio transcripts into text ...')
            text = r.recognize_google(audio_text, language = lang)
            print(text)
            # print("hello how are you")
        except:
            print('Sorry.. run again...')

# if __name__ == '__main__':
#     print('Please Select Language: ')
#     print('1. English')
#     print('2. Chinese')

#     languageSelection = getLanguage(getSelection())
    # startConvertion('sample.m4a', languageSelection)



print(startConvertion('sample2.wav','en-IN'))
