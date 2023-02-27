import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QSlider, QPushButton, QFileDialog
from PyQt5.QtGui import QPixmap
from PIL import Image
from PIL.ImageQt import ImageQt
from PyQt5.QtCore import Qt


class ImageShifter(QWidget):
    def __init__(self):
        super().__init__()

        # Load the image
        self.image_path = None
        self.image = None
        self.image_width = 0
        self.image_height = 0

        # Create the GUI elements
        self.label = QLabel()
        self.slider = QSlider()
        self.slider.setMinimum(0)
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMaximum(self.image_width)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.setSingleStep(1)
        self.slider.setValue(0)
        self.slider.valueChanged.connect(self.shift_image)
        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_slider)
        self.x_label = QLabel()
        self.open_button = QPushButton("Open Image")
        self.open_button.clicked.connect(self.open_image)
        self.save_button = QPushButton("Save Image")
        self.save_button.clicked.connect(self.save_image)

        # Create the layout and add the elements
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.slider)
        h_layout.addWidget(self.reset_button)
        h_layout.addWidget(self.open_button)
        h_layout.addWidget(self.save_button)
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.label)
        v_layout.addWidget(self.x_label)
        v_layout.addLayout(h_layout)
        self.setLayout(v_layout)
        # Set the window properties
        self.setWindowTitle("Image Shifter")
        self.setGeometry(100, 100, self.image_width, self.image_height + self.slider.height() + 50)
        self.show()
        
    def open_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Image Files (*.png *.jpg *.bmp)")
        if file_path:
            self.image_path = file_path
            self.image = Image.open(self.image_path).convert("RGBA")
            self.image_width, self.image_height = self.image.size
            self.slider.setMaximum(self.image_width)
            self.reset_slider()
            self.label.setPixmap(QPixmap.fromImage(ImageQt(self.image)))

    def save_image(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image File", "", "PNG Files (*.png)")
        if file_path:
            shifted_image = self.get_shifted_image()
            shifted_image.save(file_path) 

    def shift_image(self, value):
        # Clamp the slider value to the range [0, self.image_width]
        value = max(0, min(value, self.image_width))

        # Shift the original image
        shifted_image = Image.new("RGBA", (self.image_width, self.image_height))
        shifted_image.paste(self.image, (value, 0))
        shifted_image.paste(self.image, (value - self.image_width, 0))

        # Update the label with the shifted image (if the label has a pixmap)
        if self.label.pixmap() is not None:
            pixmap = QPixmap.fromImage(ImageQt(shifted_image.convert("RGBA")))
            self.label.setPixmap(pixmap)

        # Update the x label
        self.x_label.setText(f"X: {value}")
    def get_shifted_image(self):
        # Get the current value of the slider
        value = self.slider.value()

        # Clamp the slider value to the range [0, self.image_width]
        value = max(0, min(value, self.image_width))

        # Shift the original image
        shifted_image = Image.new("RGBA", (self.image_width, self.image_height))
        shifted_image.paste(self.image, (value, 0))
        shifted_image.paste(self.image, (value - self.image_width, 0))

        return shifted_image
    
    def reset_slider(self):
        # Reset the slider to 0
        self.slider.setValue(0)

        # Update the label with the original image
        if self.label.pixmap() is not None:
            self.label.setPixmap(QPixmap.fromImage(ImageQt(self.image)))

        # Update the x label
        self.x_label.setText("X: 0")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    shifter = ImageShifter()
    sys.exit(app.exec_())