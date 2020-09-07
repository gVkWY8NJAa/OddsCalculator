from conversions import Conversions
import pytest

def test_frac_to_dec():
    assert Conversions().frac_to_dec("4:1") == 5.0
    assert Conversions().frac_to_dec("4/1") == 5.0
    assert Conversions().frac_to_dec("1:4") == 1.25
    assert Conversions().frac_to_dec("1/4") == 1.25

def test_us_to_dec():
    assert Conversions().us_to_dec("-606") == 1.165016501650165016501650165
    assert Conversions().us_to_dec("475") == 5.75
    assert Conversions().us_to_dec("-106") == 1.943396226415094339622641509
    assert Conversions().us_to_dec("234") == 3.34


def test_dec_to_us():
    assert Conversions().dec_to_us("1.5") == -200
    assert Conversions().dec_to_us("1.9091") == -110
    assert Conversions().dec_to_us("4.75") == 375
    assert Conversions().dec_to_us("1.9434") == -106
    assert Conversions().dec_to_us("2.34") == 134


def test_dec_to_frac():
    assert Conversions().dec_to_frac(1.9091) == "10/11"
    assert Conversions().dec_to_frac(1.16501650) == "50/303"
    assert Conversions().dec_to_frac(2.34) == "67/50"


def test_impliedPr():
    assert Conversions().implied_pr(426) == 0.1901140684410646387832699620
    assert (
        Conversions().implied_pr(-110)
        == 0.52380952380952383595769106250372715294361114501953125
    )


def test_noVig():
    assert Conversions().no_vig(0.52, 0.58) == (0.4727272727272727272727272727)
    assert Conversions().no_vig(0.1739, 0.5238) == (0.2492475275906550093163250681)


def test_odds_type():
    assert Conversions().odds_type("-110") == "us"
    assert Conversions().odds_type("130") == "us"
    assert Conversions().odds_type("2.0") == "dec"
    assert Conversions().odds_type("21.033") == "dec"
    assert Conversions().odds_type("") == None


def test_expected_value():
    assert Conversions().expected_value(2.0, 0.57) == 0.7099999999999999
    assert Conversions().expected_value(3.0, 0.34) == 0.3600000000000001
