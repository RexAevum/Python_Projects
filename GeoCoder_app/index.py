from flask import Flask, render_template, request, send_file
from geopy.geocoders import ArcGIS
import pandas, os

# set up app
app = Flask(__name__)
geo = ArcGIS()

@app.route('/')
def geocode():
    return render_template('geocode_home.html')

@app.route('/done/', methods=['POST'])
def return_df():
    global dataFile, df
    if request.method == 'POST':
        dataFile = request.files['geoFile']
        df = pandas.read_csv(dataFile)
        location = df['Address'].apply(geo.geocode)
        df['Latitude'] = location.apply(lambda x: x.latitude if x != None else None)
        df['Longitude'] = location.apply(lambda x: x.longitude if x != None else None)
        df.to_csv('data/updated/updated_{}.csv'.format(dataFile.filename))
            
        return render_template('geocode_return.html', data=[df.to_html(classes='data', justify='center')], atributes= df.columns.values)

@app.route('/done/download')
def download():
    return send_file('data/updated/updated_{}.csv'.format(dataFile.filename), as_attachment=True, attachment_filename='updated_{}.csv'.format(dataFile.filename))

if __name__ == "__main__":
    app.run(debug=True)