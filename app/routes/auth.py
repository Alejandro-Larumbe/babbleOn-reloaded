from flask import Blueprint, request
from flask_login import current_user, login_user, logout_user
from app.models import User

bp = Blueprint("auth", __name__, url_prefix='/auth')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return 'Already authenticated'
    data = request.get_json()

    print(data['username'])
    user = User.query.filter(User.username == data['username']).first()
    if not user or not user.check_password(data.password):
        return 'user not found'
    login_user(user)

    return {user}
