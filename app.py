from flask import Flask, send_from_directory, render_template, request, abort
from waitress import serve
from src.models.price_predictor import predict_price
from src.models.ohe_ng import encode_neighbor
from src.utils2 import final_data
from src.models.geocode import gcodeadd 

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def index():
    """Return the main page."""
    return send_from_directory("static", "index2.html")

# @app.route("/path", methods=["POST"])
# def handle_post_request():
#     if request.method == "POST":
#         data = request.form.to_dict()
#         data['some_key'] = "Some Value"
#         # ... do something with data ... 
#     return redirect("/")

@app.route("/get_results", methods=["POST"])
def get_results():
    """ Predict the class of wine based on the inputs. """
    data = request.form
    data_ng = encode_neighbor(data)
    data_geo = gcodeadd(data)
    print(data)
    print(data_ng)
    print(data_geo)

    test_value, errors = final_data(data,data_ng,data_geo)
    print(test_value)

    if not errors:
        predicted_class = predict_price(test_value).astype('int')
        return render_template("results.html", predicted_class=predicted_class)
    else:
        return abort(400, errors)

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)
