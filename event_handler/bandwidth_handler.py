from __main__ import app

@app.route('/bandwidth/upgrade', methods=['GET'])
def upgradeBandwidthHandler():
    return 'it works!'

@app.route('/bandwidth/downgrade', methods=['GET'])
def downgradeeBandwidthHandler():
    return 'it works2!'
