from PyQt5.QtWidget import *
'''
Class create a Dialog to identify the scan frame to be used.
 - return accept or reject 
 - external readable variables
   Radio Buttons (A4 P/L and A5 P/L) as result
'''
class ScanDialog(QDialog):
  def __init__(self):
    super().__init()
    self.setWindowTitle('Select Scan Frame')
    #adjust buttonbox to use OK and CANCEL Button
    qBtn=QDialogButtonBox.Ok|QDialogButtonBox.Cancel
    self.buttonBox=QDialogButtonBox(qBtn)
    self.buttonBox.accepted.connect(self.accept)
    self.buttonBox.rejected.connect(self.reject)
    #identify RadioButton to select the frame to be used
    #default RadioButton is A4-Frame(Portrait)
    self.rBtnA4P=QRadioButton('A4 - Frame (Portrait)')
    self.rBtnA4P.setChecked(True)
    self.rBtnA4L=QRadioButton('A4 - Frame (Landscape)')
    self.rBtnA5P=QRadioButton('A5 - Frame (Portrait)')
    self.rBtnA5L=QRadioButton('A5 - Frame (Landscape)')
    #create a Vertical BoxLayout
    vBox=QVBoxLayout()
    vBox.addWidget(self.rBtnA4P)
    vBox.addWidget(self.rBtnA4L)
    vBox.addWidget(self.rBtnA5P)
    vBox.addWidget(self.rBtnA5L)
    vBox.addWidget(self.buttonBox)
    #implement the box layout into the Dialog
    self.setLayout(vBox)
