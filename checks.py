import pandas as pd

# load the data
checks = pd.read_csv('data/checks.csv')

from PyQt6.QtWidgets import QApplication, QTextBrowser
from markdown import markdown as md
import sys

def main():
    app = QApplication(sys.argv)

    browser = QTextBrowser()
    browser.setOpenExternalLinks(True)

    # Set the window title
    browser.setWindowTitle("GR Reverts")

    # Convert markdown to HTML
    md_text = """
    # GR Reverts

    This is some **markdown** text.


    """
    html = md(md_text)

    # Set the HTML in the browser widget
    browser.setHtml(html)

    browser.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()