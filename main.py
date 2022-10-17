from flask import Flask, render_template,request,make_response,jsonify,redirect, url_for

app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/Snehal')
def snehal():
    return 'Hello Snehal jejurkar'

@app.route('/home')
def gethtml():
    return render_template("home.html")

@app.route('/about')
def get_about():
    return render_template("about.html")



@app.route('/qs')
def get_qs():
    if request.args:
        req = request.args
        return " ".join(f"{k}:{v}" for k,v in req.items())
    return "No query"


order = {
    "order1": {
        "Size": "Small",
        "Toppings": "Cheese",
        "Crust": "Thin Crust"
    },
    "order2": {
        "Size": "Medium",
        "Toppings": "Tomato",
        "Crust": "Thick Crust"
    }
}


@app.route("/orders")
def get_order():
    response = make_response(jsonify(order), 200)
    return response


@app.route("/orders/<orderid>")
def get_order_details(orderid):
    if orderid in order:
        response = make_response(jsonify(order[orderid]), 200)
        return response
    return "Order not Found"


@app.route("/orders/<orderid>/<item>")
def get_item_details(orderid, item):
    item = order[orderid].get(item)
    if item:
        response = make_response(jsonify(item), 200)
        return response
    return "Order not Found"


Pizzas = ["Margrita", "Onion", "Tomato", "Mexican","Farmhouse"]


@app.route('/Menu')
def Menu_page():
    return render_template("menu.html", len=len(Pizzas), Pizzas=Pizzas)





if __name__ == '__main__':
    app.run(debug=True)