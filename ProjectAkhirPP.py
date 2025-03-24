from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout)

class GradeClaculatorApp(QWidget):
    def __init__(self): 
        super().__init__()
        self.initUI()

    def initUI(self): 
        self.page1 = QWidget()
        self.initPage1()

        self.page2 = QWidget()
        self.initPage2()

        self.page3 = QWidget()
        self.initPage3()

        self.setWindowTitle('Aplikasi Prediksi Nilai')
        self.setGeometry(300,300,600,400) #ngatur ukuran windownya

        self.page2.hide()
        self.page3.hide()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.page1)
        self.mainLayout.addWidget(self.page2)
        self.mainLayout.addWidget(self.page3)
        self.setLayout(self.mainLayout)

    def initPage1(self):
        layout1 = QVBoxLayout()
        judulapp = QLabel('Aplikasi ini membantu memprediksi hasil nilai-nilai kalian')
        layout1.addWidget(judulapp)
        
        selanjutnya = QPushButton('Next', self)
        selanjutnya.clicked.connect(self.gotoPage2)
        layout1.addWidget(selanjutnya)

        self.page1.setLayout(layout1)

    def initPage2(self):
        layout2 = QVBoxLayout()
        #input nilai 
        self.nilai = QLineEdit(self)
        self.nilai.setPlaceholderText("Masukkan nilai kalian pisahkan  dengan spasi (contoh: 80 90 85) ")
        layout2.addWidget(self.nilai)

        #input for KKM 
        self.nilaiKKM = QLineEdit(self)
        self.nilaiKKM.setPlaceholderText("Masukkan nilai KKM Anda")
        layout2.addWidget(self.nilaiKKM)

        #submit button
        self.submitnilai = QPushButton('Submit', self)
        self.submitnilai.clicked.connect(self.gotoPage3)
        layout2.addWidget(self.submitnilai)

        self.page2.setLayout(layout2)
       
    def initPage3(self): 
        layout3 = QVBoxLayout()
        
        self.labelhasil = QLabel('',self)
        layout3.addWidget(self.labelhasil)

        backbutton = QPushButton('Back', self)
        backbutton.clicked.connect(self.gotoPage2) 
        layout3.addWidget(backbutton)

        self.page3.setLayout(layout3)       

    def gotoPage2(self): 
        self.page1.hide()
        self.page2.show()
        self.page3.hide()
    
    def gotoPage3(self): 
        self.page1.hide()
        self.page2.hide()
        self.page3.show()
    
        #Get the input 
        nilai_input = self.nilai.text()
        kkm_input = self.nilaiKKM.text()

        nilai_list = list(map(int, nilai_input.split()))
        nilaikkm = int(kkm_input)

        #calculate the average 
        avg_nilai = sum(nilai_list) / len(nilai_list)
        minus = nilaikkm - avg_nilai

        if avg_nilai >= nilaikkm:
            self.labelhasil.setText(f"Rata-rata nilai Anda adalah {avg_nilai:.2f}. Selamat, Anda lulus!")            
        else:
            self.labelhasil.setText(f"Rata-rata nilai Anda adalah {avg_nilai:.2f}. Maaf, Anda belum lulus.\nAnda perlu meningkatkan nilai Anda sebesar {minus:.2f} ")


    
def main(): 
    app = QApplication([])
    ex = GradeClaculatorApp()
    ex.show()
    app.exec_()

if __name__ == '__main__':
    main()


