import pandas as pd

# load the data
checks = pd.read_csv('data/checks.csv')

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWebEngineWidgets import QWebEngineView
from markdown import markdown as md
import sys

def main():
    app = QApplication(sys.argv)

    view = QWebEngineView()

    # Set the window title
    view.setWindowTitle("GR Reverts")

    # Convert markdown to HTML
    md_text = """
    # GR Reverts

    This is some **markdown** text.
    """

    md_text+= checks.head().to_string()

    html = md(md_text)

    # Set the HTML in the browser widget
    view.setHtml(html)

    view.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()