from flask import Blueprint, jsonify, request
from src.services.entidades_services import entidadesServices
main = Blueprint('entidades',__name__)

@main.route('/',methods=['POST'])
def entidades():
    texto: list = request.json['oraciones']
    if len(texto) == 0:
        return jsonify({"status":"failer", "message": "agregar frases"})
    respuesta = entidadesServices.entidades_texto(texto)
    if respuesta is None:
        return jsonify({"status":"failer", "message": "no se encontro las entidades"})
    response = jsonify({"resultado":respuesta})
    return response