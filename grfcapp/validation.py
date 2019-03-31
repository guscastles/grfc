"""
Validation Module For The Web App (Mobile Version)

Validations for routes in the web app.
"""
import re
from flask import request, jsonify
from wtforms import Form, StringField, PasswordField, validators, ValidationError


def only_text(form, field):
    """Checks for only text values (no spaces) in the given field."""
    value = field.data
    if re.search(" ", value):
        raise ValidationError(f'Invalid {field.label.text}')


def only_text_or_email(form, field):
    """Checks for only text or email address values in the given field."""
    value = field.data
    if re.search("[^\.a-zA-Z@\-']", value):
        raise ValidationError(f'Invalid {field.label.text}')


class LoginForm(Form):
    """Custom Form class for login form."""

    username = StringField('username', [
        validators.DataRequired(),
        only_text_or_email,
        validators.Length(min=4, max=50),
    ])
    password = PasswordField('password', [
        validators.DataRequired(),
        only_text,
        validators.Length(min=12, max=20),
    ])


VALIDATORS = {"/authenticate": LoginForm}


def check_request_params():
    """Checks the request parameters by route."""
    path = request.path
    validate_function = VALIDATORS.get(path, None)
    if validate_function:
        form = validate_function(request.form)
        if not form.validate():
            return jsonify(success=False, errors=form.errors)

