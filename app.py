from flask import Flask ,request, render_template
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")
@app.route('/analysis', methods=["GET","POST"])
def result():
    text = request.form.get("text")
    model = joblib.load('svc_model.pkl')
    prediction = model.predict([text])
    if prediction[0]>=3:
        review="Positive"
    else:
        review="Negative"
    return render_template("home.html",prediction=review)
 
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")