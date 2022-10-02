import sys
import speech_recognition as sr
import numpy

# Objective: determine an index for discriminatory behavior in healthcare providers

# GLOBAL VARRIABLES

    # poss: possessive word
    # non-poss: non-possessive word

poss_word_dict = {
    "I": "poss",
    "you": "non-poss",
    "they": "non-poss",
    "we": "non-poss"
}

    # some words have positive and negative connotations
    # 
pos_neg_dict = {

    "can" : 1,
    "cannot": -1,
    "do" : 1
}

def parse_lang(text):

    text_arr = text.split(' ')
    return text_arr

def calculate_bias(text_arr):

    bias_index = 0

    # compute the bias index based on text_arr

    # de-facto code, doesn't really work the way it's supposed to
    for word in text_arr:
        if word in pos_neg_dict:
            bias_index = bias_index + text_arr[word].get()

    return bias_index

    '''
    working code in numpy

    input_vector = np.array([-1, 0, 1])
    print(input_vector)
    
    
    '''


def App():

    # call the speech-to-text API
    r = sr.Recognizer()

    with sr.Microphone() as source:

    # read the audio data from the default microphone
        audio_data = r.record(source, duration=5)
        print("Recognizing...")

    # convert speech to text
        text = r.recognize_google(audio_data)
        print(text)

    str_arr = parse_lang(text)
    print(calculate_bias(str_arr))


    '''
    experimental stuff with spanish
    text = r.recognize_google(audio_data, language="es-ES")
    
    '''

    # split the string into an array

    # call the method 



def main():
    App()

main()
