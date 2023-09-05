import spacy
def reconocer_entidad(frase):
    nlp = spacy.load('es_core_news_lg')
    documento = nlp(frase)
    for entidad in documento.ents:
        entidad = {
            entidad.text : entidad.label_

        }
        return entidad
   