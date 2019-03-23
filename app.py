from flask import Flask, render_template, make_response, send_from_directory
app = Flask(__name__)

@app.route('/altered_beast')
def game():
    vxml = render_template('altered_beast.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/main_menu')
def main_menu():
    vxml = render_template('main_menu.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/level_one')
def easy():
    vxml = render_template('level_one.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/fail')
def fail():
    vxml = render_template('fail.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/test')
def test():
    vxml = render_template('test.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response    

@app.route('/level_two')
def medium():
    vxml = render_template('level_two.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response

@app.route('/grammars/<path:path>')
def send_grammar(path):
    return send_from_directory('grammars', path)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/level_one")
def level_one():
    return render_template("level_one.html")

@app.route("/level_two")
def level_two():
    return render_template("level_two.html")

@app.route("/level_three")
def level_three():
    return render_template("level_three.html")

if __name__ == "__main__":
    app.run(debug=True)
