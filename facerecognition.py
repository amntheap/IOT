import cv2
import face_recognition


# Load the known faces and their encodings
known_face_encodings = []
known_face_names = []

for i in range(1, 4):  # Load 3 images
    known_image = face_recognition.load_image_file(f"known_face_{i}.jpg")
    known_face_encoding = face_recognition.face_encodings(known_image)[0]
    known_face_encodings.append(known_face_encoding)
    known_face_names.append(f"Person {i}")

# Initialize video capture
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert the frame to RGB format (OpenCV uses BGR)
    rgb_frame = frame[:, :, ::-1]

    # Find faces in the frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in this frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Match the face encodings with the known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # If a match was found, use the first match's name
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a rectangle around the face and label it with the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
