import argparse
from pathlib import Path
from PIL import Image
from pillow_heif import register_heif_opener

class Converter:
    def __init__(self, source: Path, destination: Path):
        self.source = source
        self.destination = destination
        register_heif_opener()

    def convert(self):
        for file in self.source.iterdir():
            if file.suffix.lower() == ".heic":
                save_path = self.destination / file.name
                png_file = save_path.with_suffix(".png")
                if png_file.is_file():
                    file.unlink()
                    print(f"Removed {file}")
                else:
                    image = Image.open(file)
                    image.save(png_file)
                    print(f"Converted {file} to {png_file}")
                

def main():
    parser = argparse.ArgumentParser(description="HEIC to PNG converter")
    parser.add_argument("-p", "--path", type=str, required=True, help="Path to the directory containing HEIC files")
    parser.add_argument("-d", "--destination", type=str, required=True, help="Path to the directory to save PNG files")
    
    args = parser.parse_args()
    converter = Converter(Path(args.path), Path(args.destination))
    converter.convert()

if __name__ == "__main__":
    main()
