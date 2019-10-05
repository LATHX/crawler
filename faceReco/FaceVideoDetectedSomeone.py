# use face recognition iterator image face
import face_recognition
import cv2 as cv
import numpy as np
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont

cap = cv.VideoCapture('video/2.mov')
isOpened = cap.isOpened()
known_face_names = ['李沁','杜江',
                    '欧豪','袁泉',
                    '余皑磊',
                    '关晓彤',
                    '刘浩','吴樾',
                    '张天爱','张涵予',
                    '朱亚文','李岷城',
                    '李现','杨祺如',
                    '杨颖','焦俊艳',
                    '阚清子','陈数',
                    '雅玫','高戈','黄志忠'
                    ]

known_face_encodings = []
for j in range(len(known_face_names)):
    filename = 'img/'+known_face_names[j]+'.jpg'
    if len(face_recognition.face_encodings(face_recognition.load_image_file(filename))) >0:
        known_face_encodings.append(face_recognition.face_encodings(face_recognition.load_image_file(filename))[0])



while(isOpened):
    sucess, imageCV = cap.read()
    unknown_image = imageCV[:, :, ::-1]


    face_locations = face_recognition.face_locations(unknown_image)
    face_encodings = face_recognition.face_encodings(unknown_image, face_locations)
    pil_image = Image.fromarray(unknown_image)
    # Create a Pillow ImageDraw Draw instance to draw with
    draw = ImageDraw.Draw(pil_image)

    # Loop through each face found in the unknown image
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding,tolerance=0.53)
        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        #if True in matches:
        #    first_match_index = matches.index(True)
        #   name = known_face_names[first_match_index]

        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = str(known_face_names[best_match_index]) + str(round(face_distances[best_match_index] * 100, 2)) + '%'
        # Draw a box around the face using the Pillow module
        draw.rectangle(((left, top), (right, bottom)), outline=(255, 0, 0))

        # Draw a label with a name below the face
        font = ImageFont.truetype('/Library/Fonts/Songti.ttc', 15, encoding="utf-8")
        text_width, text_height = draw.textsize(name,font=font)
        draw.text((left, top - 25), name, fill=(255, 0, 0, 255), font=font)
        imageCV = cv.cvtColor(np.array(pil_image), cv.COLOR_RGB2BGR)
        #cv.rectangle(imageCV, (left, top), (right, bottom), (0, 0, 255), 2)
    cv.imshow('img',imageCV)
    #time.sleep(1)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyWindow()
