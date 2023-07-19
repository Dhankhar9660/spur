import os
import time
import pytest

# Run the test case and generate the report
folder_path = "C:/Users/Bal/PycharmProjects/Spurowebest/Reports/"
timestamp = str(int(time.time()))

# Create a unique file name using the  timestamp
file_name = f"{timestamp}.html"
file_path = os.path.join(folder_path, file_name)
# Specify the directory path to save the report
directory = "C:/Users/Bal/PycharmProjects/Spurowebest/Screenshot/"

# Create the full path by joining the directory path and file name
screenshot_path = os.path.join(directory, file_name)
# Run the test case with the specified marker
pytest.main(["--html=" + file_path, "-m login"])
