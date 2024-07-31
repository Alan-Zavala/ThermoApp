from flask import render_template, session, request, redirect, url_for, flash, current_app as app
from app import db
from app.models import Element

@app.route('/main')
def main():
    return render_template('index.html')
