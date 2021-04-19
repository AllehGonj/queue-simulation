import humps

from collections import namedtuple

from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

from model.factory import simulation, processes_flow_logs, lot_times

api = Blueprint('simulate', __name__)


@api.route('/', methods=['POST'])
@cross_origin()
def source():
    # Parse JSON into an object with attributes corresponding to dict keys.
    req = humps.decamelize(request.get_json())
    attrs = namedtuple("Simulation", req.keys())(*req.values())

    simulation(attrs)

    return jsonify(
        flowLogs=processes_flow_logs,
        lotTimes=lot_times
    ), 200
