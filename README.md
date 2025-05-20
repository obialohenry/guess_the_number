# guess_the_number

A simple, interactive command-line game written in Python where players try to guess a randomly generated number between 1 and 100.

## 🎮 Game Overview

In this game:
- The computer randomly selects a number between 1 and 100
- Players choose a difficulty level (easy or hard)
- Easy mode gives 10 attempts to guess the correct number
- Hard mode gives 5 attempts to guess the correct number
- After each guess, the game provides feedback (too high, too low, or correct)
- Players win by guessing the correct number before running out of attempts

## ✨ Features

- Two difficulty levels
- Feedback after each guess
- Proper grammar handling for singular/plural attempts
- ASCII art logo for enhanced user experience

## 🔧 Requirements

- Python 3.6 or higher
- `art` package for ASCII art

## 📥 Installation

1. Make sure Python is installed on your system
2. Install the required package using pip:
   ```
   pip install art
   ```
3. Download the game file

## 🚀 How to Run

Run the game from your terminal/command prompt:

```
python main.py
```

## 🎯 How to Play

1. When the game starts, you'll see a welcome message and the logo
2. Choose your difficulty level by typing 'easy' or 'hard'
3. The game will tell you how many attempts you have
4. Enter your guess when prompted
5. The game will tell you if your guess is too high or too low
6. Keep guessing until you find the correct number or run out of attempts
7. If you guess correctly, you win!
8. If you run out of attempts, you lose

## 📝 Code Structure

- `attempt_word_form()` - Handles grammar for singular/plural attempts
- `feedback()` - Provides feedback based on the player's guess
- `easy_or_hard_level()` - Manages game logic based on difficulty level
- `guess_the_number()` - Main game function that orchestrates the gameplay

## 🛠️ Future Improvements

- Add a score tracking system
- Implement a hints mechanism
- Allow custom number ranges
- Add a replay option

## 📄 License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## 👨‍💻 Author

[Obialor Chisomebi Henry]
