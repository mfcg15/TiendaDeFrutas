from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    sumaTotal = int(request.form['strawberry']) + int(request.form['raspberry'])+ int(request.form['apple'])
    print("Cobrando a "+request.form['first_name']+" "+request.form['last_name']+" por "+str(sumaTotal)+" frutas")
    return render_template("checkout.html", strawberry = request.form['strawberry'], raspberry = request.form['raspberry'], 
    apple = request.form['apple'], first_name = request.form['first_name'], last_name = request.form['last_name'],
    student_id = request.form['student_id'])

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    