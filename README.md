[![Build Status](https://travis-ci.org/gVkWY8NJAa/OddsCalculator.svg?branch=master)](https://travis-ci.org/gVkWY8NJAa/OddsCalculator) [![Coverage Status](https://coveralls.io/repos/github/gVkWY8NJAa/OddsCalculator/badge.svg?branch=master)](https://coveralls.io/github/gVkWY8NJAa/OddsCalculator?branch=master)
# OddsCalculator

This is a Qt based betting odds converter built in Qt with PySide2 for Python. It is a fun little project to learn Qt 
on Python. 

## Contents
* [Installation](#installation)

## Key Features
* Seamlessly enter odds in US or Decimal format, they will be automatically converted.
* Calculate implied, and no vig, probabilities of winning based on two bets.
* Net and total winnings displayed given a bet amount.

## Installation
```python
python3 -m venv </path/to/new/virtual/environment>
source <venv>/bin/activate
pip install -r requirements.txt 
python oddsCalculator.py
```