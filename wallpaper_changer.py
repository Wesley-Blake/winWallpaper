import ctypes
import os
from pathlib import Path

def set_wallpaper(image_path: str) -> None:
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDWININICHANGE = 0x02

    result = ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE
    )

    if not result:
        raise Exception("Failed to set wallpaper")

def rand_wallpaper() -> str:
    PICTURES_DIR = Path.home() / 'Pictures'
    wallpapers = list(PICTURES_DIR.glob('*.jpg')) + list(PICTURES_DIR.glob('*.jpeg')) + list(PICTURES_DIR.glob('*.png'))
    import random
    return str(random.choice(wallpapers))

def get_wallpaper() -> str:
    PICTURES_DIR = Path.home() / 'Pictures'
    wallpapers = list(PICTURES_DIR.glob('*.jpg')) + list(PICTURES_DIR.glob('*.jpeg')) + list(PICTURES_DIR.glob('*.png'))
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        for i, v in enumerate(wallpapers):
            print(f"{i+1}: {v.name}")
        print("e: Exit")
        print("r: Random Wallpaper")
        input_str = input("Select the wallpaper you want to set: ")
        if input_str.isdigit():
            index = abs(int(input_str) - 1)
            break
        elif input_str.lower() == 'r':
            import random
            return str(random.choice(wallpapers))
        elif input_str.lower() == 'e':
            print("Exiting...")
            exit()
    return str(wallpapers[index % len(wallpapers)])

if __name__ == "__main__":
    #path_o_interest = get_wallpaper()
    #set_wallpaper(path_o_interest)
    set_wallpaper(rand_wallpaper())
