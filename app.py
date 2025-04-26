import cv2
import dlib
import numpy as np
from scipy.spatial import distance
import pygame
import mediapipe as mp
import time


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


mp_pose = mp.solutions.pose
pose = mp_pose.Pose()


pygame.mixer.init()
pygame.mixer.music.load('alarm.mp3')  # you can use any mp3/meme sound

def eye_aspect_ratio(eye):
    a = distance.euclidean(eye[1], eye[5])
    b = distance.euclidean(eye[2], eye[4])
    c = distance.euclidean(eye[0], eye[3])
    ear = (a + b) / (2.0 * c)
    return ear

def mouth_open(mouth):
    a = distance.euclidean(mouth[2], mouth[10])  # 51, 59
    b = distance.euclidean(mouth[4], mouth[8])   # 53, 57
    mouth_distance = (a + b) / 2.0
    return mouth_distance



cap = cv2.VideoCapture(0)

sleepy_frames = 0
yawn_frames = 0
SLEEPY_THRESHOLD = 0.25
YAWN_THRESHOLD = 45
alarm_on = False
while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        landmarks = predictor(gray, face)

        # Get coordinates for eyes
        leftEye = []
        rightEye = []
        mouth = []
        for n in range(36, 42):  # left eye
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            leftEye.append((x, y))
        for n in range(42, 48):  # right eye
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            rightEye.append((x, y))
        for n in range(48, 68):  # mouth
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            mouth.append((x, y))

        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        ear = (leftEAR + rightEAR) / 2.0

        mouthDist = mouth_open(mouth)

        # Check for sleepiness
        if ear < SLEEPY_THRESHOLD:
            sleepy_frames += 1
            if sleepy_frames >= 20:  # About 1 second if 20fps
                cv2.putText(frame, "SLEEPY ALERT!", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                if not alarm_on:
                    pygame.mixer.music.play(-1)  # Loop the alarm
                    alarm_on = True
        else:
            sleepy_frames = 0

        # Check for yawning
        if mouthDist > YAWN_THRESHOLD:
            yawn_frames += 1
            if yawn_frames >= 15:
                cv2.putText(frame, "YAWN ALERT!", (10, 60),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                if not alarm_on:
                    pygame.mixer.music.play(-1)
                    alarm_on = True
        else:
            yawn_frames = 0

        # Posture detection
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)
        if results and results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
            nose = landmarks[0]
            if nose.visibility > 0.5:
                nose_y = nose.y
                if nose_y > 0.5:
                    cv2.putText(frame, "POSTURE ALERT!", (10, 90),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    if not alarm_on:
                        pygame.mixer.music.play(-1)
                        alarm_on = True

        # 🧠 Now the important part:
        # STOP alarm if no sleepy/yawn/posture in current frame
        if sleepy_frames == 0 and yawn_frames == 0 and (
        not (results and results.pose_landmarks and nose.visibility > 0.5 and nose_y > 0.5)):
            if alarm_on:
                pygame.mixer.music.stop()
                alarm_on = False

    cv2.imshow("Sleepy Detector", frame)

    if cv2.waitKey(1) == 27:  # Press Esc to exit
        break

cap.release()
cv2.destroyAllWindows()
