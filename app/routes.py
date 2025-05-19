from flask import render_template, session, request, redirect, url_for, flash, current_app as app
from app import db
from app.models import Element
#from .calculations import in_water, in_contact
from app.forms import InWaterForm, InContactForm, InMarsForm

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/in_water', methods=['POST', 'GET'])
def in_water():
    form = InWaterForm()
    if form.validate_on_submit():
        try:
            m_water = float(form.m_water.data)
            t_water = float(form.t_water.data)
            c_water = 4.184  # J/g·°C
            t_object = float(form.t_object.data)
            m_object = float(form.m_object.data)
            c_object = float(form.c_object.data)

            cm_water = c_water * m_water
            cm_object = c_object * m_object
            result = (cm_object * t_object + cm_water * t_water) / (cm_object + cm_water)
            result = round(result, 2)

            return render_template('in_water.html', form=form, result=result, m1=form.m_water.data,T1=form.t_water.data,
                                   T2=form.t_object.data,m2=form.m_object.data,c2=form.c_object.data)

        except (TypeError, ValueError):
            flash("Invalid input. Please enter valid numbers.")
            return render_template('in_water.html', form=form)

    if request.method == 'POST':
        flash('All fields are required.')

    return render_template('in_water.html', form=form)


@app.route('/in_waterLatent', methods=['POST', 'GET'])
def in_waterLatent():
    form = InWaterForm()
    if form.validate_on_submit():
        try:
            m_water = float(form.m_water.data)  # g 
            t_water = float(form.t_water.data)  # C
            c_water = 4.184  # J/g·°C
            t_object = float(form.t_object.data)
            m_object = float(form.m_object.data)
            c_object = float(form.c_object.data)

            cm_water = c_water * m_water
            cm_object = c_object * m_object
            result = (cm_object * t_object + cm_water * t_water) / (cm_object + cm_water)
            result = round(result, 2)

            return render_template('in_waterLatent.html', form=form, result=result, m1=form.m_water.data,T1=form.t_water.data,
                                   T2=form.t_object.data,m2=form.m_object.data,c2=form.c_object.data)

        except (TypeError, ValueError):
            flash("Invalid input. Please enter valid numbers.")
            return render_template('in_waterLatent.html', form=form)

    if request.method == 'POST':
        flash('All fields are required.')

    return render_template('in_waterLatent.html', form = form)

@app.route('/in_contact', methods=['POST', 'GET'])
def in_contact():
    form = InContactForm()
    if form.validate_on_submit():
        try:
            m_1 = float(form.m_1.data)  # g
            t_1 = float(form.t_1.data)  # C
            c_1 = float(form.c_1.data)  # J/g·°C
            t_2 = float(form.t_2.data)  
            m_2 = float(form.m_2.data)
            c_2 = float(form.c_2.data)

            cm_1 = c_1 * m_1
            cm_2 = c_2 * m_2
            result = (cm_1 * t_1 + cm_2 * t_2) / (cm_1 + cm_2)
            result = round(result, 2)

            return render_template('in_contact.html', form=form, result=result, m1=form.m_1.data,T1=form.t_1.data,
                                   c1=form.c_1.data, T2=form.t_2.data,m2=form.m_2.data,c2=form.c_2.data)

        except (TypeError, ValueError):
            flash("Invalid input. Please enter valid numbers.")
            return render_template('in_contact.html', form=form)

    if request.method == 'POST':
        flash('All fields are required.')

    return render_template('in_contact.html', form=form)

@app.route('/mars', methods=['POST', 'GET'])
def mars():
    #form = InWaterForm()
    #water_temp = float(form.water_T.data)

    return render_template('mars.html')