from flask import Flask, render_template
import pandas as pd
import folium
from folium import IFrame
from collections import Counter
import json
import base64

app = Flask(__name__)

@app.route('/')
def index():
    start_coords = (-25.562265, 133.549433)

    folium_map1 = folium.Map(
        location=start_coords, 
        zoom_start=17
    )
    folium_map1.save('templates/map1.html')

    folium_map2 = folium.Map(
        location=start_coords, 
        zoom_start=17
    )
    folium_map2.save('templates/map2.html')


    return render_template('index.html')

@app.route('/map1')
def map1():
    return render_template('ausmap.html')

@app.route('/map2')
def map2():
    return render_template('statemap.html')


if __name__ == '__main__':
    app.run(debug=True)