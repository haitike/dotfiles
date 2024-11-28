# Form implementation generated from reading ui file 'ankimorphs/ui/known_morphs_exporter_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_KnownMorphsExporterDialog(object):
    def setupUi(self, KnownMorphsExporterDialog):
        KnownMorphsExporterDialog.setObjectName("KnownMorphsExporterDialog")
        KnownMorphsExporterDialog.resize(519, 293)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(KnownMorphsExporterDialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectOutputPushButton = QtWidgets.QPushButton(parent=KnownMorphsExporterDialog)
        self.selectOutputPushButton.setObjectName("selectOutputPushButton")
        self.horizontalLayout.addWidget(self.selectOutputPushButton)
        self.outputLineEdit = QtWidgets.QLineEdit(parent=KnownMorphsExporterDialog)
        self.outputLineEdit.setObjectName("outputLineEdit")
        self.horizontalLayout.addWidget(self.outputLineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(parent=KnownMorphsExporterDialog)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.storeOnlyMorphLemmaRadioButton = QtWidgets.QRadioButton(parent=KnownMorphsExporterDialog)
        self.storeOnlyMorphLemmaRadioButton.setObjectName("storeOnlyMorphLemmaRadioButton")
        self.horizontalLayout_4.addWidget(self.storeOnlyMorphLemmaRadioButton)
        self.storeMorphLemmaAndInflectionRadioButton = QtWidgets.QRadioButton(parent=KnownMorphsExporterDialog)
        self.storeMorphLemmaAndInflectionRadioButton.setObjectName("storeMorphLemmaAndInflectionRadioButton")
        self.horizontalLayout_4.addWidget(self.storeMorphLemmaAndInflectionRadioButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(parent=KnownMorphsExporterDialog)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(3, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=KnownMorphsExporterDialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.knownIntervalSpinBox = QtWidgets.QSpinBox(parent=KnownMorphsExporterDialog)
        self.knownIntervalSpinBox.setObjectName("knownIntervalSpinBox")
        self.horizontalLayout_2.addWidget(self.knownIntervalSpinBox, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label = QtWidgets.QLabel(parent=KnownMorphsExporterDialog)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignLeft)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=KnownMorphsExporterDialog)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.addOccurrencesColumnCheckBox = QtWidgets.QCheckBox(parent=KnownMorphsExporterDialog)
        self.addOccurrencesColumnCheckBox.setObjectName("addOccurrencesColumnCheckBox")
        self.verticalLayout_2.addWidget(self.addOccurrencesColumnCheckBox)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.exportKnownMorphsPushButton = QtWidgets.QPushButton(parent=KnownMorphsExporterDialog)
        self.exportKnownMorphsPushButton.setObjectName("exportKnownMorphsPushButton")
        self.horizontalLayout_3.addWidget(self.exportKnownMorphsPushButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.retranslateUi(KnownMorphsExporterDialog)
        QtCore.QMetaObject.connectSlotsByName(KnownMorphsExporterDialog)

    def retranslateUi(self, KnownMorphsExporterDialog):
        _translate = QtCore.QCoreApplication.translate
        KnownMorphsExporterDialog.setWindowTitle(_translate("KnownMorphsExporterDialog", "Known Morphs Exporter"))
        self.selectOutputPushButton.setText(_translate("KnownMorphsExporterDialog", "Select Output Directory"))
        self.label_3.setText(_translate("KnownMorphsExporterDialog", "Morph version"))
        self.storeOnlyMorphLemmaRadioButton.setText(_translate("KnownMorphsExporterDialog", "Lemmas"))
        self.storeMorphLemmaAndInflectionRadioButton.setText(_translate("KnownMorphsExporterDialog", "Inflections"))
        self.label_5.setText(_translate("KnownMorphsExporterDialog", "Morph learning interval"))
        self.label_2.setText(_translate("KnownMorphsExporterDialog", "Morphs with interval "))
        self.label.setText(_translate("KnownMorphsExporterDialog", "days or higher"))
        self.label_4.setText(_translate("KnownMorphsExporterDialog", "Extra"))
        self.addOccurrencesColumnCheckBox.setText(_translate("KnownMorphsExporterDialog", "Add occurrences column"))
        self.exportKnownMorphsPushButton.setText(_translate("KnownMorphsExporterDialog", "Export Known Morphs"))