# Calculator
## Project Requirement for CCC 

- **Written with Python 3.9 (Can work with 3.7.9)**
- **Uses PyQt6 as the GUI Framework**
- **Uses Pyparsing for the calculator logic**

### This project has the following features.

**Calculator Logic**:

- Numeric keypad (0-9) with decimal point
- Can perform `addition` (+) , `subtraction` (-), `multiplication` (x), and `division` (%)
- Can perform trigonometric operations (`sine`, `cosine`, `tangent`, `inverses`, `hyperbolic`)
- Can perform `logarithmic` and `exponential` operations
- Can perform other algebraic operations (`square root`, `cube root`, `scientific notations`, etc.)
- Capable of chaining multiple operations together (with or without parentheses) and it execute them in the correct order
- Can perform `round`, `truncate`, `modular`, and `absolute functions`
- Other necessary functions: `delete`, `clear all`, `ANS`, etc.

**UI**:

- Can switch between the basic calculator layout to the scientific calculator layout.
- A button press effect, which can be changed or disabled.
- A subtle background music.
- A date and time widget in the status bar.
- A status bar that shows tips on how to use certain functions.
- An Instructions window that shows general instructions on how to use our calculator.
- An About window that has a link for our GitHub repository and presentation video (to be updated as we finish it)

_And some extra little adjustment to the UI, the windows are non-resizable so that the layout is preserved. By extension, the calculator can't be maximized._

# How to Set Up

1. Clone or download the repository.
2. Install the necessary dependencies:
```
pip install -r requirements.txt
```
3. Run the program:
```
python main.py
```
4. Make sure all the `.py` files are located in the same folder. 
5. Make sure the `resources` folder is also within the same directory, as the UI uses files that are in this folder.

### Calculator logic is located in `calculator.py`
### UI code is located in `ui.py`
### You can initiate some tests for the calculator logic with `test.py`

# Team

Team Leader: Ralph Christian Palmaira // JARalph23Z

Team Members: 
- Brixson Domantay // brxzn
- Ray Dalipe // Torurae
- Hans Tulayan // Meriodasu007
- Saile Galilea // Kkaepsong

# Disclaimer
```
All the codes within this repository are either self-made or adapted from other repositories under the MIT License, which allows for the distribution and alteration of such codes. If you wish, you can open an issue so we can address any problems immediately. Thank you for your understanding.
```
