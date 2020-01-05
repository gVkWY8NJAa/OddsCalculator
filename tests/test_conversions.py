from conversions import Conversions
from decimal import Decimal
import pytest


def test_us_to_dec():
    assert Conversions().us_to_dec("-606") == Decimal('1.165016501650165016501650165')
    assert Conversions().us_to_dec("475") == Decimal('5.75')
    assert Conversions().us_to_dec("-106") == Decimal('1.943396226415094339622641509')
    assert Conversions().us_to_dec("234") == Decimal('3.34')


def test_dec_to_us():
    assert Conversions().dec_to_us("1.5") == -200
    assert Conversions().dec_to_us("1.9091") == -110
    assert Conversions().dec_to_us("4.75") == 375
    assert Conversions().dec_to_us("1.9434") == -106
    assert Conversions().dec_to_us("2.34") == 134

def test_dec_to_frac():
    assert Conversions().dec_to_frac(Decimal('1.9091')) == '10/11'
    assert Conversions().dec_to_frac(Decimal('1.16501650')) == '50/303'
    assert Conversions().dec_to_frac(Decimal('2.34')) == '67/50'

def test_impliedPr():
    assert Conversions().implied_pr(426) == 0.1901140684410646387832699620
    assert Conversions().implied_pr(-110) == 0.52380952380952383595769106250372715294361114501953125

def test_noVig():
    assert Conversions().no_vig(Decimal('0.52'), Decimal('0.58')) == Decimal('0.4727272727272727272727272727')
    assert Conversions().no_vig(Decimal('.1739'), Decimal('0.5238')) == Decimal('0.2492475275906550093163250681')

def test_odds_type():
    assert Conversions().odds_type("-110") == "us"
    assert Conversions().odds_type("130") == "us"
    assert Conversions().odds_type("2.0") == "dec"
    assert Conversions().odds_type("21.033") == "dec"
    assert Conversions().odds_type("") == None