# Tuple Out Dice Game

## Overview
This is a simple dice game written in Python called "Tuple Out." The objective is to score the most points without rolling three of the same number, which is called "tupling out."

## Rules
1. Players roll three dice.
2. If all three dice show the same number, the player "tuples out" and scores 0 points.
3. If two dice show the same value, they are fixed, and only the third dice can be rerolled.
4. Players can reroll any unfixed dice as many times as they want until they decide to stop or tuple out.
5. The score is the sum of the dice values when the player stops rolling.

## Features
- Roll three dice.
- Option to keep specific dice and reroll others.
- Prevents players from rerolling fixed dice.
- Calculates the final score.

## How to Run
1. Make sure you have Python installed on your computer.
2. Open a terminal in the project folder.
3. Run the following command:
   ```bash
   python tuple_out.py
