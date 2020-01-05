import sys
from decimal import Decimal
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel

# here we have to load the converted .ui file as a module
from ui_mainwindow import Ui_MainWindow
from conversions import Conversions


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__()

        # load template
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # call the slot based on the signal (clicked)
        self.ui.convert_button.clicked.connect(self.convert)

        # quit button
        self.ui.quitButton.clicked.connect(self.quit)

    def convert(self):
        oddsA, oddsB = False, False
        # load values from ui.odds
        if len(self.ui.oddsA.text()) != 0:
            oddsA = self.ui.oddsA.text()
            if Conversions().odds_type(oddsA) == "us":
                # Get decimal odds from US odds
                decOddsA = Conversions().us_to_dec(oddsA)

                # set usOdds
                usOddsA = int(oddsA)

            if Conversions().odds_type(oddsA) == "dec":
                # get us odds from dec
                usOddsA = Conversions().dec_to_us(oddsA)

                # set decOdds
                decOddsA = Decimal(oddsA)

            # Calculate net odds
            netDecOddsA = decOddsA - 1

            # Get implied probability from US odds
            impliedPrA = Conversions().implied_pr(usOddsA)

            # get fractional odds
            fracA = Conversions().dec_to_frac(decOddsA)

            self.ui.output_dec_odds_A.setText("{:.4f}".format(decOddsA))
            self.ui.output_net_dec_odds_A.setText("{:.4f}".format(netDecOddsA))
            self.ui.output_imp_pr_A.setText("{:.4f}".format(impliedPrA))
            self.ui.output_us_odds_A.setText(f"{usOddsA}")
            self.ui.output_frac_odds_A.setText(f"{fracA}")

        if len(self.ui.oddsB.text()) != 0:
            oddsB = self.ui.oddsB.text()
            if Conversions().odds_type(oddsB) == "us":
                # Get decimal odds from US odds
                decOddsB = Conversions().us_to_dec(oddsB)

                # set usOdds
                usOddsB = int(oddsB)

            if Conversions().odds_type(oddsB) == "dec":
                # get us odds from dec
                usOddsB = Conversions().dec_to_us(oddsB)

                # set decOdds
                decOddsB = Decimal(oddsB)

            # Calculate net odds
            netDecOddsB = decOddsB - 1

            # Get implied probability from US odds
            impliedPrB = Conversions().implied_pr(usOddsB)

            # get fractional odds
            fracB = Conversions().dec_to_frac(decOddsB)

            self.ui.output_dec_odds_B.setText("{:.4f}".format(decOddsB))
            self.ui.output_net_dec_odds_B.setText("{:.4f}".format(netDecOddsB))
            self.ui.output_imp_pr_B.setText("{:.4f}".format(impliedPrB))
            self.ui.output_us_odds_B.setText(f"{usOddsB}")
            self.ui.output_frac_odds_B.setText(f"{fracB}")

        else:
            oddsB = False

        if oddsA and oddsB:
            # NoVig is the ratio of 1 side to the sum of all sides
            noVigA = Conversions().no_vig(impliedPrA, impliedPrB)
            noVigB = Conversions().no_vig(impliedPrB, impliedPrA)

            # output to window
            self.ui.output_no_vig_A.setText("{:.4f}".format(noVigA))
            self.ui.output_no_vig_B.setText("{:.4f}".format(noVigB))

        if len(self.ui.input_betAmt_A.text()) != 0 and oddsA:
            betAmtA = self.ui.input_betAmt_A.text()
            self.ui.input_win_A.setText("${:.2f}".format(Decimal(betAmtA) * netDecOddsA))
            self.ui.input_payout_A.setText("${:.2f}".format(Decimal(betAmtA) * decOddsA))

        if len(self.ui.input_betAmt_B.text()) != 0 and oddsB:
            betAmtB = self.ui.input_betAmt_B.text()
            self.ui.input_win_B.setText("${:.2f}".format(Decimal(betAmtB) * netDecOddsB))
            self.ui.input_payout_B.setText("${:.2f}".format(Decimal(betAmtB) * decOddsB))

    def quit(self):
        sys.exit(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
