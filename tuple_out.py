import random
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import time
import os

# Function to roll dice
def roll_dice():
    return (random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))

# Function to display dice rolls
def display_dice(dice):
    print(f"Your dice: {dice}")

# Function to check if all dice show the same number (tuple out)
def is_tuple_out(dice):
    return dice[0] == dice[1] == dice[2]

# Function to calculate the score
def calculate_score(dice):
    return sum(dice)

# Function to reroll dice based on player's choice
def reroll_dice(dice, keep):
    new_dice = [dice[i] if i in keep else random.randint(1, 6) for i in range(3)]
    return tuple(new_dice)

# Function to log game results
def log_results(dice, score, tuple_out):
    try:
        # Check if the file exists and write header if it's the first time
        file_exists = os.path.isfile("game_results.csv")
        with open("game_results.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Dice", "Score", "Tuple Out", "Timestamp"])  # Write header if file doesn't exist
            writer.writerow([dice, score, tuple_out, time.strftime("%Y-%m-%d %H:%M:%S")])
    except OSError as e:
        print(f"Error logging results: {e}")

# Function to analyze game history
def analyze_history():
    try:
        data = pd.read_csv("game_results.csv", names=["Dice", "Score", "Tuple Out", "Timestamp"], header=0)
        print("\n--- Game History Analysis ---")
        print(f"Total games played: {len(data)}")
        print(f"Average score: {data['Score'].mean():.2f}")
        print(f"Games with Tuple Out: {data['Tuple Out'].sum()}")

        sns.set(style="whitegrid")
        plt.figure(figsize=(8, 5))
        sns.histplot(data['Score'], bins=10, kde=True)
        plt.title("Score Distribution")
        plt.xlabel("Score")
        plt.ylabel("Frequency")
        plt.show()
    except FileNotFoundError:
        print("No game history found. Play a game first.")
    except pd.errors.EmptyDataError:
        print("Game history file is empty. Play a game first.")
    except OSError as e:
        print(f"Error analyzing history: {e}")

# Main menu function
def main():
    print("Welcome to Tuple Out Dice Game!")
    print("The goal is to get the highest score without rolling three of the same number (tuple out).\n")

    while True:
        print("\n--- Main Menu ---")
        print("1. Play a game")
        print("2. Analyze game history")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")
        if choice == "1":
            dice = roll_dice()
            display_dice(dice)

            if is_tuple_out(dice):
                print("Oh no! You tupled out! Game over.")
                log_results(dice, 0, True)
                continue

            keep = input("Enter the positions of the dice you want to keep (0, 1, 2) separated by spaces, or press Enter to reroll all: ")
            if keep.strip():
                try:
                    keep = list(map(int, keep.split()))
                    if not all(0 <= k <= 2 for k in keep):
                        raise ValueError("Positions must be 0, 1, or 2.")
                except ValueError as e:
                    print(f"Invalid input: {e}. Keeping no dice.")
                    keep = []
            else:
                keep = []

            dice = reroll_dice(dice, keep)
            display_dice(dice)

            if is_tuple_out(dice):
                print("Oh no! You tupled out on the reroll! Game over.")
                log_results(dice, 0, True)
                continue

            score = calculate_score(dice)
            print(f"Your final score is: {score}")
            log_results(dice, score, False)

        elif choice == "2":
            analyze_history()
        elif choice == "3":
            print("Goodbye! Thanks for playing Tuple Out Dice Game!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        main()
    except OSError as e:
        print(f"Critical error encountered: {e}. Exiting the game.")




