from flask import Blueprint, request,jsonify
from python.models.subscribed import Subscribed
from python.controllers.subscribeds_controller import SubscribedsController
from python.models.user import User
import json

sub = Blueprint('sub',__name__, url_prefix='/subscribed')
subsController = SubscribedsController()

def init_app(app):
    app.register_blueprint(sub)

@sub.route('/', methods = ['POST'])
def add_sub():
    data = request.get_json()  
    subs = subsController.add_subscriber(data['name'],data['email'],data['discord_id'],data['period'],data['minority_group']) 
    return subs.__dict__

@sub.route('/', methods = ['GET'])
def list_sub():
    result = {}
    subs = subsController.list_subscribeds()

    for i in range (len(subs)):
        result[i + 1] = json.loads(subs[i].to_json())
    
    return result

@sub.route('/', methods = ['DELETE'])
def remove_org():
    data = request.get_json()
    print(data)
    return subsController.remove_subscribed(data['email_user']).to_json()