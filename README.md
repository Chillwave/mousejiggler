# Mouse Jiggler

Mouse Jiggler is a Python script that jiggles the mouse cursor at a specified interval. It is useful for preventing screen lock, sleep, or idle actions when you are away from your computer.

## Prerequisites

- Python 3.x
- pyautogui library

## Installation

1. Clone the repository:

```
git clone https://github.com/your-username/mouse-jiggler.git
```

2. Install the required dependencies:

```
pip install pyautogui
```

## Usage

1. Open a terminal or command prompt and navigate to the cloned repository folder.

2. Run the `mouse_jiggler.py` script with the desired interval:

```
python mouse_jiggler.py -t <interval>
```

- Replace `<interval>` with the desired interval in seconds. By default, the interval is set to 45 seconds.

3. The script will start jiggling the mouse cursor. Move the cursor manually to stop the jiggling temporarily.

4. Press `Ctrl+C` to stop the script and exit.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [pyautogui](https://github.com/asweigart/pyautogui) - The `pyautogui` library used for mouse jiggling.
```
