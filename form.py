from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class Form(QWidget):
    def __init__(self, fields, calculate_callback, result_tab):
        super().__init__()
        self.labels = {}
        self.inputs = {}
        self.fields = fields

        self.result_tab = result_tab

        self.vbox = QVBoxLayout()
        self.initUI(fields)
        self.result_field = QLabel('', self)
        # self.result_field.setFixedWidth()
        # self.result_field.setFixedWidth(200)
        self.vbox.addWidget(self.result_field)
        self.calculate_value = calculate_callback
        self.setLayout(self.vbox)

    def initUI(self, fields):
        self.setWindowTitle('Number Input Form')
        self.setGeometry(100, 100, 300, 150)

        for field in fields:
            input = QLineEdit(self)
            self.inputs[field['name']] = input
            label = QLabel(field['label'], self)
            self.labels[field['name']] = label

            hbox = QHBoxLayout()
            hbox.addWidget(label)
            hbox.addWidget(input)
            self.vbox.addLayout(hbox)

        # Create the submit button
        self.submit_button = QPushButton('Submit', self)
        self.submit_button.clicked.connect(self.submit)

        self.vbox.addWidget(self.submit_button)

    def submit(self):
        try:
            values = []
            for field in self.fields:
                values.append(self.inputs[field['name']].text())

            res = self.calculate_value(values)

            self.result_tab.setText(f"Dirty price: {res[0]}\n"
                                    f"Clean price: {res[1]}\n"
                                    f"Accrued interest: {res[2]}\n"
                                    f"Face value: {res[3]}\n"
                                    f"Coupon rate: {res[4]}\n"
                                    f"Coupon frequency: {res[5]}\n"
                                    f"Yield to maturity: {res[6]}\n"
                                    f"Time to maturity: {res[7]}\n"
                                    f"Macaulay duration: {res[8]}\n"
                                    f"Modified duration: {res[9]}\n"
                                    f"Convexity: {res[10]}\n"
                                    f"Settlement date: {res[11]}\n"
                                    f"Maturity date: {res[12]}\n"
                                    f"Convention: {res[13]}\n"
                                    )
            # if not isinstance(res, str):
            #     res = "{:6.2f}".format(res)
            #
            # print(res)

            # self.result_field.setText(f"Result is: {str(res)}")
        except:
            self.result_field.setText("Wrong input")
