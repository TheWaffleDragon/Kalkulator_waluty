from flask import Flask,render_template, request, url_for

import csv


app = Flask(__name__)

@app.route("/Kalkulator")  
def simple(): 
    return render_template("calc.html") 


@app.route("/calc", methods=["POST"])     
def calc():
    currency_type = request.form["currencyType"] 
    currency_amount = request.form["currencyAmount"] 
    with open('rates.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter =";") 
        for row in reader:
            if row['code'] == currency_type:
                course = row['bid']
                result=float(course)*float(currency_amount)
                return render_template("calc.html", result=result) 
     

if __name__ == '__main__':  
    app.run(debug=True) 