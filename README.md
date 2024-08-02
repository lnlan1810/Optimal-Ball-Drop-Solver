# Optimal Ball Drop Solver

## Overview

**Optimal Ball Drop Solver** is a Python tool designed to determine the minimum number of throws required to find the highest floor from which a ball will break when dropped. The solution uses an optimized strategy based on binary search principles to efficiently solve the ball drop problem with a given number of balls and floors.

## Features

- Calculates the minimum number of throws required to find the critical floor.
- Optimizes the number of balls used by discarding any extras beyond what's needed for the binary search.
- Provides interactive simulation for determining the critical floor.

## How It Works

1. **Input:** The user provides the number of floors (`n`) and balls (`k`).
2. **Optimization:** The tool adjusts the number of balls if the provided number exceeds what is necessary for the binary search.
3. **Simulation:** The program simulates the process of dropping balls from various floors and adjusting the search range based on user feedback.
4. **Output:** The tool outputs the critical floor where the ball starts to break.

## Usage

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/lnlan1810/Optimal-Ball-Drop-Solver.git
   ```

2. **Input the Number of Floors and Balls:**
   
   When prompted, enter the number of floors and balls separated by a space.

   Example:
   ```
   Input: number of floors and number of balls: 10 3
   ```

3. **Provide Responses:**

   As the simulation proceeds, you'll be prompted to provide responses based on whether the ball broke or not. Use "Broken" or "Not Broken" as responses.

## Requirements

- Python 3.x

## Contributing

Feel free to submit issues or pull requests. Contributions are welcome!
