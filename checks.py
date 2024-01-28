import pandas as pd
import sys

from PyQt6.QtWidgets import (
  QApplication,
  QHBoxLayout,
  QWidget
)
from PyQt6.QtWebEngineWidgets import QWebEngineView
from markdown import markdown as markdown

def get_checks():
    # load the data
    checks = pd.read_csv('data/checks.csv')
    return checks

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GR Reverts")
        # self.resize(800, 600)

        # Create a top-level layout
        layout = QHBoxLayout()

        # Create a QWebEngineView object
        view = QWebEngineView()

        # Add the QWebEngineView object to the layout
        layout.addWidget(view)

        # Set the layout of the application
        self.setLayout(layout)

        # Convert markdown to HTML
        md_text = """
        # GR Reverts

        This is some **markdown** text.
        """

        # md_text+= checks.head().to_string()

        html = markdown(md_text)

        # Set the HTML in the browser widget
        view.setHtml(html)

def main():
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()