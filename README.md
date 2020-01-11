[![Build Status](https://travis-ci.org/gVkWY8NJAa/OddsCalculator.svg?branch=master)](https://travis-ci.org/gVkWY8NJAa/OddsCalculator) [![Coverage Status](https://coveralls.io/repos/github/gVkWY8NJAa/OddsCalculator/badge.svg?branch=master)](https://coveralls.io/github/gVkWY8NJAa/OddsCalculator?branch=master)
# OddsCalculator

This is a Qt based betting odds converter built in Qt with PySide2 for Python. It is a fun little project to learn Qt 
on Python. 

![alt text](https://github.com/gVkWY8NJAa/OddsCalculator/raw/dev/images/usOdds.png "US An decimal odds can be entered seamlessly.")
![alt text](https://github.com/gVkWY8NJAa/OddsCalculator/raw/dev/images/decOdds.png "US An decimal odds can be entered seamlessly.")


## Contents
* [Key Features](#key features)
* [Installation](#installation)

## Key Features
* Seamlessly enter odds in US or Decimal format, they will be automatically converted.
* Calculate implied, and no vig, probabilities of winning based on two bets.
* Net and total winnings displayed given a bet amount.
* Expected value calculation based on given odds

## Installation
```
python3 -m venv </path/to/new/virtual/environment>
source </path/to/new/venv>/bin/activate
cd </path/to/new/venv> && git clone https://github.com/gVkWY8NJAa/OddsCalculator.git
cd OddsCalculator && pip install -r requirements.txt 
python oddsCalculator.py
```