import mss
import datetime
import os

def take_screenshot(file_name_prefix, directory="screenshots"):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{file_name_prefix}_{timestamp}.png"
    file_path = os.path.join(directory, file_name)

    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    try:
        # Take screenshot and save it
        with mss.mss() as sct:
            screenshot = sct.shot(output=file_path)
        print(f"Screenshot saved as {file_path}")
    except Exception as e:
        print(f"Failed to take screenshot: {e}")

    return file_path

# Ensure that the screenshots directory is created when the script runs
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")
