import spacy

class entidadesServices():
    @classmethod
    def entidades_texto(cls,texto):
        
        resultado = []

        for frase in texto:
            entidades= reconocer_entidad(frase)
            resultado.append({"oracion":frase, "entidades": entidades})
        return resultado;

def reconocer_entidad(frase):
    nlp = spacy.load('es_core_news_sm')
    documento = nlp(frase)
    for entidad in documento.ents:
        entidad = {
            entidad.text : entidad.label_

        }
        return entidad
   