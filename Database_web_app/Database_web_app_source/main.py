from flask import Flask, render_template, request

app= Flask(__name__)

@app.route('/') # by efault this is a GET method
def index():
    return render_template('index.html')

@app.route('/success/', methods=['POST']) # if you want to specify another method
def success():
    if request.method == 'POST':
        print(request.form)
        email = request.form['userEmail'] # the defined name= variable in html is what you add here
        height = request.form['userHeight']
        age = request.form['userAge']
    return render_template('got_data.html')



# Check if file is main (the executed script)    
if __name__=='__main__':
    app.debug = True
    app.run(port=5000)