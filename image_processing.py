import face_recognition

def process_and_compare(id_card_filename, person_filename): #funcion defination with two arguments

    id_card_face = face_recognition.load_image_file(id_card_filename) #Loading ID card image
    person_face = face_recognition.load_image_file(person_filename) #Loading Person Face Image


    id_card_face_encoding = face_recognition.face_encodings(id_card_face)[0] #Face_encodings is facial features that can be compared to any other picture of a face

    person_face_encoding = face_recognition.face_encodings(person_face)[0] #face_encodings for numerical representations of person face features

    #calculate the similarity score between (id_card_face_encoding) and the person's image. Lower distances indicate more similar faces.
    
    similarity_score = face_recognition.face_distance([id_card_face_encoding], person_face_encoding)[0]

    match = similarity_score < 0.68  # You can adjust the threshold

    return similarity_score, match
