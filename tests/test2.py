import spacy

# Cargar el modelo pre-entrenado de Spacy
nlp = spacy.load("es_core_news_sm")

# Texto de ejemplo
texto = "Buenos Dias , Como puedo recuperar mi Nombre de usuario "

# Procesar el texto con Spacy
doc = nlp(texto)

# Iterar sobre las entidades nombradas en el documento
for ent in doc.ents:
    # Si la entidad es una persona, imprimir su texto
    if ent.label_ == "PER":
        print(ent.text)
