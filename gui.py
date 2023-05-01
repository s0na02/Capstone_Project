from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor
import sys

from bond_calc import test
from form import Form


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # set the title of main window
        self.setWindowTitle('Bond Calculator')

        # set the size of window
        self.Width = 800
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)

        # set background color
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(220, 230, 241))
        palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
        self.setPalette(palette)

        # add tabs
        self.initUI()


    def initUI(self):
        result_layout = QVBoxLayout()
        self.result_widget = QTabWidget()
        self.result_widget.setLayout(result_layout)
        self.res_label = QLabel()
        result_layout.addWidget(self.res_label)

        self.form_widget = QTabWidget()
        self.form_widget.tabBar().setObjectName("mainTab")

        self.form_widget.addTab(self.ui1(), '')

        self.form_widget.setCurrentIndex(0)
        self.form_widget.setStyleSheet('''QTabBar::tab{width: 0; \
            height: 0; margin: 0; padding: 0; border: none;}''')

        main_layout = QHBoxLayout()
        main_layout.addWidget(self.form_widget)
        main_layout.addWidget(self.result_widget)
        # main_layout.setStretch(0, 40)
        main_layout.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)

        # set upper margin color
        upper_margin = QWidget(self)
        upper_margin.setGeometry(0, 0, self.Width, int(0.05 * self.height))
        upper_margin.setAutoFillBackground(True)
        upper_palette = QPalette()
        upper_palette.setColor(QPalette.Window, QColor(0, 0, 139))
        upper_margin.setPalette(upper_palette)

        main_v_layout = QVBoxLayout()
        main_v_layout.addWidget(upper_margin)
        main_v_layout.addWidget(main_widget)

        main_widget_2 = QWidget(self)
        main_widget_2.setLayout(main_v_layout)
        self.setCentralWidget(main_widget_2)

    # -----------------
    # pages

    def ui1(self):
        main_layout = QVBoxLayout()

        fields = [
            {
                'label': 'Principal value',
                'name': 'pvalue'
            },
            {
                'label': 'Coupon rate',
                'name': 'crate'
            },
            {
                'label': 'Coupon frequency',
                'name': 'cfreq'
            },
            {
                'label': 'Settlement date',
                'name': 'sdate',
            },
            {
                'label': 'Maturity date',
                'name': 'mdate',
            },
            {
                'label': 'Yield to mat',
                'name': 'ymat',
            },
            {
                'label': 'Convention',
                'name': 'conv',
            },
        ]
        form = Form(fields, test, self.res_label)
        main_layout.addWidget(form)

        main = QWidget()
        main.setLayout(main_layout)

        return main


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
