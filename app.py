from flask import Flask, render_template, request
from urllib import request as r


def country_summary(country):
    html = r.urlopen("https://api.covid19api.com/summary")
    data = html.read()
    data_as_dict = eval(data.decode("UTF-8"))
    x = []
    found = False

    for countries in data_as_dict["Countries"]:
        if countries['Country'] == country:
            for info in countries:
                country_data = info, countries[info]
                x.append(country_data)
            found = True
    if found == False:
        return "Country not found 🙁"
    return list(x[4:11])

app = Flask(__name__)

@app.route('/')  # , methods=['GET','POST']
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def getValue():
    country = request.form['country']
    result = country_summary(country)
    final_data = ''
    try:
        for (stat, num) in result:
            last_but_before_final_data = "{}: {},\n".format(stat, num)
            final_data += (last_but_before_final_data)
    except:
        if result == "Country not found 🙁":
            final_data = "Country not found 🙁"


    return render_template("index.html", r=final_data)


if __name__ == "__main__""":
    app.run(debug=True)
