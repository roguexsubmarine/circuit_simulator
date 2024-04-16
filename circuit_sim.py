import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QRadioButton, QHBoxLayout, QGridLayout, QPushButton, QLineEdit
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QPixmap, QTransform

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("PassiveElectronFlowAnalyser")

        leftPanel = QVBoxLayout()

        self.inputValue = QLineEdit()
        self.inputValue.setMaxLength(5)
        self.inputValue.setPlaceholderText("Enter your Value")
        self.inputValue.returnPressed.connect(self.return_pressed)  # Connect to method in MainWindow
        self.inputValue.selectionChanged.connect(self.selection_changed)
        self.inputValue.textChanged.connect(self.text_changed)
        self.inputValue.textEdited.connect(self.text_edited)


        ### Create radio buttons
        self.resistor_button = QRadioButton("Resistor")
        self.battery_button = QRadioButton("Battery")
        self.wire_button = QRadioButton("Wire")
        self.node_button = QRadioButton("Node")
        
        ## Set "Wire" radio button as default selected
        self.wire_button.setChecked(True)

        ## Connect radio buttons to slot
        self.resistor_button.clicked.connect(self.radio_button_clicked)
        self.battery_button.clicked.connect(self.radio_button_clicked)
        self.wire_button.clicked.connect(self.radio_button_clicked)
        self.node_button.clicked.connect(self.radio_button_clicked)


        ### Adding components to left Panel 
        leftPanel.addWidget(self.inputValue)
        leftPanel.addWidget(self.resistor_button)
        leftPanel.addWidget(self.battery_button)
        leftPanel.addWidget(self.wire_button)
        leftPanel.addWidget(self.node_button)

        ## Create a "Clear" button
        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.clear_buttons)
        leftPanel.addWidget(clear_button)

        rightGrid = QGridLayout()
        rightGrid.setSpacing(0)
        rightGrid.setContentsMargins(0, 0, 0, 0)
        
        ## number of column and rows of the grid
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

        ## Keep track of the active component
        self.active_component = "Wire"

    def return_pressed(self):
        # This method will be called when the return key is pressed in the QLineEdit
        text = self.inputValue.text()
        print("Return Pressed:", text)

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

        ## Rotate the image
        rotation = self.button_rotations[button]
        rotation += 90
        if rotation >= 360:
            rotation = 0
        transform = QTransform().rotate(rotation)
        rotated_pixmap = pixmap.transformed(transform)

        ## Set the rotated icon for the button
        button.setIcon(QIcon(rotated_pixmap))
        button.setIconSize(QSize(30, 30))

        ## Update the rotation angle for the button
        self.button_rotations[button] = rotation

    def clear_buttons(self):
        for button in self.buttons:
            button.setChecked(False)
            button.setIcon(QIcon())  # Clear the icon
            self.button_rotations[button] = 0  # Reset rotation angle to 0
        print("Buttons Cleared")


    def return_pressed(self):
        print("Return pressed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)




app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
