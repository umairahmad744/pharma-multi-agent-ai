import pandas as pd

import joblib


model = joblib.load(

    "ml/anomaly_model.pkl"

)


def anomaly_agent(state):

    sample_data = [

        {

            "batch":"B001",

            "temperature":35,

            "pressure":95,

            "ph":6.8,

            "yield":95,

            "mixing_time":20,

            "defect_rate":1

        },

        {

            "batch":"B002",

            "temperature":58,

            "pressure":128,

            "ph":5.7,

            "yield":72,

            "mixing_time":38,

            "defect_rate":9

        },

        {

            "batch":"B003",

            "temperature":36,

            "pressure":92,

            "ph":7.0,

            "yield":96,

            "mixing_time":22,

            "defect_rate":1

        }

    ]


    df = pd.DataFrame(

        sample_data

    )


    features = df[[

        "temperature",

        "pressure",

        "ph",

        "yield",

        "mixing_time",

        "defect_rate"

    ]]


    predictions = model.predict(

        features

    )


    anomalies = []


    for row,pred in zip(

        sample_data,

        predictions

    ):

        if pred == -1:

            anomalies.append(

                row

            )


    return {

        **state,

        "anomalies": anomalies

    }