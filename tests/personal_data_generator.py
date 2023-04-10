import pandas as pd
import os, csv
from pathlib import Path
from faker import Faker
from datetime import datetime

fake = Faker()

df = pd.DataFrame(
    [
        {
            "booking_id" : fake.unique.random_int(min=1, max=999),
            "customer_name" : fake.name(),
            "destination_country" : "United States of America" if fake.boolean(chance_of_getting_true = 50) else fake.country(),
            "package_description" : fake.sentence(nb_words=8),
            "weight" : round(fake.pyfloat(min_value=0, max_value=10),2),
            "volume" : round(fake.pyfloat(min_value=0, max_value=125),2),
            "required_delivery_date" : datetime.strftime(fake.date_this_year(before_today = True, after_today = False), '%m/%d/%Y'),
            "is_dangerous": fake.boolean(chance_of_getting_true = 20),
            "is_urgent" : fake.boolean(chance_of_getting_true = 30),
            "possible_delivery_date" : datetime.strftime(fake.date_this_year(before_today = False, after_today = True), '%m/%d/%Y'),
            "ground_price" : round(fake.pyfloat(min_value=25, max_value=200),2) if fake.boolean(chance_of_getting_true = 50) else -1.00,
            "air_price" : round(fake.pyfloat(min_value=25, max_value=200),2) if fake.boolean(chance_of_getting_true = 50) else -1.00,
            "ocean_price" : round(fake.pyfloat(min_value=25, max_value=200),2) if fake.boolean(chance_of_getting_true = 50) else -1.00,
            "preferred_route" : "ground" if fake.boolean(chance_of_getting_true = 33) else "air" if fake.boolean(chance_of_getting_true = 50) else "ocean"
        }
        for _ in range(100)
    ]
)

filename = "/../resources/booking_quotes.csv"
csv_path = Path(os.path.dirname(os.path.abspath(__file__)) + filename)
df.to_csv(csv_path, index=False, quoting=csv.QUOTE_NONNUMERIC)