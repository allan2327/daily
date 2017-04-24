# Functions to support /signIn
from flask import (Flask, request, render_template, flash, session, jsonify, abort)
from model import *
from flask_bcrypt import Bcrypt
import re

# functions clear_old_session and email_in_db taken from signUp_func.def 



def confirm_password(email, password):
    """ Check if password matches hash
        Return Boolean
    """
    user = User.query.filter_by(email=email).first()
    return bcrypt.check_password_hash(user.password, password)

def add_to_session(email):
    """ Add user to session
        Return None
    """
    
    user = User.query.filter_by(email=email).first()
    session.setdefault('current_user', user.id)

    return 
    