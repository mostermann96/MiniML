from flask import Flask
from flask import request
from sklearn.linear_model import  LinearRegression
from random import randint


"""Gewicht:
#Realfahrzeit bestehnd aus Geolocation und Fahrplan
#Wetter 1-4 || Sonne:1 Wind:2 Regen/Schnee:3 Sturm/Eis:4
Datum Monatsunterteilung 1:6-9 2:3-5 3:10-11 4: 12-2 """

TRAIN_SET_LIMIT = 10
TRAIN_SET_COUNT = 1000


app = Flask(__name__)
@app.route('/machine', methods=['GET', 'POST'])
def func():
    date = request.args.get('date', type = int)
    weather = request.args.get('weather', type= int)
    salt = request.args.get('salt', type= int)

    TRAIN_INPUT = list()
    TRAIN_OUTPUT = list()

    for i in range(TRAIN_SET_COUNT):
        a = randint(0, TRAIN_SET_LIMIT)
        b = randint(0, TRAIN_SET_LIMIT)
        c = randint(0, TRAIN_SET_LIMIT)

        op = 1 + ((a * b * c)) / (899)

        TRAIN_INPUT.append([a, b, c])
        TRAIN_OUTPUT.append(op)

    predictor = LinearRegression(n_jobs=-1)
    predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)

    X_TEST=[[date, weather, salt]]

    outcome = predictor.predict(X=X_TEST)
    coefficients = predictor.coef_
    return str(outcome)

