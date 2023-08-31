from flask import Blueprint, jsonify, request
from src.services.entidades_services import entidadesServices
main = Blueprint('entidades',__name__)

@main.route('/',methods=['POST'])
def entidades():
    texto: list = request.json['oraciones']
    respuesta = entidadesServices.entidades_texto(texto)
    response = jsonify({"resultado":respuesta})
    return response