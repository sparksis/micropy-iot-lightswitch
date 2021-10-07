def setState(state):
    from app.httpclient import HttpClient

    client = HttpClient({'Content-Type': 'application/json'})
    response = client.post('https://maker.ifttt.com/trigger/livingroom_switch_toggled/json/with/key/bpGQDLtVGRPza0T7xPXGaR', data=f'{{"value":"{state}"}}')
