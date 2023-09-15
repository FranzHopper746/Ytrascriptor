## Prereusiti
Il pitone (3.10, ma credo >= 3 sia abbastanza) e pip e python-venv non so come si installi su windows

## Setup

Crea l'environment di venv

```bash
python3 -m venv ytrascriptor
```

Attiva l'environment (da fare ogni volta)

```bash
source ytrascriptor/bin/activate
```

Installa sta roba

```bash
pip install requirements
```

Credo che si debba installare ffmpeg, su Windows dovrebbe bastare sta roba:

```bash
winget.exe install ffmpeg
```

## Esempio di sta tragedia

```bash
python3 Ytrascriptor.py "url del video"
```
