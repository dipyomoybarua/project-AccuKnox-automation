import pyautogui
import datetime
import os

def take_screenshot(file_name_prefix):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{file_name_prefix}_{timestamp}.png"
    file_path = os.path.join("screenshots", file_name)

    # Create screenshots directory if it doesn't exist
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    # Take screenshot and save it
    screenshot = pyautogui.screenshot()
    screenshot.save(file_path)
    print(f"Screenshot saved as {file_path}")
