# use face recognition iterator image face
import face_recognition
import cv2 as cv
import numpy as np
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont
imageCV = cv.imread('img/unknow.jpg')
knowImg1 = face_recognition.load_image_file('img/李沁.jpg')
knowImg2 = face_recognition.load_image_file('img/杜江.jpg')
knowImg3 = face_recognition.load_image_file('img/欧豪.jpg')
knowImg4 = face_recognition.load_image_file('img/袁泉.jpg')
unknow = face_recognition.load_image_file('img/unknow.jpg')
unknowLocation = face_recognition.face_locations(unknow)

face_encoding1 = face_recognition.face_encodings(knowImg1)[0]
face_encoding2 = face_recognition.face_encodings(knowImg2)[0]
face_encoding3 = face_recognition.face_encodings(knowImg3)[0]
face_encoding4 = face_recognition.face_encodings(knowImg4)[0]
known_face_encodings = []
known_face_encodings.append(face_encoding1)
known_face_encodings.append(face_encoding2)
known_face_encodings.append(face_encoding3)
known_face_encodings.append(face_encoding4)
known_face_names = ['李沁','杜江','欧豪','袁泉']
i = 0
for pos in unknowLocation:
    name = 'unknown'
    cv.rectangle(imageCV,(pos[3],pos[0]),(pos[1],pos[2]),(0,255,0),4)
    unknows = face_recognition.face_encodings(unknow)[i]
    i =i +1
    results = face_recognition.compare_faces(known_face_encodings,unknows)
    # # If a match was found in known_face_encodings, just use the first one.
    # if True in matches:
    #     first_match_index = matches.index(True)
    #     name = known_face_names[first_match_index]

    # Or instead, use the known face with the smallest distance to the new face
    face_distances = face_recognition.face_distance(known_face_encodings, unknows)
    best_match_index = np.argmin(face_distances)
    if results[best_match_index]:
        name = str(known_face_names[best_match_index]) + str(round(face_distances[best_match_index] * 100,2)) + '%'

    #cv.putText(imageCV, name, (pos[3] + 6, pos[2] - 6), font, 1.0, (255, 255, 255), 1)



    # PIL图片上打印汉字
    cv2img = cv.cvtColor(imageCV, cv.COLOR_BGR2RGB)  # cv2和PIL中颜色的hex码的储存顺序不同
    pilimg = Image.fromarray(cv2img)
    draw = ImageDraw.Draw(pilimg)  # 图片上打印
    draw.line(face_recognition.face_landmarks(unknow)[0]['chin'], fill=(255, 0, 0, 128),width=3)
    font = ImageFont.truetype('/Library/Fonts/Songti.ttc',14, encoding="utf-8")
    draw.text((pos[3] , pos[0] - 26), name, (255, 255, 255), font=font)  # 参数1：打印坐标，参数2：文本，参数3：字体颜色，参数4：字体
    # PIL图片转cv2 图片
    imageCV = cv.cvtColor(np.array(pilimg), cv.COLOR_RGB2BGR)

cv.imshow('img',imageCV)
cv.waitKey(0)

