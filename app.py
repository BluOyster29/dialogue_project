from flask import Flask, render_template, make_response, send_from_directory

app = Flask(__name__)

song = ["audio/metal.wav", "audio/metal.wav"]

@app.route('/main_menu')
def main_menu():
    vxml = render_template('main_menu.xml')
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
    vxml = render_template('test.xml', song=song[0])
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response    

@app.route('/grammars/<path:path>')
def send_grammar(path):
    return send_from_directory('grammars', path)

@app.route('/audio/<path:path>')
def send_audio(path):
    return send_from_directory('audio', path)

if __name__ == "__main__":
    app.run(debug=True)
