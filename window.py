from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(330, 250)
        font = QtGui.QFont()
        font.setPointSize(8)
        window.setFont(font)
        window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        window.setWindowTitle("Cámara frigorífica")
        self.env_box = QtWidgets.QGroupBox(window)
        self.env_box.setGeometry(QtCore.QRect(10, 10, 231, 171))
        self.env_box.setObjectName("env_box")
        self.chamber_box = QtWidgets.QGroupBox(self.env_box)
        self.chamber_box.setGeometry(QtCore.QRect(10, 50, 211, 111))
        self.chamber_box.setObjectName("chamber_box")
        self.label_2 = QtWidgets.QLabel(self.chamber_box)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.chamber_box)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 91, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.chamber_box)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 91, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.chamber_box)
        self.label_5.setGeometry(QtCore.QRect(190, 20, 21, 21))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.chamber_box)
        self.label_6.setGeometry(QtCore.QRect(190, 50, 21, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.chamber_box)
        self.label_7.setGeometry(QtCore.QRect(190, 80, 21, 21))
        self.label_7.setObjectName("label_7")
        self.int_temp_entry = QtWidgets.QLineEdit(self.chamber_box)
        self.int_temp_entry.setGeometry(QtCore.QRect(110, 20, 71, 20))
        self.int_temp_entry.setObjectName("int_temp_entry")
        self.perfo_entry = QtWidgets.QLineEdit(self.chamber_box)
        self.perfo_entry.setGeometry(QtCore.QRect(110, 50, 71, 20))
        self.perfo_entry.setObjectName("perfo_entry")
        self.power_entry = QtWidgets.QLineEdit(self.chamber_box)
        self.power_entry.setGeometry(QtCore.QRect(110, 80, 71, 20))
        self.power_entry.setObjectName("power_entry")
        self.label = QtWidgets.QLabel(self.env_box)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 21))
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(self.env_box)
        self.label_8.setGeometry(QtCore.QRect(200, 20, 21, 21))
        self.label_8.setObjectName("label_8")
        self.ext_temp_entry = QtWidgets.QLineEdit(self.env_box)
        self.ext_temp_entry.setGeometry(QtCore.QRect(120, 20, 71, 20))
        self.ext_temp_entry.setObjectName("ext_temp_entry")
        self.results_box = QtWidgets.QGroupBox(window)
        self.results_box.setGeometry(QtCore.QRect(10, 190, 311, 51))
        self.results_box.setObjectName("results_box")
        self.cop_result_label = QtWidgets.QLabel(self.results_box)
        self.cop_result_label.setGeometry(QtCore.QRect(10, 20, 71, 21))
        self.cop_result_label.setObjectName("cop_result_label")
        self.effi_result_label = QtWidgets.QLabel(self.results_box)
        self.effi_result_label.setGeometry(QtCore.QRect(90, 20, 111, 21))
        self.effi_result_label.setObjectName("effi_result_label")
        self.heat_result_label = QtWidgets.QLabel(self.results_box)
        self.heat_result_label.setGeometry(QtCore.QRect(220, 20, 101, 21))
        self.heat_result_label.setObjectName("heat_result_label")
        self.del_button = QtWidgets.QPushButton(window)
        self.del_button.setGeometry(QtCore.QRect(250, 50, 75, 23))
        self.del_button.setObjectName("del_button")
        self.del_button.clicked.connect(self.delete) #Función del botón
        self.calc_button = QtWidgets.QPushButton(window)
        self.calc_button.setGeometry(QtCore.QRect(250, 20, 75, 23))
        self.calc_button.setCheckable(False)
        self.calc_button.setObjectName("calc_button")
        self.calc_button.clicked.connect(self.calculate) #Función del botón

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        self.env_box.setTitle(_translate("window", "Ambiente"))
        self.chamber_box.setTitle(_translate("window", "Cámara frigorífica"))
        self.label_2.setText(_translate("window", "Temperatura"))
        self.label_3.setText(_translate("window", "Rendimiento"))
        self.label_4.setText(_translate("window", "Potencia"))
        self.label_5.setText(_translate("window", "°C"))
        self.label_6.setText(_translate("window", "%"))
        self.label_7.setText(_translate("window", "kW"))
        self.label.setText(_translate("window", "Temperatura"))
        self.label_8.setText(_translate("window", "°C"))
        self.results_box.setTitle(_translate("window", "Resultados"))
        self.cop_result_label.setText(_translate("window", "COP:"))
        self.effi_result_label.setText(_translate("window", "Eficiencia:"))
        self.heat_result_label.setText(_translate("window", "Calor:"))
        self.del_button.setText(_translate("window", "Borrar"))
        self.calc_button.setText(_translate("window", "Calcular"))

    # ----- Define variable -----
    cop = 0
    effi = 0
    heat = 0
    # ----- Get values from entry -----
    def get_ext_temp(self):
        return float(self.ext_temp_entry.text())

    def get_int_temp(self):
        return float(self.int_temp_entry.text())
    
    def get_perfo(self):
        return float(self.perfo_entry.text())
    
    def get_power(self):
        return float(self.power_entry.text())
    # -------------------------------

    def celcius_to_kelvin(self,temp):
        return temp+273
    
    def coefficient_of_perfomance(self):
        temp_int = self.celcius_to_kelvin(self.get_int_temp())
        temp_ext = self.celcius_to_kelvin(self.get_ext_temp())
        self.cop = temp_int/(temp_ext-temp_int)
    
    def efficiency(self):
        self.effi = self.get_perfo()*self.cop
    
    def heat_flux(self):
        self.heat = (self.effi/100)*self.get_power()

    def calculate(self):
        try:
            self.coefficient_of_perfomance()
            self.efficiency()
            self.heat_flux()
            self.cop_result_label.setText(f"COP: {abs(self.cop):.2f}")
            self.effi_result_label.setText(f"Eficiencia: {abs(self.effi):.2f} %")
            self.heat_result_label.setText(f"Calor: {(self.heat):.2f} kW")
        except:
            print("Error al calcular.")
    
    def delete(self):
        self.cop_result_label.setText("COP:")
        self.effi_result_label.setText("Eficiencia:")
        self.heat_result_label.setText("Calor:")
        self.ext_temp_entry.clear()
        self.int_temp_entry.clear()
        self.perfo_entry.clear()
        self.power_entry.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QDialog()
    ui = Ui_window()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
