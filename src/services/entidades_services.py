import spacy

class entidadesServices():
    @classmethod
    def entidades_texto(cls,texto):
        
        resultado = []

        for frase in texto:
            entidades= reconocer_entidad(frase)
            listado = list(entidades)
            resultado.append({"oracion":frase, "entidades": listado})
        return resultado;

def reconocer_entidad(frase):
    nlp = spacy.load('es_core_news_sm')
    documento = nlp(frase)
    for entidad in documento.ents:
        return  {entidad.text, entidad.label_}
   