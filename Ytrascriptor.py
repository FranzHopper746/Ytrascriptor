import argparse, os
import whisper
from pytube import YouTube

downloadsPath = "downloads"
transcriptionPath = "trascrizioni"

def time_to_minutes(time):
    h = int(time / 60 / 60)
    time = time - (h * 60 * 60)
    m = int(time / 60)
    time = time - (m * 60)
    s = int(time)
    return "{:02d}".format(h) +":"+"{:02d}".format(m)+":"+"{:02d}".format(s)

def main():
    if not os.path.exists(transcriptionPath):
        os.makedirs(transcriptionPath)

    parser = argparse.ArgumentParser(
        prog='Ytrascriptor',
        description='Sta roba trascrive i video di yt',
        epilog='babbi')

    parser.add_argument("videourl", nargs='+', help="l'url del video di youtube")
    parser.add_argument("-m", "--model", dest="model", default="base", help="modello di whisper['tiny', 'base', 'small', 'mediun', 'large'] default: 'base'")
    parser.add_argument("-t", "--timestamp", action="store_true")
    args = parser.parse_args()
    mode = args.model

    for url in args.videourl:
        yt = YouTube(url)
        source = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        filename = source.default_filename
        print("inizio download audio di "+filename+" url: "+url)
        source.download(downloadsPath)
        print("inizio trascrizione di: "+filename) 
        model = whisper.load_model(mode).cuda()
        result = model.transcribe(verbose=True, audio=downloadsPath + "/"+filename)
        file = open(transcriptionPath+"/"+filename+".txt", "w+")
        if(args.timestamp):
            for r in result["segments"]:
                file.write("[" + time_to_minutes(r["start"]) + " - " + time_to_minutes(r["end"]) + "]:" + r["text"]+"\n")
        else:
            file.write(result["text"])

if __name__ == "__main__":
   main()