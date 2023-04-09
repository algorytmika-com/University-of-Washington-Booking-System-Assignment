import pandas as pd
import os, csv
from pathlib import Path
from faker import Faker

fake = Faker()

df = pd.DataFrame(
    [
        {
            "booking_id" : fake.unique.random_int(min=1, max=999),
            "customer_name" : fake.name(),
            "destination_country" : "United States of America" if fake.boolean(chance_of_getting_true = 50) else fake.country(),
            "package_description" : fake.sentence(nb_words=8),
            "weight" : fake.pyfloat(min_value=0, max_value=10),
            "volume" : fake.pyfloat(min_value=0, max_value=125),
            "required_delivery_date" : fake.date('%m/%d/%Y'),
            "is_dangerous": fake.boolean(chance_of_getting_true = 20),
            "is_urgent" : fake.boolean(chance_of_getting_true = 30),
            "route" : "ground" if fake.boolean(chance_of_getting_true = 33) else "air" if fake.boolean(chance_of_getting_true = 50) else "ocean",
            "price_accepted" : fake.pyfloat(min_value=25, max_value=200)
        }
        for _ in range(100)
    ]
)

filename = "/../resources/booking_quotes.csv"
csv_path = Path(os.path.dirname(os.path.abspath(__file__)) + filename)
df.to_csv(csv_path, index=False, quoting=csv.QUOTE_NONNUMERIC)