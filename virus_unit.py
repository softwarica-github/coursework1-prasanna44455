import unittest
import tkinter as tk
from tkinter import messagebox
from unittest.mock import patch

import virus_scanner

class TestVirusScanner(unittest.TestCase):

    @patch('virus_scanner.filedialog.askopenfilename', return_value='/path/to/file.exe')
    def test_scan_file(self, mock_askopenfilename):
        # Create the main window
        window = tk.Tk()
        window.title("Antivirus Scanner")
        window.geometry("500x300")

        # Create label to display the scan result
        result_label = tk.Label(window, text="", font=("Arial", 18))