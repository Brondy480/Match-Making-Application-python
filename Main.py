import sys
from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QApplication
from welcome import WelcomeScreen

##########################################
##  RUNNING THE APPLICATION             ##
##########################################

#RIEN POUR TOI MAN


app = QApplication(sys.argv)
widget = QStackedWidget()
welcomewindow = WelcomeScreen(widget)
widget.addWidget(welcomewindow)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
sys.exit(app.exec_())


# THIS MAXIMUS AND I WROTE THIS COMMENT

#THERE ARE A LOT OF THINGS TO DEAL WITH MAN

# I made this Change in my phone
