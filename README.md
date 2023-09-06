# Mouse Jiggler

Mouse Jiggler is a Python script that jiggles the mouse cursor at a specified interval. It is useful for preventing screen lock, sleep, or idle actions when you are away from your computer.

## Prerequisites

- Python 3.x
- pyautogui library

## Installation

1. Install the required dependencies:

```
pip install pyautogui
```

## Usage

1. Open a terminal or command prompt and navigate to the cloned repository folder.

2. Run the `mousejiggler.py` script with the desired interval:

```
python mousejiggler.py -t <interval>
```

- Replace `<interval>` with the desired interval in seconds. By default, the interval is set to 45 seconds.

3. The script will start jiggling the mouse cursor. Move the cursor manually to stop the jiggling temporarily.

4. Press `Ctrl+C` to stop the script and exit.

## Acknowledgements

- [pyautogui](https://github.com/asweigart/pyautogui) - The `pyautogui` library used for mouse jiggling.
```
