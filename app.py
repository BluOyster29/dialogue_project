from flask import Flask, render_template, make_response, send_from_directory, jsonify, request

app = Flask(__name__)

@app.route('/rob_trivia')
def rob_trivia():
    vxml = render_template('rob_trivia.xml')
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

'''
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
            return jsonify(result=name)
        elif score:
            return jsonify(result=score)
        
		if lang.lower() == 'python':
			return jsonify(result='You are wise')
		else:
			return jsonify(result='Try again.')
        
    except Exception as e:
        return str(e)

@app.route('/leaderboard')
def leaderboard():
	# serve index template
    try:
	    return render_template('leaderboard.html')
    except Exception as e:
        return (str(e))

''' 
if __name__ == "__main__":
    app.run(debug=True)

