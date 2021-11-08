from __main__ import app

@app.route('/user', methods=['GET'])
def test():
    return 'it works!'
