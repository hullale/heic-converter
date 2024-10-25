import argparse
from pathlib import Path
from PIL import Image
from pillow_heif import register_heif_opener

class Converter:
    def __init__(self, source: Path, delete: bool):
        self.source = source
        self.delete = delete
        register_heif_opener()

    def check_if_files_exist(self):
        num_files = len(list(self.source.rglob('*.heic')))
        if num_files > 10:
            print(f"Warning: {num_files} files are about to be converted.")
            input("\tPress Enter to continue...")

    def convert(self):
        self.check_if_files_exist()

        for file in self.source.rglob("*"):
            if file.suffix.lower() == ".heic":
                png_file = file.with_suffix(".png")
                if png_file.is_file():
                    print(f"PNG already exists at: {png_file}")
                else:
                    print(f"Converting {file} to {png_file}")
                    image = Image.open(file)
                    image.save(png_file)
                
                if self.delete and png_file.is_file():
                    print(f"Removing {file}")
                    file.unlink()
                    
                

def main():
    parser = argparse.ArgumentParser(description="HEIC to PNG converter")
    parser.add_argument("-p", "--path", type=str, required=True, help="Path to the directory containing HEIC files")
    parser.add_argument("-d", "--delete", action='store_true', help="Delete HEIC files after converting? (Recommend running after verifying conversion worked)")
    
    args = parser.parse_args()
    converter = Converter(Path(args.path), args.delete)
    converter.convert()

if __name__ == "__main__":
    main()
