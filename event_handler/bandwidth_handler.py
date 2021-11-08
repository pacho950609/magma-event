from __main__ import app
from event_service.bandwidth_service import upgradeBandwidth, downgradeBandwidth

@app.route('/bandwidth/upgrade', methods=['GET'])
def upgradeBandwidthHandler():
    upgradeBandwidth()
    return 'it works!'

@app.route('/bandwidth/downgrade', methods=['GET'])
def downgradeeBandwidthHandler():
    downgradeBandwidth()
    return 'it works2!'
