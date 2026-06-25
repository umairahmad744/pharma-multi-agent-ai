import pandas as pd

import random

from sklearn.ensemble import IsolationForest

import joblib


data=[]

for i in range(500):

    temp=random.randint(30,60)

    pressure=random.randint(80,130)

    ph=round(

        random.uniform(5.5,8),

        2

    )

    yield_rate=random.randint(70,100)

    mixing=random.randint(10,40)

    defect=random.randint(0,10)

    data.append(

        [

            temp,

            pressure,

            ph,

            yield_rate,

            mixing,

            defect

        ]

    )


df=pd.DataFrame(

    data,

    columns=[

        "temperature",

        "pressure",

        "ph",

        "yield",

        "mixing_time",

        "defect_rate"

    ]

)

model=IsolationForest(

    contamination=0.05,

    random_state=42

)

model.fit(df)

joblib.dump(

    model,

    "ml/anomaly_model.pkl"

)

print(

    "Model trained"

)