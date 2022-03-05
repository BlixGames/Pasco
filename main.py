import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *




class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)
        from PyQt5.QtCore import Qt
        from PyQt5.QtWidgets import QApplication
        ...
        QApplication.setOverrideCursor(Qt.CrossCursor)
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('http://google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('Pasco v1.01.1')
window = MainWindow()
app.exec_()

# importing the required libraries

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import sys




class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.acceptDrops()
        # set the title
        self.setWindowTitle("Pasco Launcher")

        # setting the geometry of window
        self.setGeometry(0, 0, 400, 300)

        # creating label
        self.label = QLabel(self)

        # loading image
        self.pixmap = QPixmap('festisite_google.png')

        # adding image to label
        self.label.setPixmap(self.pixmap)

        # Optional, resize label to image size
        self.label.resize(self.pixmap.width(),
                          self.pixmap.height())

        # show all the widgets
        self.show()


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# start the app
sys.exit(App.exec())

import pickle


class MyClass():
    def __init__(self, param):
        self.param = param


def save_object(obj):
    try:
        with open("data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)


obj = MyClass(10)
save_object(obj)

import pickle


class MyClass():
    def __init__(self, param):
        self.param = param


def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)


obj = load_object("data.pickle")

print(obj.param)
print(isinstance(obj, MyClass))


import tkinter as tk
import tkinter.ttk as ttk
import time

class App(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.button = ttk.Button(master=self.master, text='Run task', command=self.onclick_button)
        self.button.grid(padx=25, pady=25)

    def set_cursor_busy(self):
        self.button.config(cursor='watch')
        self.update_idletasks()

    def reset_cursor(self):
        self.config(cursor='')

    def onclick_button(self):
        self.set_cursor_busy()
        time.sleep(5)           # Simulate a long running task.
        self.reset_cursor()


root = tk.Tk()
app = App(master=root)
app.mainloop()

