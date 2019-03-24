from flask import Flask, render_template, make_response, send_from_directory, jsonify, request
from nltk import word_tokenize


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
    vxml = render_template('test.xml')
    response = make_response(vxml)
    response.headers["Content-Type"] = "application/xml"
    return response    

@app.route('/grammars/<path:path>')
def send_grammar(path):
    return send_from_directory('grammars', path)

@app.route('/audio/<path:path>')
def send_audio(path):
    return send_from_directory('audio', path)

@app.route('/interactive/')
def interactive():
	# serve index template
    try:
	    return render_template('interactive.html')
    except Exception as e:
        return (str(e))

@app.route('/background_process')
def background_process():
    try:
        name = request.args.get('playerName', 0, type=str)

        score = request.args.get('playerScore', 0, type=str)
      
        if name:
            add_leaderboard(name)
            return jsonify(result=name)
        elif score:
            add_leaderboard(score)
            return jsonify(result=score)
        '''
		if lang.lower() == 'python':
			return jsonify(result='You are wise')
		else:
			return jsonify(result='Try again.')
        '''
    except Exception as e:
        return str(e)


def add_leaderboard(output):
    with open('leaderboard.md', 'rb') as l:
        lines = l.readlines()
        print(word_tokenize(lines))
        print(output)
        
        
if __name__ == "__main__":
    app.run(debug=True)
