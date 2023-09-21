## Prereusiti
Il pitone (3.10, ma credo >= 3 sia abbastanza) e pip e python-venv non so come si installi su windows

## Setup

Crea l'environment di venv

```bash
python -m venv ytrascriptor
```

Attiva l'environment (da fare ogni volta)

Linux:
```bash
source ytrascriptor/bin/activate
```

Windows:
```bash
.\ytrascriptor\Scripts\activate.bat
```
Installa sta roba

```bash
pip install -r requirements.txt
```

Credo che si debba installare ffmpeg, su Windows dovrebbe bastare sta roba:

```bash
winget.exe install ffmpeg
```

## Esempio di sta tragedia

```bash
python Ytrascriptor.py "url del video"
```

## CUDA

Installa i driver CUDA, Cudnn, poi reinstalla pytorch

```bash
pip uninstall torch torchvision torchaudio

pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```