# EPL-Shots-Heatmap

I have created a simple script for getting shot data from Understat and creating a visual of the top 10 players with the most shots.

I made a simple Gui interface using Tkinter to help generate these visualizations.

<img src='./fodenAllShots.png' height='700' width='400'>

## Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/D-Walsh33/EPL-Shots-Heatmap
```

---

### 2. Create and activate a virtual environment

```bash
# Create the virtual environment (only once)
python -m venv venv

# Activate the virtual environment (Windows Bash)
source venv/Scripts/activate
```

> When activated, your prompt should show `(venv)` at the beginning.

---

### 3. Install dependencies

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

- This installs all required libraries listed in `requirements.txt`, including `understat` and any others your project uses.

---

### 4. Run your scripts

```bash
python main.py
```

---

### 4. Update Data

```bash
python getData.py
```

- In getData.py you can change which year or years you would like to get data for.
- If you add new files to the data folder, Edit main.py to reflect the new files.

---

### 5. Deactivate the virtual environment

```bash
deactivate
```

- Returns your shell to the system Python.

---

## Optional Development Tips

- Always activate the venv before working on the project.
- Update dependencies in `requirements.txt` whenever you install new packages:

```bash
pip freeze > requirements.txt
```

- Quick venv activation using a Bash alias:

```bash
alias activate_myproject='source ~/my_project/venv/Scripts/activate'
```

- Keep your venv out of Git using `.gitignore`.

---

## Notes

- This setup works for Windows Bash, Linux, and macOS with minor path adjustments.
- Ensure Python 3.11 is used for compatibility with `understat`.
-
