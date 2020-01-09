# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(300, 382)
        MainWindow.setMinimumSize(QSize(300, 228))
        MainWindow.setMaximumSize(QSize(300, 382))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(-1, -1, -1, 9)
        self.input_win_B = QLineEdit(self.centralwidget)
        self.input_win_B.setObjectName(u"input_win_B")
        self.input_win_B.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.input_win_B, 13, 2, 1, 1)

        self.output_net_dec_odds_B = QLabel(self.centralwidget)
        self.output_net_dec_odds_B.setObjectName(u"output_net_dec_odds_B")
        font = QFont()
        font.setItalic(True)
        self.output_net_dec_odds_B.setFont(font)
        self.output_net_dec_odds_B.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.output_net_dec_odds_B, 8, 2, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 12, 0, 1, 1)

        self.output_no_vig_A = QLabel(self.centralwidget)
        self.output_no_vig_A.setObjectName(u"output_no_vig_A")
        self.output_no_vig_A.setFont(font)
        self.output_no_vig_A.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.output_no_vig_A, 10, 1, 1, 1)

        self.input_betAmt_A = QLineEdit(self.centralwidget)
        self.input_betAmt_A.setObjectName(u"input_betAmt_A")
        self.input_betAmt_A.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.input_betAmt_A, 12, 1, 1, 1)

        self.output_no_vig_B = QLabel(self.centralwidget)
        self.output_no_vig_B.setObjectName(u"output_no_vig_B")
        self.output_no_vig_B.setFont(font)
        self.output_no_vig_B.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.output_no_vig_B, 10, 2, 1, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 1, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 14, 0, 1, 1)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 1, 2, 1, 1)

        self.output_frac_odds_B = QLabel(self.centralwidget)
        self.output_frac_odds_B.setObjectName(u"output_frac_odds_B")
        self.output_frac_odds_B.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.output_frac_odds_B, 6, 2, 1, 1)

        self.output_imp_pr_B = QLabel(self.centralwidget)
        self.output_imp_pr_B.setObjectName(u"output_imp_pr_B")
        self.output_imp_pr_B.setFont(font)
        self.output_imp_pr_B.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.output_imp_pr_B, 9, 2, 1, 1)

        self.input_payout_A = QLineEdit(self.centralwidget)
        self.input_payout_A.setObjectName(u"input_payout_A")
        self.input_payout_A.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.input_payout_A, 14, 1, 1, 1)

        self.input_win_A = QLineEdit(self.centralwidget)
        self.input_win_A.setObjectName(u"input_win_A")
        self.input_win_A.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.input_win_A, 13, 1, 1, 1)

        self.oddsA = QLineEdit(self.centralwidget)
        self.oddsA.setObjectName(u"oddsA")
        self.oddsA.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.oddsA, 2, 1, 1, 1)

        self.quitButton = QPushButton(self.centralwidget)
        self.quitButton.setObjectName(u"quitButton")
        self.quitButton.setMinimumSize(QSize(0, 28))
        font1 = QFont()
        font1.setBold(False)
        font1.setWeight(50);
        self.quitButton.setFont(font1)
        self.quitButton.setAutoDefault(False)
        self.quitButton.setFlat(False)

        self.gridLayout.addWidget(self.quitButton, 15, 0, 1, 1)

        self.input_payout_B = QLineEdit(self.centralwidget)
        self.input_payout_B.setObjectName(u"input_payout_B")
        self.input_payout_B.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.input_payout_B, 14, 2, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 13, 0, 1, 1)

        self.output_dec_odds_A = QLabel(self.centralwidget)
        self.output_dec_odds_A.setObjectName(u"output_dec_odds_A")
        self.output_dec_odds_A.setFont(font)
        self.output_dec_odds_A.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.output_dec_odds_A, 5, 1, 1, 1)

        self.input_betAmt_B = QLineEdit(self.centralwidget)
        self.input_betAmt_B.setObjectName(u"input_betAmt_B")
        self.input_betAmt_B.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.input_betAmt_B, 12, 2, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75);
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label_Frac_odds = QLabel(self.centralwidget)
        self.label_Frac_odds.setObjectName(u"label_Frac_odds")

        self.gridLayout.addWidget(self.label_Frac_odds, 6, 0, 1, 1)

        self.label_USOdds = QLabel(self.centralwidget)
        self.label_USOdds.setObjectName(u"label_USOdds")

        self.gridLayout.addWidget(self.label_USOdds, 4, 0, 1, 1)

        self.output_us_odds_B = QLabel(self.centralwidget)
        self.output_us_odds_B.setObjectName(u"output_us_odds_B")
        self.output_us_odds_B.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.output_us_odds_B, 4, 2, 1, 1)

        self.label_ImpliedPr = QLabel(self.centralwidget)
        self.label_ImpliedPr.setObjectName(u"label_ImpliedPr")

        self.gridLayout.addWidget(self.label_ImpliedPr, 9, 0, 1, 1)

        self.output_frac_odds_A = QLabel(self.centralwidget)
        self.output_frac_odds_A.setObjectName(u"output_frac_odds_A")
        self.output_frac_odds_A.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.output_frac_odds_A, 6, 1, 1, 1)

        self.label_DecOdds = QLabel(self.centralwidget)
        self.label_DecOdds.setObjectName(u"label_DecOdds")

        self.gridLayout.addWidget(self.label_DecOdds, 5, 0, 1, 1)

        self.label_Odds_1 = QLabel(self.centralwidget)
        self.label_Odds_1.setObjectName(u"label_Odds_1")
        self.label_Odds_1.setFont(font2)
        self.label_Odds_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_Odds_1, 0, 1, 1, 1)

        self.output_net_dec_odds_A = QLabel(self.centralwidget)
        self.output_net_dec_odds_A.setObjectName(u"output_net_dec_odds_A")
        self.output_net_dec_odds_A.setFont(font)
        self.output_net_dec_odds_A.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.output_net_dec_odds_A, 8, 1, 1, 1)

        self.output_us_odds_A = QLabel(self.centralwidget)
        self.output_us_odds_A.setObjectName(u"output_us_odds_A")
        self.output_us_odds_A.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.output_us_odds_A, 4, 1, 1, 1)

        self.output_imp_pr_A = QLabel(self.centralwidget)
        self.output_imp_pr_A.setObjectName(u"output_imp_pr_A")
        self.output_imp_pr_A.setFont(font)
        self.output_imp_pr_A.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.output_imp_pr_A, 9, 1, 1, 1)

        self.convert_button = QPushButton(self.centralwidget)
        self.convert_button.setObjectName(u"convert_button")
        self.convert_button.setMinimumSize(QSize(0, 28))
        self.convert_button.setFont(font2)
        self.convert_button.setAutoDefault(True)

        self.gridLayout.addWidget(self.convert_button, 15, 1, 1, 2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 2, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFont(font1)
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 3)

        self.output_dec_odds_B = QLabel(self.centralwidget)
        self.output_dec_odds_B.setObjectName(u"output_dec_odds_B")
        self.output_dec_odds_B.setFont(font)
        self.output_dec_odds_B.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.output_dec_odds_B, 5, 2, 1, 1)

        self.label_No_Vig = QLabel(self.centralwidget)
        self.label_No_Vig.setObjectName(u"label_No_Vig")

        self.gridLayout.addWidget(self.label_No_Vig, 10, 0, 1, 1)

        self.label_NetOdds = QLabel(self.centralwidget)
        self.label_NetOdds.setObjectName(u"label_NetOdds")

        self.gridLayout.addWidget(self.label_NetOdds, 8, 0, 1, 1)

        self.oddsB = QLineEdit(self.centralwidget)
        self.oddsB.setObjectName(u"oddsB")
        self.oddsB.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.oddsB, 2, 2, 1, 1)

        self.label_EV = QLabel(self.centralwidget)
        self.label_EV.setObjectName(u"label_EV")

        self.gridLayout.addWidget(self.label_EV, 11, 0, 1, 1)

        self.output_ev_A = QLabel(self.centralwidget)
        self.output_ev_A.setObjectName(u"output_ev_A")
        self.output_ev_A.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.output_ev_A, 11, 1, 1, 1)

        self.output_ev_B = QLabel(self.centralwidget)
        self.output_ev_B.setObjectName(u"output_ev_B")
        self.output_ev_B.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.output_ev_B, 11, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.convert_button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Odds Converter", None))
        self.input_win_B.setText("")
        self.output_net_dec_odds_B.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Bet Amount ($)", None))
        self.output_no_vig_A.setText("")
        self.input_betAmt_A.setText("")
        self.output_no_vig_B.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Payout ($)", None))
        self.output_frac_odds_B.setText("")
        self.output_imp_pr_B.setText("")
        self.input_payout_A.setText("")
        self.input_win_A.setText("")
        self.quitButton.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.input_payout_B.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"To Win ($)", None))
        self.output_dec_odds_A.setText("")
        self.input_betAmt_B.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Enter Odds:", None))
        self.label_Frac_odds.setText(QCoreApplication.translate("MainWindow", u"Fractional Odds", None))
        self.label_USOdds.setText(QCoreApplication.translate("MainWindow", u"US Odds", None))
        self.output_us_odds_B.setText("")
        self.label_ImpliedPr.setText(QCoreApplication.translate("MainWindow", u"Implied Pr", None))
        self.output_frac_odds_A.setText("")
        self.label_DecOdds.setText(QCoreApplication.translate("MainWindow", u"Decimal Odds", None))
        self.label_Odds_1.setText(QCoreApplication.translate("MainWindow", u"Team A", None))
        self.output_net_dec_odds_A.setText("")
        self.output_us_odds_A.setText("")
        self.output_imp_pr_A.setText("")
        self.convert_button.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Team B", None))
        self.output_dec_odds_B.setText("")
        self.label_No_Vig.setText(QCoreApplication.translate("MainWindow", u"No Vig Imp Pr", None))
        self.label_NetOdds.setText(QCoreApplication.translate("MainWindow", u"Net Odds", None))
        self.label_EV.setText(QCoreApplication.translate("MainWindow", u"Expected Value", None))
        self.output_ev_A.setText("")
        self.output_ev_B.setText("")
    # retranslateUi

