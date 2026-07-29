import ctypes
import random
import winreg
from pathlib import Path

SPI_SETDESKWALLPAPER = 20
SPIF_UPDATEINIFILE = 0x01
SPIF_SENDWININICHANGE = 0x02
PICTURES_DIR = Path.home() / "Pictures"


def set_wallpaper(image_path: str) -> None:
    with winreg.OpenKey(
        winreg.HKEY_CURRENT_USER, r"Control Panel\Desktop", 0, winreg.KEY_SET_VALUE
    ) as key:
        winreg.SetValueEx(
            key,
            "WallpaperStyle",
            0,
            winreg.REG_SZ,
            "1",  # 0: Center, 1: Fit, 2: Stretch, 3: Stretch, 4: Fit, 5: Fit
        )
        winreg.SetValueEx(
            key,
            "TileWallpaper",
            0,
            winreg.REG_SZ,
            "0",  # 0: No tiling, 1: Tile
        )

    result = ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE
    )

    if not result:
        raise RuntimeError("Failed to set wallpaper")


def rand_wallpaper() -> str:
    wallpapers = (
        list(PICTURES_DIR.glob("*.jpg"))
        + list(PICTURES_DIR.glob("*.jpeg"))
        + list(PICTURES_DIR.glob("*.png"))
    )
    return str(random.choice(wallpapers))


if __name__ == "__main__":
    set_wallpaper(rand_wallpaper())
