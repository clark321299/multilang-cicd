from flask import Flask, request, render_template, g
from flask_babel import Babel, gettext

app = Flask(__name__, template_folder='templates')
app.config['BABEL_DEFAULT_LOCALE'] = 'uk'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = '../translations'
babel = Babel(app)

@babel.localeselector
def get_locale():
    # Визначення мови з запиту або налаштувань користувача
    return request.args.get('lang', 'uk')

@app.route('/')
def index():
    return render_template('index.html', greeting=gettext('Hello World'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
