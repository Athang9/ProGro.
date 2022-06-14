# from crypt import methods
# from os import link
from typing import Collection
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
    url_for,
    make_response,
    jsonify,
)
import pickle

# from matplotlib.pyplot import get
# import numpy as np
# import pymongo
# from pymongo import MongoClient
import requests

res = []

# cluster = pymongo.MongoClient("mongodb://localhost:27017/ProgroBlogs")
# db = cluster["ProgroBlogs"]
# collection = db["Bulletin"]

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/fertilizer/")
def fertilizer():
    return render_template("fertilizer.html")


@app.route("/cropre/", methods=["POST"])
def cropre():
    N = request.form["n"]
    P = request.form["p"]
    K = request.form["k"]
    T = request.form["t"]
    H = request.form["h"]
    PH = request.form["ph"]
    R = request.form["r"]
    model = pickle.load(open("crop.pkl", "rb"))
    data = [[N, P, K, T, H, PH, R]]
    pred = model.predict(data)
    pred1 = str(pred[0])
    msg = "You should grow "
    msg1 = " in your farm."
    msg2 = msg + pred1 + msg1
    return render_template("Crop prediction.html", ms=msg2)


@app.route("/ferpre/", methods=["POST"])
def ferpre():
    N = request.form["n"]
    P = request.form["p"]
    K = request.form["k"]
    T = request.form["t"]
    H = request.form["h"]
    M = request.form["m"]
    # CR=request.form['c']
    # print(CR)
    # 	if CR == 'Maize':
    # 		C = 0
    # 	elif CR == 'Sugarcane':
    # 		C = 1
    # 	elif CR == 'Cotton':
    # 		C = 2
    # 	elif CR == 'Tobacco':
    # 		C = 3
    # 	elif CR == 'Paddy':
    # 		C = 4
    # 	elif CR == 'Barley':
    # 		C = 5
    # 	elif CR == 'Wheat':
    # 		C = 6
    # 	elif CR == 'Millets':
    # 		C = 7
    # 	elif CR == 'Oil seeds':
    # 		C = 8
    # 	elif CR == 'Pulses':
    # 		C = 9
    # 	elif CR == 'Ground Nuts':
    # 		C = 10
    model = pickle.load(open("fert.pkl", "rb"))
    data = [[T, H, M, 4, N, P, K]]
    pred = model.predict(data)
    pred1 = pred[0]
    if pred1 == "Urea":
        return render_template("urea.html")
    elif pred1 == "17-17-17":
        return render_template("17-17-17.html")
    elif pred1 == "20-20":
        return render_template("20-20.html")
    elif pred1 == "DAP":
        return render_template("DAP.html")
    elif pred1 == "14-35-14":
        return render_template("14-35-14.html")
    elif pred1 == "10-26-26":
        return render_template("10-26-26.html")
    elif pred1 == "28-28":
        return render_template("28-28.html")
    else:
        return render_template("fertilizer.html", m=pred1)


# @app.route('/fpredict/', methods=["POST"])
# def fpredict():
#   	N=request.form['n']
# 		P=float(request.form['p'])
# 		K=request.form['k']
# 		T=request.form['t']
# 		H=request.form['h']
# 		M=request.form['m']
# 		CR=request.form['cro']
# 		with open('fert.pkl','rb') as f:
# 			model = pickle.load(f)
# 		data = [[T,H,M,0,N,P,K]]
# 		pred = model.predict(data)
# 	return render_template("fertilizer.html", m=pred)
# if request.method == "POST":
# 	N=float(request.form['n'])
# 	print(N)
# 	P=float(request.form['p'])
# 	print(P)
# 	K=float(request.form['k'])
# 	T=float(request.form['t'])
# 	H=float(request.form['h'])
# 	M=float(request.form['m'])
# 	CR=request.args.get('cro')
# 	if CR == 'Maize':
# 			C = 0
# 	elif CR == 'Sugarcane':
# 			C = 1
# 	elif CR == 'Cotton':
# 			C = 2
# 	elif CR == 'Tobacco':
##			C = 3
# 	elif CR == 'Paddy':
# 			C = 4
# 	elif CR == 'Barley':
# 			C = 5
# 	elif CR == 'Wheat':
# 			C = 6
# 	elif CR == 'Millets':
# 			C = 7
# 	elif CR == 'Oil seeds':
# 			C = 8
# 	elif CR == 'Pulses':
# 			C = 9
# elif CR == 'Ground Nuts':
# 		C = 10
# 	data = [[28, 54, 46, 2,35, 0, 0]]
# 	print(data)
# 	with open('fert.pkl','rb') as f:
# 		model = pickle.load(f)
# 	prediction = model.predict(data)
# 	print(prediction)
# 	msg = "You should use this" + str(prediction)
# 	print(msg)
# 	return render_template("result.html", m=msg)
# else:
# 	return render_template("fertilizer.html")

# def new_func():

#   return elif


