Image Shifter
This is a PyQt5 GUI application that allows you to shift the position of an image horizontally using a slider. It loads an image file and displays it in a QLabel. The user can move the slider left or right to shift the image. The X position of the image is displayed in a QLabel. The user can reset the slider to the initial position or save the shifted image to a file.

Prerequisites
Python 3.x
PyQt5
Pillow (PIL)
Usage
Run the ImageShifter.py script using Python.

Click on the "Open Image" button to select an image file.

Use the slider to shift the image left or right. The X position of the image will be displayed in a QLabel.

Click on the "Reset" button to reset the slider to the initial position.

Click on the "Save Image" button to save the shifted image to a file.

Code
The application is defined in the ImageShifter class, which inherits from QWidget. It contains the following elements:

image_path: the path to the loaded image file
image: the loaded image object
image_width and image_height: the dimensions of the loaded image
label: the QLabel that displays the image
slider: the QSlider that controls the horizontal position of the image
reset_button: the QPushButton that resets the slider to the initial position
x_label: the QLabel that displays the X position of the image
open_button: the QPushButton that opens an image file
save_button: the QPushButton that saves the shifted image to a file
The open_image method opens an image file and loads it into the image object. It updates the dimensions of the image, sets the maximum value of the slider, and resets the slider to the initial position. It also displays the loaded image in the label.

The save_image method saves the shifted image to a file. It first creates a new image object that contains the shifted image, then saves it to a file using the getSaveFileName method of the QFileDialog class.

The shift_image method is called every time the value of the slider is changed. It shifts the original image and displays the shifted image in the label. It also updates the x_label with the current X position of the image.

The get_shifted_image method returns an image object that contains the shifted image.

The reset_slider method resets the slider to the initial position and displays the original image in the label. It also updates the x_label.

The ImageShifter class is instantiated and shown using the QApplication class.

License
This code is licensed under the MIT license.