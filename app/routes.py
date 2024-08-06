from flask import render_template, session, request, redirect, url_for, flash, current_app as app
from app import db
from app.models import Element
#from .calculations import in_water, in_contact
#from app.forms import InWaterForm

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/in_water', methods=['POST', 'GET'])
def in_water():
    #form = InWaterForm()
    #water_temp = float(form.water_T.data)

    return render_template('in_water.html')

@app.route('/in_waterLatent', methods=['POST', 'GET'])
def in_waterLatent():
    #form = InWaterForm()
    #water_temp = float(form.water_T.data)

    return render_template('in_waterLatent.html')

@app.route('/in_contact', methods=['POST', 'GET'])
def in_contact():
    #form = InWaterForm()
    #water_temp = float(form.water_T.data)

    return render_template('in_contact.html')

@app.route('/mars', methods=['POST', 'GET'])
def mars():
    #form = InWaterForm()
    #water_temp = float(form.water_T.data)

    return render_template('mars.html')