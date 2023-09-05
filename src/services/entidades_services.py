from src.model.entidades_model import reconocer_entidad

class entidadesServices():
    @classmethod
    def entidades_texto(cls,texto):
        resultado = []
        for frase in texto:
            entidades= reconocer_entidad(frase)
            resultado.append({"oracion":frase, "entidades": entidades})
        return resultado;

