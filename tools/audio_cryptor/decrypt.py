import base64
import wave


class Decryptor():
    def __init__(self, filename:str) -> None:
        self.file = str(filename)

    def decryptAudio(self):
        string = []
        WaveAudio = wave.open(self.file, mode="rb")
        AudioFrame = bytearray(list(WaveAudio.readframes(WaveAudio.getnframes())))
        ExtractingData = [AudioFrame[i] & 1 for i in range(len(AudioFrame))]
        decode = "".join(chr(int("".join(map(str, ExtractingData[i:i+8])), 2)) for i in range(0, len(ExtractingData), 8))
        removing_Punct = decode.split("***")[0]
        decoded_message = base64.standard_b64decode(bytes(removing_Punct, encoding="utf-8"))
        string.append("".join(str(decoded_message).split("'")[1]))
        WaveAudio.close()
        return "".join(string)

if __name__ == '__main__':
    d = Decryptor("E:\\update\\Network-Framework\\a.wav")
    print(d.decryptAudio())
