import time
import argparse
import pyautogui

def is_mouse_active():
    pointer = pyautogui.position()
    time.sleep(0.1)
    return pointer != pyautogui.position()

def jiggle_mouse(duration, interval):
    i = 0
    while True:
        if not is_mouse_active():
            print(f"Jiggling mouse {i+1}")
            pyautogui.move(1, 1, duration=duration)
            pyautogui.move(-1, -1, duration=duration)
            i += 1
        
        time.sleep(interval)

def main():
    parser = argparse.ArgumentParser(description="Jiggle the mouse cursor at a specified interval.")
    parser.add_argument("-t", "--interval", type=int, default=45, help="Interval between mouse jiggles in seconds. Default is 45.")
    args = parser.parse_args()

    interval = args.interval
    jiggle_mouse(1, interval)

if __name__ == "__main__":
    main()
