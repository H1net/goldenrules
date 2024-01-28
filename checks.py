import pandas as pd
import sys

from PyQt6.QtWidgets import (
  QApplication,
  QVBoxLayout,
  QHBoxLayout,
  QWidget
)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from markdown import markdown as markdown

def get_checks():
    # load the data
    checks = pd.read_csv('data/checks.csv')
    return checks


def get_view():
    # Create a QWebEngineView object
    view = QWebEngineView()
    # Convert markdown to HTML
    md_text = """
    # GR Reverts

    This is some **markdown** text.
    """

    # md_text+= checks.head().to_string()

    html = markdown(md_text)

    # Set the HTML in the browser widget
    view.setHtml(html)
    return view

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GR Reverts")
        # self.resize(800, 600)

        # Create a top-level layout
        layout = QVBoxLayout()

        # Create filter bar
        layoutHeader = QHBoxLayout()

        # Create filter bar
        layoutFooter = QHBoxLayout()

        # Create a QWebEngineView object
        view = get_view()

        # Add the QWebEngineView object to the layout
        layout.addLayout(layoutHeader)
        layout.addWidget(view)
        layout.addLayout(layoutFooter)

        # Set the layout of the application
        self.setLayout(layout)

def main():
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()