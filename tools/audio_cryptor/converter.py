import pydub


def converter(AudioFileName:str, output:str):

    """
    wave to mp3
    """

    if AudioFileName.endswith(".mp3"):
        audio = pydub.AudioSegment.from_mp3(AudioFileName)
        audio.export(output, format="mp3")
    elif AudioFileName.endswith(".ogg"):
        audio = pydub.AudioSegment.from_ogg(AudioFileName)
        audio.export(output, format="mp3")
    elif AudioFileName.endswith(".wav"):
        audio = pydub.AudioSegment.from_wav(AudioFileName)
        audio.export(output, format="mp3")
    else:
        audio = "File Type Not Found"

    return audio

def converterWav(AudioFileName:str, output:str):

    """
    mp3 to wav
    """

    if AudioFileName.endswith(".mp3"):
        audio = pydub.AudioSegment.from_mp3(AudioFileName)
        audio.export(output, format="wav")
    elif AudioFileName.endswith(".ogg"):
        audio = pydub.AudioSegment.from_ogg(AudioFileName)
        audio.export(output, format="wav")
    elif AudioFileName.endswith(".wav"):
        audio = pydub.AudioSegment.from_wav(AudioFileName)
        audio.export(output, format="wav")
    else:
        audio = "File Type Not Found"

    return audio


