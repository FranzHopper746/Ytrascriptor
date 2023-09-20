import argparse, os
import whisper
from pytube import YouTube

downloadsPath = "downloads"
transcriptionPath = "trascrizioni"


def run_transcriptor():
    if not os.path.exists(transcriptionPath):
        os.makedirs(transcriptionPath)

    parser = argparse.ArgumentParser(
        prog='Ytrascriptor',
        description='Sta roba trascrive i video di yt',
        epilog='babbi')

    parser.add_argument("videourl", nargs='+', help="l'url del video di youtube")
    parser.add_argument("-m", "--model", dest="model", default="base",
                        help="modello di whisper['tiny', 'base', 'small', 'mediun', 'large'] default: 'base'")
    args = parser.parse_args()
    mode = args.model

    for url in args.videourl:
        yt = YouTube(url)
        source = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        filename = source.default_filename
        print("inizio download audio di " + filename + " url: " + url)
        source.download(downloadsPath)
        print("inizio trascrizione di: " + filename)
        model = whisper.load_model(mode).cuda()
        result = model.transcribe(verbose=True, audio=downloadsPath + "/" + filename)
        file = open(transcriptionPath + "/" + filename + ".txt", "w+")
        file.write(result["text"])


if __name__ == "__main__":
    main()
