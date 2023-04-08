from faker import Faker
from settings import csv_path
import pandas as pd


fake = Faker()

df = pd.DataFrame(
    [
        {
            "booking_id" : fake.unique.random_int(min=1, max=999),
            "customer_name" : fake.name(),
            "destination_country" : "United States of America" if fake.boolean(chance_of_getting_true = 50) else fake.country(),
            "destination_city" : fake.city(),
            "package_description" : fake.sentence(nb_words=8),
            "weight" : fake.pyfloat(min_value=0, max_value=10),
            "volume" : fake.pyfloat(min_value=0, max_value=125),
            "required_delivery_date" : fake.date('%m/%d/%Y'),
            "is_dangerous": fake.boolean(chance_of_getting_true = 20),
            "is_urgent" : fake.boolean(chance_of_getting_true = 30),
            "price_accepted" : fake.pyfloat(min_value=25, max_value=200)
        }
        for _ in range(100)
    ]
)

df.to_csv(csv_path, index=False)