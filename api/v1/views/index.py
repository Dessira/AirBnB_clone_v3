#!/usr/bin/python3
"""Checks status"""

from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage


classes = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User"
}

@app_views.route('/status', methods=['Get'])
def return_status():
    """returns the status of the request"""
    return jsonify({'status': 'OK')

@app_views.route('/stats', strict_slashes=False)
def stats():
    my_list = {}
    for key, value in classes.items():
        num = storage.count(value)
        my_list[key] = num
    return jsonify(my_list)


if __name__ == "__main__":
    pass
