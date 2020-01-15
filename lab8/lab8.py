import flask
import pandas

app = flask.Flask(__name__)

@app.route('/')
def index():
    with open('./data.txt', 'r', encoding = 'utf-8') as f:
        data = pandas.read_csv(f, sep = '\t', names=['№', 'Субъект РФ', '1959', '1970', '1979', '1989', '2002', '2010', '2013', '2014', '2015', '2016', '2017', '2018'])
        print(data)
    return flask.render_template('index.html', data = data.iterrows())

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)
