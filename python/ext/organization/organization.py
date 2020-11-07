from flask import Blueprint, request, jsonify
from python.models.organization import Organization
from python.controllers.organization_controller import OrganizationController
from python.models.user import User

org = Blueprint('org', __name__, url_prefix='/organization')
orgC = OrganizationController()

def init_app(app):
    app.register_blueprint(org)

@org.route('/add', methods=['POST'])
def add_org():
    data = request.get_json()
    ownerData = data['owner']
    owner = User(ownerData['name'], ownerData['email'], ownerData['discord_id'])
    return str(orgC.add_organization(data['name'], data['desc'], owner, data['category']))

@org.route('/list', methods=['GET'])
def list_orgs():
    response = {}
    orgs = orgC.list_organizations()
    
    for i in range(len(orgs)):
            temp_org = orgs[i].__dict__
            temp_owner = temp_org['owner']
            if(isinstance(temp_owner, User)):
                temp_owner = temp_owner.__dict__

            temp_org['owner'] = temp_owner
            response[i + 1] = temp_org

    return jsonify(response)


@org.route('/remove', methods=['DELETE'])
def remove_org():
    data = request.get_json()
    return orgC.remove_organization(data['org_Id']).__dict__
    

@org.route('/org', methods=['GET'])
def get_org():
    org_id = request.args.get('org_id')
    temp_org = orgC.get_organization(int(org_id)).__dict__
    temp_owner = temp_org['owner']

    if(isinstance(temp_owner, User)):
        temp_owner = temp_owner.__dict__

    temp_org['owner'] = temp_owner
    return temp_org