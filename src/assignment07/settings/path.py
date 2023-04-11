from pathlib import Path
import os

filename = "/../../../resources/booking_quotes.csv"
csv_path = Path(os.path.dirname(os.path.abspath(__file__)) + filename)
