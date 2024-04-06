import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QRadioButton, QHBoxLayout, QGridLayout, QPushButton
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QPixmap, QTransform

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("PassiveElectronFlowAnalyser")

        leftPanel = QVBoxLayout()
        # Create radio buttons
        self.resistor_button = QRadioButton("Resistor")
        self.battery_button = QRadioButton("Battery")
        self.inductor_button = QRadioButton("Inductor")
        self.wire_button = QRadioButton("Wire")
        
        # Set "Wire" radio button as default selected
        self.wire_button.setChecked(True)

        # Connect radio buttons to slot
        self.resistor_button.clicked.connect(self.radio_button_clicked)
        self.battery_button.clicked.connect(self.radio_button_clicked)
        self.inductor_button.clicked.connect(self.radio_button_clicked)
        self.wire_button.clicked.connect(self.radio_button_clicked)

        leftPanel.addWidget(self.resistor_button)
        leftPanel.addWidget(self.battery_button)
        leftPanel.addWidget(self.inductor_button)
        leftPanel.addWidget(self.wire_button)

        # Create a "Clear" button
        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear_buttons)
        leftPanel.addWidget(clear_button)

        rightGrid = QGridLayout()
        rightGrid.setSpacing(0)
        rightGrid.setContentsMargins(0, 0, 0, 0)
        
        ##number of column and rows of the grid
        n = 15
        self.buttons = []  # List to hold all buttons
        self.button_rotations = {}  # Dictionary to store rotation angle for each button

        for i in range(n):
            for j in range(n):
                button = QPushButton()
                button.setCheckable(True)
                button.setFixedSize(QSize(30, 30))
                button.clicked.connect(lambda checked, i=i, j=j: self.button_clicked(i, j))
                rightGrid.addWidget(button, i, j)
                self.buttons.append(button)  # Add button to the list
                self.button_rotations[button] = 0  # Initial rotation angle is 0

        outerLayout = QHBoxLayout()
        outerLayout.addLayout(leftPanel)
        outerLayout.addLayout(rightGrid)

        widget = QWidget()
        widget.setLayout(outerLayout)
        self.setCentralWidget(widget)

        # Keep track of the active component
        self.active_component = "Wire"

    def radio_button_clicked(self):
        sender = self.sender()
        if sender.isChecked():
            self.active_component = sender.text()
            print("Active Component:", self.active_component)

    def button_clicked(self, row, col):
        print("Row, Col:", row, col, self.active_component)

        button = self.buttons[row * 15 + col]  # Get the button at the specified row and column
        icon_path = f"./icons/{self.active_component.lower()}.jpg"
        pixmap = QPixmap(icon_path)

        # Rotate the image
        rotation = self.button_rotations[button]
        rotation += 90
        if rotation >= 360:
            rotation = 0
        transform = QTransform().rotate(rotation)
        rotated_pixmap = pixmap.transformed(transform)

        # Set the rotated icon for the button
        button.setIcon(QIcon(rotated_pixmap))
        button.setIconSize(QSize(30, 30))

        # Update the rotation angle for the button
        self.button_rotations[button] = rotation

    def clear_buttons(self):
        for button in self.buttons:
            button.setChecked(False)
            button.setIcon(QIcon())  # Clear the icon
            self.button_rotations[button] = 0  # Reset rotation angle to 0
        print("Buttons Cleared")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
