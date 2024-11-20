from flask import Blueprint, render_template, request, jsonify

bp = Blueprint('main', __name__)


@bp.route('/')
def home():
    return render_template('index.html')


@bp.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!', 203


@bp.route('/submit', methods=['POST'])
def submit():
    data = request.form['name']
    return f'Hello, {data}!'


@bp.route('/submit', methods=['GET'])
def submit_get():

    return f'Hello, Default Name!', 200


@bp.route('/search/<username>')
def search(username):
    query = request.args.get('q')
    page = request.args.get('page', 1)  # Если параметр 'page' не передан, по умолчанию будет 1
    return f'Hello {username}. Search query: {query}, Page: {page}'


@bp.errorhandler(404)
def page_not_found(e):
    return 'Sorry, this page does not exist'


@bp.route('/api/data')
def get_data():
    data = {
        'name': 'Flask API',
        'version': '1.0',
        'features': ['lightweight', 'easy to use', 'flexible']
    }
    return jsonify(data)