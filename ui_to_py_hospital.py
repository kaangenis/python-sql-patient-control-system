from PyQt5 import uic

with open('duzenlePage.py', 'w', encoding="utf-8") as fout:
    uic.compileUi('duzenlePage.ui', fout)