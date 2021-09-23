
from flask import Flask, request
from pandas import read_csv
from datetime import datetime

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    fileBytes = file.read()
    with open("values.csv", "w") as file:
        file.write(str(fileBytes))
    temp = {
        "A" : 0,
        "B" : 0,
        "5" : 0,
        "1" : 0,
    }
    csv = read_csv("values.csv", sep=";", engine="python")
    for index, row in csv.iterrows():
        if type(row["date"]) == str:
            if row["date"][-4:] == "2021":
                for char in row["values"]:
                    for _char in list(temp):
                        if _char == char:
                            temp[_char] += 1
    return temp, 200

app.run(port="8080")