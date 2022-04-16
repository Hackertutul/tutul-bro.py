import os, platform
os.system("cd $HOME/")
#os.system("termux-setup-storage")
os.system("xdg-open https://www.facebook.com/groups/660205018582939")

try:
    import requests
except(ImportError):
    os.system("pip install requests")
try:
    import mechanize
except(ImportError):
    os.system("pip install mechanize")
try:
    import bs4
except(ImportError):
    os.system("pip install bs4")

tutul=platform.architecture()[0]
try:
    if tutul=="32bit":
        __import__("tutul32").main_menu()
    elif tutul=="64bit":
        __import__("tutul").main_menu()
    else:
        print(" We have issue to launch script")
        exit()
except(AttributeError,OSError,KeyError,IOError):
    if tutul == "32bit":
        import pro32
        tutul32.main_menu()
    elif tutul == "64bit":
        import tutul
        tutul.main_menu()
    else:
        print(" We have issue to launch script")
        exit()
