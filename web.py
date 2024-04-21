from flask import Flask, request

app = Flask(__name__)

def getTags(text):
	# run model
	return 'tags'

def getPage(input='', output=''):
	return '''
		<html>
			<head>
			<title>Text2Tag</title>
			</head>
			<body>
			<div style="text-align: center">
			<h2>Текст статьи:</h2>
			<form method="POST">
			<textarea name="textarea" cols="100" rows="20">{0}</textarea>
			<br><br>
			<input type="submit" value="Получить тэги">
			</form>
			<br>
			<h2>Тэги статьи:</h2>
			<output name="result" for="a b">{1}</output>
			</div>
			</body>
		</html>
		'''.format(input, output)

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		text = request.form.get('textarea')
		res = getTags(text)
		return getPage(text, res)
	return getPage()

app.run(host='0.0.0.0', port=8080)
