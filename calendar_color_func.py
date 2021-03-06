from flask import (Flask, request, render_template, flash, session, jsonify, abort)
from model import *

def get_color_options(user_id):
    """ Query all DB for user's colorset user=0 or user=user_id
        Return array of obj rows 
    """
    
    return db.session.query(Colorset).filter(Colorset.user.in_([0, user_id])).order_by(Colorset.id).all()



def format_color_response(user_id):
    """ Format into dict colorset table
        Return {colorId: id, user: 0 or user_id, colorHex: hex, colorName: name, emotion: emotion}
    """

    all_color_row = get_color_options(user_id)

    response = []

    for row in all_color_row:
        response.append({
            'colorId': row.id,
            'user' : row.user,
            'emotion': row.emotion,
            'colorHex': row.colorHex,
            'colorName' : row.colorName
            })
    return response
