from fractions import Fraction
import re


class Conversions:
    def __init__(self, *args, **kwagrs):
        pass

    def us_to_dec(self, value: str) -> float:
        """
        Convert US odds to float
        Args:
            value (str): US odds ie -600, 475
        Returns:
            float: converted us odds in decimal format
        """
        valueAsDec = float(value)
        if valueAsDec > 0:
            return (valueAsDec / 100) + 1
        elif valueAsDec < 0:
            return 100 / abs(valueAsDec) + 1
        else:
            return 0

    def frac_to_dec(self, value: str) -> float:
        """
        Convert fractional odds to decimal odds
        Args:
            value (str): fractional odds ie 4:1 or 4/1
        Returns:
             float converted fractional odds in decimal format
        """
        if ':' in value:
            f, a = int(value.split(':')[0]), int(value.split(':')[1])
            return (f/a)+1
        if '/' in value:
            f, a = int(value.split('/')[0]), int(value.split('/')[1])
            return (f/a)+1
        else:
            return 0

    def dec_to_us(self, value: str) -> int:
        """
        Convert decimal odds to US
        Args:
            value (str): decimal odds in string format
        Returns:
             int: converted us odds in int format
        """
        valueAsDec = float(value)
        if valueAsDec >= 2.0:
            return int((valueAsDec - 1) * 100)
        elif valueAsDec < 2.0:
            return int(round(-100 / (valueAsDec - 1), 0))

    def dec_to_frac(self, value: float) -> str:
        """
        Convert decimal odds to fractional odds
        Args:
            value (decimal): odds in decimal.float() format
        """
        net = value - 1
        return str(Fraction(net).limit_denominator(1000))

    def implied_pr(self, value: int) -> float:
        """
        Calculates implied probability given US odds
        Args:
            value (int): 400
        Returns:
            float: implied probability
        """
        if value > 0:
            return 100 / (100 + value)
        elif value < 0:
            return abs(value) / (abs(value) + 100)
        else:
            return 0

    def no_vig(self, value1: float, value2: float) -> float:
        """
        Calculates the implied no vig probability given implied probabilities for two bets
        Args:
            value1 (float): implied probability for the side you want to find the adjusted no vig Pr for
            value2 (float): implied probability of the other side of the bet
        Returns:
            float: No vig implied probability for value1
        """
        return value1 / (value1 + value2)

    def odds_type(self, value: str) -> str:
        """
        Figure out if an input string is in US or decimal format
        Args:
            value (str): -110, 2.0 as strings
        Returns:
             string: "dec, us"
        """
        if re.match(r"[0-9]{1,4}\.[0-9]{1,4}", value):
            return "dec"
        elif re.match(r"(^\d{3}|^-\d{3})", value):
            return "us"
        elif re.match(r"[0-9]{1,4}(\:|\/)[0-9]{1,4}", value):
            return 'frac'
        else:
            return None

    def expected_value(self, decOdds: float, implied_pr: float) -> float:
        """
        calculate expected value based on implied probability
        Args:
            decOdds (float): Decimal odds of the wager
            implied_pr (float): implied pr in decimal formal
        Returns:
            ev (float): expected value (net odds * pr_win) + (pr_lose * wager)
        """
        return (decOdds * implied_pr) + ((1 - implied_pr) * -1)
