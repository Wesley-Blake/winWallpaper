import ctypes
import winreg
import os
from pathlib import Path


def set_wallpaper(image_path: str) -> None:
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDWININICHANGE = 0x02

    with winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Control Panel\Desktop",
        0,
        winreg.KEY_SET_VALUE
    ) as key:
        winreg.SetValueEx(
            key,
            "WallpaperStyle",
            0,
            winreg.REG_SZ,
            "1"  # 0: Center, 1: Fit, 2: Stretch, 3: Stretch, 4: Fit, 5: Fit
        )
        winreg.SetValueEx(
            key,
            "TileWallpaper",
            0,
            winreg.REG_SZ,
            "0"  # 0: No tiling, 1: Tile
        )

    result = ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER,
        0,
        image_path,
        SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE
    )

    if not result:
        raise Exception("Failed to set wallpaper")


def rand_wallpaper() -> str:
    PICTURES_DIR = Path.home() / 'Pictures'
    wallpapers = (
        list(PICTURES_DIR.glob('*.jpg'))
        + list(PICTURES_DIR.glob('*.jpeg'))
        + list(PICTURES_DIR.glob('*.png'))
    )
    import random
    return str(random.choice(wallpapers))


def get_wallpaper() -> str:
    PICTURES_DIR = Path.home() / 'Pictures'
    wallpapers = (
        list(PICTURES_DIR.glob('*.jpg'))
        + list(PICTURES_DIR.glob('*.jpeg'))
        + list(PICTURES_DIR.glob('*.png'))
    )
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
    set_wallpaper(rand_wallpaper())
