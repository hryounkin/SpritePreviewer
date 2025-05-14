#Henry Younkin
#u1511014
#A7: Sprite Previewer

import math

from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *

# This function loads a series of sprite images stored in a folder with a
# consistent naming pattern: sprite_# or sprite_##. It returns a list of the images.
def load_sprite(sprite_folder_name, number_of_frames):
    frames = []
    padding = math.ceil(math.log(number_of_frames - 1, 10))
    for frame in range(number_of_frames):
        folder_and_file_name = sprite_folder_name + "/sprite_" + str(frame).rjust(padding, '0') + ".png"
        frames.append(QPixmap(folder_and_file_name))

    return frames

class SpritePreview(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Animation Preview")
        # This loads the provided sprite and would need to be changed for your own.
        self.num_frames = 10
        self.frames = load_sprite('spriteImages',self.num_frames)

        # Add any other instance variables needed to track information as the program
        # runs here
        self.timer = QTimer(self)
        self.current_frame = 0


        # Make the GUI in the setupUI method
        self.setupUI()


    def setupUI(self):
        # An application needs a central widget - often a QFrame
        frame = QFrame()

        self.piclabel = QLabel()
        self.fps_label = QLabel()
        self.slider = QSlider()
        self.slider.setRange(1, 60)
        self.slider.valueChanged.connect(self.update_fps)
        self.startbutton = QPushButton("Start")
        self.startbutton.clicked.connect(self.startAnimation)
        self.exitbutton = QPushButton("Exit")
        self.exitbutton.clicked.connect(self.close)


        h_layout = QHBoxLayout()
        h_layout.addWidget(self.piclabel)
        h_layout.addWidget(self.slider)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.fps_label)
        v_layout.addWidget(self.startbutton)
        v_layout.addWidget(self.exitbutton)

        frame.setLayout(v_layout)

        self.piclabel.setPixmap(self.frames[self.current_frame])
        self.setCentralWidget(frame)


    # You will need methods in the class to act as slots to connect to signals
    def startAnimation(self):
        if self.timer.isActive():
            self.timer.stop()
            self.startbutton.setText("Start")
        else:
            self.timer.timeout.connect(self.update_frame)
            self.startbutton.setText("Stop")
            self.timer.start(1000//self.slider.value())

    def update_frame(self):
        self.current_frame += 1
        if self.current_frame >= len(self.frames):
            self.current_frame = 0
        self.piclabel.setPixmap(self.frames[self.current_frame])


    def update_fps(self, current_fps):
        self.fps_label.setText("Frames per second: "+str(current_fps))
        if self.timer.isActive():
            self.timer.setInterval(1000//self.slider.value())



def main():
    app = QApplication([])
    # Create our custom application
    window = SpritePreview()
    # And show it
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
