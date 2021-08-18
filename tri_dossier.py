from pathlib import Path

data_dir = Path.cwd() / "data"

extensions = {
    ".mp3": "Musique",
    ".wav": "Musique",
    ".flac": "Musique",
    ".avi": "Videos",
    ".mp4": "Videos",
    ".gif": "Videos",
    ".bmp": "Images",
    ".png": "Images",
    ".jpg": "Images",
    ".txt": "Documents",
    ".pptx": "Documents",
    ".csv": "Documents",
    ".xls": "Documents",
    ".odp": "Documents",
    ".pages": "Documents",
}

files = [f for f in data_dir.iterdir() if f.is_file()]

for f in files:
    if f.suffix in extensions.keys():
        output_dir = data_dir / extensions[f.suffix]
    else:
        output_dir = data_dir / "Autres"
    
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)