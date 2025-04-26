
# SleepyFace Detector for Online Classes

### A Real-Time Sleepiness, Yawning, and Posture Detection System
#### Built using OpenCV, Dlib, Mediapipe, and Pygame.

About
------
This project detects:
- Sleepiness by monitoring if your eyes are closed continuously.
- Yawning by detecting mouth opening.
- Bad Posture by checking if your head is tilted down.

If any sleepy behavior is detected, it plays a loud alarm to wake you up!

### Perfect for:
- Online classes
- Late-night coding
- Staying alert while studying

Tech Stack
-----------
- Python 3.8+
- OpenCV
- Dlib
- SciPy
- Pygame
- MediaPipe

How it works
------------
| Behavior Detected        | Trigger    |
|--------------------------|------------|
| Eyes closed for few secs | Play alarm |
| Yawning detected         | Play alarm |
| Head tilting down        | Play alarm |

The alarm automatically stops when normal posture and eye opening are restored.

Requirements
-------------
Install the required libraries:

pip install opencv-python dlib imutils scipy pygame mediapipe

Make sure you have these important files:
- shape_predictor_68_face_landmarks.dat
- alarm.mp3

Usage
------
1. Clone the repository or download the code.
2. Place the shape_predictor_68_face_landmarks.dat and alarm.mp3 in the project folder.
3. Run the script:

python app.py

4. Press Ctrl+C key to exit.

Features
---------
- Real-time Eye, Mouth, and Posture Detection
- Continuous alarm until you're awake
- Customizable Alarm Sound
- Smart alarm control (no repeated sounds if already playing)
- Lightweight and fast (works on most laptops)

Screenshots
------------
(Add your real screenshots later if you want.)

Future Improvements
--------------------
- Add a countdown timer before triggering the alarm.
- Send WhatsApp/SMS alerts to friends.
- Track sleepiness over time and generate a report.
- Deploy it as a web app using Streamlit.

Author
-------
Abhinav L G

[Github](https://github.com/abhinavlg )

Acknowledgements
-----------------
- MediaPipe
- Dlib
- OpenCV
- Pygame

License
--------
This project is open-source and free to use under the MIT License.

Stay awake. Stay awesome.
