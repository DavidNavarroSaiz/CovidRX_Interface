# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui_designer.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1021, 497)
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionAbout_2 = QAction(MainWindow)
        self.actionAbout_2.setObjectName(u"actionAbout_2")
        self.actionVgg19 = QAction(MainWindow)
        self.actionVgg19.setObjectName(u"actionVgg19")
        self.actionVgg19.setCheckable(True)
        self.actionVgg19.setChecked(True)
        self.actionDenseNet = QAction(MainWindow)
        self.actionDenseNet.setObjectName(u"actionDenseNet")
        self.actionDenseNet.setCheckable(True)
        self.actionDenseNet.setChecked(True)
        self.actionMobileNet = QAction(MainWindow)
        self.actionMobileNet.setObjectName(u"actionMobileNet")
        self.actionMobileNet.setCheckable(True)
        self.actionMobileNet.setChecked(True)
        self.actionAlexNet = QAction(MainWindow)
        self.actionAlexNet.setObjectName(u"actionAlexNet")
        self.actionAlexNet.setCheckable(True)
        self.actionAlexNet.setChecked(False)
        self.actionEfficientNet = QAction(MainWindow)
        self.actionEfficientNet.setObjectName(u"actionEfficientNet")
        self.actionEfficientNet.setCheckable(True)
        self.actionEfficientNet.setChecked(True)
        self.actionInceptionV3 = QAction(MainWindow)
        self.actionInceptionV3.setObjectName(u"actionInceptionV3")
        self.actionInceptionV3.setCheckable(True)
        self.actionInceptionV3.setChecked(False)
        self.actionResNet_2 = QAction(MainWindow)
        self.actionResNet_2.setObjectName(u"actionResNet_2")
        self.actionResNet_2.setCheckable(True)
        self.actionResNet_2.setChecked(True)
        self.actionRexNet = QAction(MainWindow)
        self.actionRexNet.setObjectName(u"actionRexNet")
        self.actionRexNet.setCheckable(True)
        self.actionRexNet.setChecked(True)
        self.actionInception_ResNet = QAction(MainWindow)
        self.actionInception_ResNet.setObjectName(u"actionInception_ResNet")
        self.actionInception_ResNet.setCheckable(True)
        self.actionInception_ResNet.setChecked(True)
        self.actionXception = QAction(MainWindow)
        self.actionXception.setObjectName(u"actionXception")
        self.actionXception.setCheckable(True)
        self.actionXception.setChecked(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.labelLogoFlir = QLabel(self.centralwidget)
        self.labelLogoFlir.setObjectName(u"labelLogoFlir")
        self.labelLogoFlir.setGeometry(QRect(9, 200, 1069, 186))
        self.labelLogo = QLabel(self.centralwidget)
        self.labelLogo.setObjectName(u"labelLogo")
        self.labelLogo.setGeometry(QRect(9, -7, 1069, 201))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frameDisplayImage = QFrame(self.centralwidget)
        self.frameDisplayImage.setObjectName(u"frameDisplayImage")
        self.frameDisplayImage.setFrameShape(QFrame.StyledPanel)
        self.frameDisplayImage.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frameDisplayImage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.frameDisplayImage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(371, 381))
        self.label_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)

        self.done_run = QLabel(self.frameDisplayImage)
        self.done_run.setObjectName(u"done_run")

        self.horizontalLayout_5.addWidget(self.done_run)

        self.pushButtonRun = QPushButton(self.frameDisplayImage)
        self.pushButtonRun.setObjectName(u"pushButtonRun")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.pushButtonRun.setFont(font1)

        self.horizontalLayout_5.addWidget(self.pushButtonRun)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)


        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.frameDisplayImage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(371, 381))
        self.label_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.label_4)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.done_load = QLabel(self.frameDisplayImage)
        self.done_load.setObjectName(u"done_load")

        self.horizontalLayout_4.addWidget(self.done_load)

        self.pushload = QPushButton(self.frameDisplayImage)
        self.pushload.setObjectName(u"pushload")
        self.pushload.setEnabled(True)
        font2 = QFont()
        font2.setPointSize(12)
        font2.setStrikeOut(False)
        self.pushload.setFont(font2)
        self.pushload.setFlat(False)

        self.horizontalLayout_4.addWidget(self.pushload)

        self.horizontalSpacer_6 = QSpacerItem(30, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.frame = QFrame(self.frameDisplayImage)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_covid = QLabel(self.frame)
        self.label_covid.setObjectName(u"label_covid")
        self.label_covid.setMaximumSize(QSize(150, 50))
#if QT_CONFIG(tooltip)
        self.label_covid.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.label_covid.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_covid.setWordWrap(False)

        self.gridLayout_4.addWidget(self.label_covid, 0, 2, 1, 1)

        self.universidad = QLabel(self.frame)
        self.universidad.setObjectName(u"universidad")
        self.universidad.setMaximumSize(QSize(400, 50))
        self.universidad.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout_4.addWidget(self.universidad, 1, 2, 1, 1)

        self.FinalPrediction = QLabel(self.frame)
        self.FinalPrediction.setObjectName(u"FinalPrediction")
        self.FinalPrediction.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setPointSize(12)
        self.FinalPrediction.setFont(font3)

        self.gridLayout_4.addWidget(self.FinalPrediction, 2, 2, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetMinimumSize)
        self.gridLayout_3.setVerticalSpacing(29)
        self.gridLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        self.progressBar_2 = QProgressBar(self.frame)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(0)

        self.verticalLayout.addWidget(self.progressBar_2)

        self.progressBar_3 = QProgressBar(self.frame)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setValue(0)

        self.verticalLayout.addWidget(self.progressBar_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setPointSize(11)
        self.label_2.setFont(font4)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)

        self.verticalLayout_2.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font4)

        self.verticalLayout_2.addWidget(self.label_7)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.gridLayout_3.addLayout(self.verticalLayout_5, 1, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 3, 0, 1, 4)

        self.SaveButton = QPushButton(self.frame)
        self.SaveButton.setObjectName(u"SaveButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveButton.sizePolicy().hasHeightForWidth())
        self.SaveButton.setSizePolicy(sizePolicy)
        self.SaveButton.setFont(font3)

        self.gridLayout_4.addWidget(self.SaveButton, 4, 2, 1, 1)

        self.logo_covid = QLabel(self.frame)
        self.logo_covid.setObjectName(u"logo_covid")

        self.gridLayout_4.addWidget(self.logo_covid, 0, 1, 1, 1)

        self.done_saved = QLabel(self.frame)
        self.done_saved.setObjectName(u"done_saved")

        self.gridLayout_4.addWidget(self.done_saved, 4, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 2, 1, 1)


        self.horizontalLayout.addWidget(self.frameDisplayImage)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1021, 21))
        self.menuMen = QMenu(self.menubar)
        self.menuMen.setObjectName(u"menuMen")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuModels = QMenu(self.menubar)
        self.menuModels.setObjectName(u"menuModels")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.pushload, self.pushButtonRun)

        self.menubar.addAction(self.menuMen.menuAction())
        self.menubar.addAction(self.menuModels.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuMen.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout_2)
        self.menuModels.addAction(self.actionVgg19)
        self.menuModels.addAction(self.actionDenseNet)
        self.menuModels.addAction(self.actionMobileNet)
        self.menuModels.addAction(self.actionAlexNet)
        self.menuModels.addAction(self.actionEfficientNet)
        self.menuModels.addAction(self.actionInceptionV3)
        self.menuModels.addAction(self.actionResNet_2)
        self.menuModels.addAction(self.actionRexNet)
        self.menuModels.addAction(self.actionInception_ResNet)
        self.menuModels.addAction(self.actionXception)

        self.retranslateUi(MainWindow)

        self.pushload.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionAbout_2.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionVgg19.setText(QCoreApplication.translate("MainWindow", u"Vgg19", None))
        self.actionDenseNet.setText(QCoreApplication.translate("MainWindow", u"DenseNet", None))
        self.actionMobileNet.setText(QCoreApplication.translate("MainWindow", u"MobileNet", None))
        self.actionAlexNet.setText(QCoreApplication.translate("MainWindow", u"AlexNet", None))
        self.actionEfficientNet.setText(QCoreApplication.translate("MainWindow", u"EfficientNet", None))
        self.actionInceptionV3.setText(QCoreApplication.translate("MainWindow", u"InceptionV3", None))
        self.actionResNet_2.setText(QCoreApplication.translate("MainWindow", u"ResNet", None))
        self.actionRexNet.setText(QCoreApplication.translate("MainWindow", u"RexNet", None))
        self.actionInception_ResNet.setText(QCoreApplication.translate("MainWindow", u"Inception-ResNet", None))
        self.actionXception.setText(QCoreApplication.translate("MainWindow", u"Xception", None))
        self.labelLogoFlir.setText("")
        self.labelLogo.setText("")
        self.label_5.setText("")
        self.done_run.setText("")
        self.pushButtonRun.setText(QCoreApplication.translate("MainWindow", u"     Run diagnosis     ", None))
        self.label_4.setText("")
        self.done_load.setText("")
        self.pushload.setText(QCoreApplication.translate("MainWindow", u"      Load Image      ", None))
        self.label_covid.setText(QCoreApplication.translate("MainWindow", u"COVID- RX", None))
        self.universidad.setText(QCoreApplication.translate("MainWindow", u"Universidad del Magdalena-Colombia", None))
        self.FinalPrediction.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"  Normal  ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"  Pneumonia", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"  Covid", None))
        self.SaveButton.setText(QCoreApplication.translate("MainWindow", u"     Save HeatMap     ", None))
        self.logo_covid.setText("")
        self.done_saved.setText("")
        self.menuMen.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.menuModels.setTitle(QCoreApplication.translate("MainWindow", u"Models", None))
    # retranslateUi

