# EPL-Shots-Heatmap

This is a small project to better understand using tkinter to create a GUI for python.
When this project is completed the user will be able to create nice graphs to visualize Premier League shots.

<img src='./fodenAllShots.png' height='700' width='400'>

I have created a simple GUI for the user to select which year they would like to look at and they can cycle through the top 10 players:

<img src='updatedGUI.gif'>

# My Project

A brief description of your project goes here.

---

## Setup & Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd my_project
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
python src/main.py
```

- Replace `src/main.py` with the path to your main script.

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
