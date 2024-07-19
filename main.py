import time

import pyautogui
import pygetwindow as gw


class WindowControlUtil:

    def __init__(self, window_title):
        self.window_title = window_title
        self.target_window = None

    def focus_window(self):
        """
        Focuses on the window based on the given title.
        """
        window_titles = gw.getAllTitles()

        for title in window_titles:
            if self.window_title in title:
                self.target_window = gw.getWindowsWithTitle(title)[0]
                break

        if not self.target_window:
            print(f"{self.window_title} window not found.")
            return False

        self.target_window.activate()
        return True

    def capture_window(self, display=True):
        """
        Captures the screenshot of the window and returns it as an image.

        Args:
        display (bool): Whether to display the captured image.

        Returns:
        PIL.Image.Image: The captured image.
        """
        if not self.target_window:
            print("Target window is not focused.")
            return None

        left, top, right, bottom = (
            self.target_window.left,
            self.target_window.top,
            self.target_window.right,
            self.target_window.bottom,
        )

        screenshot = pyautogui.screenshot(
            region=(left, top, right - left, bottom - top)
        )

        if display:
            screenshot.show()

        return screenshot

    def press_keys(self, keys, duration=0.1):
        """
        Press a single key or multiple keys for a specific duration.

        Args:
        keys (str or list of str): The key(s) to press.
        duration (float): The duration to hold the key(s) down.
        """
        if isinstance(keys, str):
            keys = [keys]

        for key in keys:
            pyautogui.keyDown(key)

        time.sleep(duration)

        for key in keys:
            pyautogui.keyUp(key)
