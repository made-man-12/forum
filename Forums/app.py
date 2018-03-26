from flask import Flask, render_template
from dummy_data import stores, models

app = Flask(__name__)
post_stores = stores.PostStore()


@app.route('/')
@app.route('/index')
def home():
    return render_template('index.html', posts=post_stores.get_all())


if __name__ == '__main__':
    app.run(port=8001, debug=True)
