from flask import Flask, render_template, jsonify, request
import pusher
import boto3


class PixelBattle:
    def __init__(self, app: Flask):

        pusher_client = pusher.Pusher(
            app_id='1539388',
            key='eaf74954e926bfb7e254',
            secret='bbe4fca250192997d5b5',
            cluster='eu',
            ssl=True
        )
        dynamo_client = boto3.resource(
            'dynamodb',
            region_name='us-east-2'
        )
        table = dynamo_client.Table('pixes-battle-data')

        @app.route("/")
        def output():
            return render_template('index.html')

        @app.route('/paint-pixel', methods=['POST'])
        def paint_pixel():
            try:
                data = request.get_json()
                color = data['color']
                coord_x = data['coord_x']
                coord_y = data['coord_y']
                table.put_item(
                    Item={
                        'coordinates': f'{coord_x}:{coord_y}',
                        'color': color
                    }
                )
                pusher_client.trigger('pixel-battle-channel', 'paint-pixel', {'color': color, 'coord_x': coord_x, 'coord_y': coord_y})
                return jsonify({'result': 'success'})
            except:
                return jsonify({'result': 'failure'})

        @app.route('/initial-load', methods=['POST'])
        def initial_load():
            try:
                all_data = table.scan()['Items']
                dict = {}
                for i in all_data:
                    dict[i['coordinates']] = i['color']
                return jsonify(dict)
            except:
                return jsonify({'result': 'failure'})
