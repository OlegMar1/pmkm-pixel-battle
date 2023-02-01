from flask import Flask, render_template, jsonify, request
import pusher

pusher_client = pusher.Pusher(
    app_id='1539388',
    key='eaf74954e926bfb7e254',
    secret='bbe4fca250192997d5b5',
    cluster='eu',
    ssl=True
)


class PixelBattle:
    def __init__(self, app: Flask):
        @app.route("/")
        def output():
            return render_template('index.html')

        @app.route('/paint-pixel', methods=['POST'])
        def message():
            try:
                data = request.get_json()
                color = data['color']
                coord_x = data['coord_x']
                coord_y = data['coord_y']
                pusher_client.trigger('pixel-battle-channel', 'paint-pixel', {'color': color, 'coord_x': coord_x, 'coord_y': coord_y})
                return jsonify({'result': 'success'})
            except:
                return jsonify({'result': 'failure'})
