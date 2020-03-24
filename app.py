from flask import Flask

app = Flask(__name__)
order_queue = []

@app.route('/')
def hello_whale():
    return "Whale, Hello there!"


@app.route('/add_to_orders')
def add_to_order_queue():
    order_queue.append('something')
    return 'thing done'

@app.route('/list_orders')
def list_orders():
    return "\n".join(order_queue)


@app.route('/update')
def update():
    return 'Done!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
