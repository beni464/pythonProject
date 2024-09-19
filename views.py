from flask import Blueprint, render_template, jsonify, request, redirect, url_for

views = Blueprint(__name__, 'views')


@views.route('/')
def home():
    return render_template('index.html')


@views.route('/start')
def get_data():
    return render_template('start.html')




