import pandas as pd
import sys

from PyQt6.QtWidgets import (
  QApplication,
  QVBoxLayout,
  QHBoxLayout,
  QWidget,
  QTableView
)
from PyQt6.QtCore import QAbstractTableModel, Qt  # Changed this line
from PyQt6.QtWebEngineWidgets import QWebEngineView
from markdown import markdown as markdown

def get_checks():
    # load the data
    checks = pd.read_csv('data/checks.csv')
    return checks

class PandasModel(QAbstractTableModel):
    def __init__(self, df, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._df = df

    def rowCount(self, parent=None):
        return self._df.shape[0]

    def columnCount(self, parent=None):
        return self._df.shape[1]

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):  # Changed this line
        if index.isValid():
            if role == Qt.ItemDataRole.DisplayRole:  # Changed this line
                return str(self._df.iloc[index.row(), index.column()])
        return None

    def headerData(self, section, orientation, role):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:  # Changed this line
            return self._df.columns[section]
        return None

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GR Reverts")
        self.resize(800, 600)

        # Create a top-level layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create a QTableView and set its model
        self.tableView = QTableView()
        checks = get_checks()
        model = PandasModel(checks)
        self.tableView.setModel(model)

        # Add the QTableView to the layout
        layout.addWidget(self.tableView)

        # Set the main window's properties
        self.showMaximized()

def main():
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()