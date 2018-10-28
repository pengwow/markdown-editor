# -*- coding: utf-8 -*-
from src.MainWindow import *
import sys

if __name__=="__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    main_widown=QtWidgets.QMainWindow()
    ui=Ui_MainWindow()
    ui.setupUi(main_widown)
    main_widown.show()
    sys.exit(app.exec_())