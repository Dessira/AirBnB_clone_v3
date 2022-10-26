#!/usr/bin/python3
"""Checks status"""

from api.v1.views import app_views

@app_views.route('/status', methods=['Get'])
def return_status():
    """returns the status of the request"""
    return jsonify({'status': 'OK')
