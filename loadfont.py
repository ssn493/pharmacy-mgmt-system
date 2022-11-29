import sys
import os
import shutil

BASEPATH = os.getcwd()+os.path.sep
LIN_PATH =  os.path.expanduser('~')+os.path.sep+r'.fonts'

loaded_fonts_lin = []

def loadfont_win(fontpath, private=True, enumerable=False):
    """
    Makes fonts located in file `fontpath` available to the font system.
    `private`     if True, other processes cannot see this font, and this
                  font will be unloaded when the process dies
    `enumerable`  if True, this font will appear when enumerating fonts
    """
    try:
        from ctypes import windll, byref, create_unicode_buffer, create_string_buffer
    except ImportError:
        return False

    FR_PRIVATE = 0x10
    FR_NOT_ENUM = 0x20
    # This function was taken from
    # https://github.com/ifwe/digsby/blob/f5fe00244744aa131e07f09348d10563f3d8fa99/digsby/src/gui/native/win/winfonts.py#L15
    # This function is written for Python 2.x. For 3.x, you
    # have to convert the isinstance checks to bytes and str
    if isinstance(fontpath, bytes):
        pathbuf = create_string_buffer(fontpath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExA
    elif isinstance(fontpath, str):
        pathbuf = create_unicode_buffer(fontpath)
        AddFontResourceEx = windll.gdi32.AddFontResourceExW
    else:
        raise TypeError("fontpath must be of type str or unicode")

    flags = (FR_PRIVATE if private else 0) | (FR_NOT_ENUM if not enumerable else 0)
    numFontsAdded = AddFontResourceEx(byref(pathbuf), flags, 0)
    return bool(numFontsAdded)

def loadfont_lin(fontpath):
    path, filename= os.path.split(fontpath)
    shutil.copy2(fontpath, LIN_PATH)
    global loaded_fonts_lin
    loaded_fonts_lin.append(filename)

def removefont_lin(fontpath):
    global loaded_fonts_lin
    dirpath, filename = os.path.split(fontpath)
    if filename in loaded_fonts_lin and os.path.isfile(LIN_PATH+os.path.sep+filename):
        os.remove(LIN_PATH+os.path.sep+filename)
    else:
        raise Exception('Font not loaded')