@app.route("/crop/")
def crop():
    # if request.method == "POST":
    # 		N=float(request.args.get('n'))
    # 		K=float(request.args.get('k'))
    # 		P=float(request.args.get('p'))
    # 		T=float(request.args.get('t'))
    # 		H=float(request.args.get('h'))
    # 		PH=float(request.args.get('ph'))
    # 		R=float(request.args.get('r'))
    # 		prediction = model.predict[[N,K,P,T,H,PH,R]]
    # 		msg = "You should grow this" + str(prediction)
    # 		return render_template("Crop prediction.html", m=msg)
    # else:
    return render_template("Crop prediction.html")


# @app.route('/predict/')
# def predict():
# 		N=float(request.args.get('n'))
# 		K=float(request.args.get('k'))
# 		P=float(request.args.get('p'))
# 		T=float(request.args.get('t'))
# 		H=float(request.args.get('h'))
# 		PH=float(request.args.get('ph'))
# 		R=float(request.args.get('r'))
# 		data = [[N,P,K,T,H,PH,R]]
# 		with open('crop.pkl','rb') as f:
# 			model = pickle.load(f)
# 		prediction = model.predict(data)
# 		msg = "You should grow this" + str(prediction)
# 		return render_template("Crop prediction.html", m=msg)
# try:
# 	prediction = model.predict(request.form.get('n','k','p','t','h','ph','r'))
# 	print([[request.form.get('n','k','p','t','h','ph','r')]])
# 	print(prediction)
# 	return render_template("Crop prediction.html", prediction_text=f'You should grow this {prediction}')
# except:
# 	return render_template('Crop prediction.html', prediction_text=f"Invalid Input")
# 	int_features = [int(x) for x in request.form.values()]
# 	final_features = [np.array(int_features)]
# 	prediction = model.predict(final_features)
# 	output = prediction[0]
# 	print(output)
# 	return render_template('Crop prediction.html', prediction_text = "You should grow this ${}".format(output))

# @app.route('/disease/')
# def disease():
#    return render_template('disease.html')


@app.route("/agrihub/")
def agrihub():
    return render_template("agrihub.html")


@app.route("/insights/")
def agriinsights():
    return render_template("insights.html")


@app.route("/blogs/")
def blogs():
    to_find_many = collection.find({}, {"_id": 0})
    for data in to_find_many:
        list_of_dict_values = list(data.values())
        res.append(list_of_dict_values[0])
    print(res)
    return render_template("Blogs.html", info=res)


@app.route("/insightsadmin/")
def insightsadmin():
    return render_template("insightsadmin.html")


@app.route("/dynamiccard/")
def dynamiccard():
    return render_template("adminpage.html")


# @app.route("/news/", methods=["post", "get"])
# def news():
#    cluster = pymongo.MongoClient("mongodb://localhost:27017/")
#    db = cluster["ProgroBlogs"]
#    collection1 = db["Bulletin"]
# head = request.form["heading"]
# abc = db.Bulletin.insert_many([{"heading": head}])
# to_find_many = collection1.find({}, {"_id": 0})

# for data in to_find_many:
#     list_of_dict_values = list(data.values())
#     res.append(list_of_dict_values[0])
# print(res)
# return render_template("Blogs.html", info=res)


# client = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.yzbk1.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client.test


@app.route("/formsignin/", methods=["post", "get"])
def signin():
    database = {"bhandarkarathang@gmail.com": "athang123@"}
    email = request.form["Email"]
    print(email)
    pwd = request.form["Password"]
    if email not in database:
        return render_template("insightsadmin.html")
    else:
        if database[email] != pwd:
            return render_template("insightsadmin.html")
        else:
            return render_template("dynamiccard.html")


@app.route("/adminpage/")
def adminpage():
    return render_template("adminpage.html")


@app.route("/agrinews/")
def agrinews():
    try:
        # a1= "https://serpapi.com/search.json?"
        # a2= "q=IndiaAgriculture&tbm=nws"
        # a3= '&api_key=b12217562727563e8f023a862765dac7a70f93ee5d16b65cfe45654851c93dcb'
        # wa= a1+a2+a3
        # res=requests.get(wa)
        r = requests.get(
            "https://serpapi.com/search.json?q=IndiaAgriculture&location=india&tbm=nws&api_key=b12217562727563e8f023a862765dac7a70f93ee5d16b65cfe45654851c93dcb"
        )
        data = r.json()
        # print(data)
        data1 = data["news_results"]
        print(data1)
        # for d in data1:
        # 	title=[]
        # print(r.json())
        # print(r.json(['news_results']))
        # data=res.json()
        # print(data)
        # info=data["news_results"]
        # print(info)
        return render_template("news.html", news=data1)
        # print(data)
        # return make_response(jsonify({"msg":info}))

        # params = {
        # "q": "India Agriculture",
        # "tbm": "nws",
        # "location": "",
        # "api_key": "b12217562727563e8f023a862765dac7a70f93ee5d16b65cfe45654851c93dcb"
        # }

        # search = GoogleSearch(params)
        # results = search.get_dict()
        # news_results = results['news_results']
        # print(news_results)
    except Exception as e:
        msg = "issue" + str(e)
        return render_template("news.html")
        return make_response(jsonify({"msg": msg}))
        print(make_response(jsonify({"msg": msg})))
    else:
        return render_template("news.html")

    # from requests_html import HTMLSession


if __name__ == "__main__":
    app.run(debug="True", host="127.0.0.1", port="8080")
