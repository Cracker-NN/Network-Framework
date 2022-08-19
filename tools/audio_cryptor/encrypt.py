from pydub import AudioSegment
import os
import platform
import base64
import wave
from os import path

class Encrypter():
    def __init__(self, msg:str, Audiofilename:str) -> None:
        self.message = str(msg)
        self.Audio_File = str(Audiofilename)

    def slash(self):
        if platform.system().lower() == "windows":
            slash = "\\"
        else:
            slash = "/"
        return slash

    def WAV(self):
        inputfile = self.Audio_File
        output = str(os.getcwd()) + self.slash() + "tools" + self.slash() + "audio_cryptor" + self.slash() +"output.wav"
        if inputfile.endswith(".mp3"):
            sound = AudioSegment.from_mp3(inputfile)
            sound.export(output, format="wav")
        elif inputfile.endswith(".ogg"):
            sound = AudioSegment.from_ogg(inputfile)
            sound.export(output, format="wav")
        elif inputfile.endswith(".wav"):
            sound = AudioSegment.from_wav(inputfile)
            sound.export(output, format="wav")
        else:
            print("File Type Not Supported")

        return sound

    def encryptHash(self):
        encrypt_msg = base64.standard_b64encode(bytes(self.message, "utf-8"))
        return str("".join(str(encrypt_msg).split("'")[1]))

    def encryptAudioFile(self):
        output = str(os.getcwd()) + self.slash() + "tools" + self.slash() + "audio_cryptor" + self.slash() +"output.wav"
        WaveOpen = wave.open(output, mode="rb")
        FrameConvert = bytearray(list(WaveOpen.readframes(WaveOpen.getnframes())))
        stringValue = self.encryptHash() + int((len(FrameConvert)-len(self.encryptHash())*8*8)/8) * '*'
        bits = list(map(int, ''.join([bin(ord(i)).lstrip('0b').rjust(8,'0') for i in stringValue])))
        for i ,bit in enumerate(bits):
            FrameConvert[i] = (FrameConvert[i] & 254) | bit
        opening = bytes(FrameConvert)
        with wave.open("output" + "_encrypt" + ".wav", mode="wb") as f:
            f.setparams(WaveOpen.getparams())
            f.writeframes(opening)
        WaveOpen.close()

    def console(self):
        if self.Audio_File.endswith(".mp3"):
            audioFormat = ".mp3"
        elif self.Audio_File.endswith(".ogg"):
            audioFormat = ".ogg"
        elif self.Audio_File.endswith(".wav"):
            audioFormat = ".wav"
        else:
            audioFormat = "Audio Format is Unknown"

        return audioFormat

    def encrypt(self):
        print("")
        print(f"\033[1;34m[+]\033[0;37m Converting {self.console()} => .wav")
        self.WAV()
        print(f"\033[1;34m[+]\033[0;37m Converting {self.message} => Hashed")
        self.encryptHash()
        print(f"\033[1;34m[+]\033[0;37m Mixing Message with Audio => output_encrypt.wav")
        self.encryptAudioFile()
        print(f"\033[1;34m[+]\033[0;37m Removing Temporary Files => output.wav")
        path = str(os.getcwd()) + self.slash() + "tools" + self.slash() + "audio_cryptor" + self.slash() + "output.wav"
        os.remove(path=path)
        print("")


