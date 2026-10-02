import cv2 as cv
import mediapipe as mp
from mediapipe.python.solutions.hands import HandLandmark
from mediapipe.python.solutions.drawing_utils import DrawingSpec

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

custom_style = mp_drawing_styles.get_default_hand_landmarks_style()

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Error: Camera open failed")
    exit()

unused_landmarks = [
    HandLandmark.WRIST,
    HandLandmark.THUMB_CMC,
    HandLandmark.THUMB_IP,
    HandLandmark.THUMB_MCP,
    HandLandmark.THUMB_TIP,
    HandLandmark.INDEX_FINGER_MCP,
    HandLandmark.MIDDLE_FINGER_MCP,
    HandLandmark.RING_FINGER_MCP,
    HandLandmark.PINKY_MCP
]

for landmark in unused_landmarks:
    custom_style[landmark] = DrawingSpec(color=(255,255,0), thickness=None, circle_radius = 0)

period = 0
with mp_hands.Hands(
    min_detection_confidence = 0.9,
    model_complexity = 1,
    static_image_mode=False,
    max_num_hands=1) as hands:
    
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Error: Frame reception failed")
            exit()
        
        input = cv.cvtColor(image, cv.COLOR_BGR2RGB)
#         image = cv.flip(image, 1)
        results = hands.process(input)
        
        image_height, image_width, _ = image.shape
        
        cv.rectangle(image, (400, 75), (600, 225), (255, 0, 0), 2)
            
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                
                index_x =round(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width, 2)
                index_y = round(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height, 2)
                middle_x = round(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].x * image_width, 2)
                middle_y = round(hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y * image_height, 2)
                ring_x = round(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].x * image_width, 2)
                ring_y = round(hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y * image_height, 2)
                pinky_x = round(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].x * image_width, 2)
                pinky_y = round(hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y * image_height, 2)
                
                index_fret = -1;
                middle_fret = -1;
                ring_fret = -1;
                pinky_fret = -1;
                
                period += 1
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    landmark_drawing_spec=custom_style)
                if (period >= 100):
#                     print(
#                          f'Index finger tip coordinates: ',
#                          f'({index_x}',
#                          f'{index_y})\n')
                    if (index_y > 85 and index_y < 105):
                        index_fret = 1;
#                         print("high E")
                    elif (index_y > 105 and index_y < 125):
                        index_fret = 2;
#                         print("A")
                    elif (index_y > 140 and index_y < 160):
                        index_fret = 3;
#                         print("D")
                    elif (index_y > 160 and index_y < 175):
                        index_fret = 4;
#                         print("G")
                    elif (index_y > 180 and index_y < 200):
                        index_fret = 5;
#                         print("B")
                    elif (index_y > 200 and index_y < 250):
                        index_fret = 6;
#                         print("low E")
                        
                    if (middle_y > 85 and middle_y < 105):
                        middle_fret = 1;
#                         print("high E")
                    elif (middle_y > 105 and middle_y < 125):
                        middle_fret = 2;
#                         print("A")
                    elif (middle_y > 140 and middle_y < 160):
                        middle_fret = 3;
#                         print("D")
                    elif (middle_y > 160 and middle_y < 175):
                        middle_fret = 4;
#                         print("G")
                    elif (middle_y > 180 and middle_y < 200):
                        middle_fret = 5;
#                         print("B")
                    elif (middle_y > 200 and middle_y < 250):
                        middle_fret = 6;
#                         print("low E")
                        
                    if (ring_y > 85 and ring_y < 105):
                        ring_fret = 1;
#                         print("high E")
                    elif (ring_y > 105 and ring_y < 125):
                        ring_fret = 2;
#                         print("A")
                    elif (ring_y > 140 and ring_y < 160):
                        ring_fret = 3;
#                         print("D")
                    elif (ring_y > 160 and ring_y < 175):
                        ring_fret = 4;
#                         print("G")
                    elif (ring_y > 180 and ring_y < 200):
                        ring_fret = 5;
#                         print("B")
                    elif (ring_y > 200 and ring_y < 250):
                        ring_fret = 6;
                    
                    if (pinky_y > 85 and pinky_y < 105):
                        index_fret = 1;
#                         print("high E")
                    elif (pinky_y > 105 and pinky_y < 125):
                        index_fret = 2;
#                         print("A")
                    elif (pinky_y > 140 and pinky_y < 160):
                        index_fret = 3;
#                         print("D")
                    elif (pinky_y > 160 and pinky_y < 175):
                        index_fret = 4;
#                         print("G")
                    elif (pinky_y > 180 and pinky_y < 200):
                        index_fret = 5;
#                         print("B")
                    elif (pinky_y > 200 and pinky_y < 250):
                        index_fret = 6;
                    
                    if (index_fret + middle_fret + ring_fret + pinky_fret > -3):
                        print(f'{index_fret}', f'{middle_fret}', f'{ring_fret}', f'{pinky_fret}\n')
                    
                    if (index_fret == 2 and middle_fret == 4 and ring_fret == 5):
                        print("C\n");
                    if (index_fret >= 5 and middle_fret >= 5 and ring_fret >= 5):
                        print("D\n");
                    if (index_fret == 3 and middle_fret == 2):
                        print("E\n");
                    if (index_fret == 2 and middle_fret == 3 and ring_fret == 4):
                        print("F\n");
                    if ((index_fret == 3 or index_fret == 4) and (middle_fret == 2 or middle_fret == 1)):
                        print("G\n");
                    if ((index_fret == 3 or index_fret == 4) and (middle_fret == 3 or middle_fret == 4) and ring_fret == 2):
                        print("A\n");
                    if (index_fret == 5 and middle_fret == 4 and ring_fret == 3 and pinky_fret == 2):
                        print("B\n");
                    period = 0
#                      
#                          f'Middle finger tip coordinates: ',
#                          f'({middle_x}',
#                          f'{middle_y})\n'
#                         
#                          f'Ring finger tip coordinates: ',
#                          f'({ring_x}',
#                          f'{ring_y})\n'
#                          
# 
#                          f'Pinky finger tip coordinates: ',
#                          f'({pinky_x}',
#                          f'{pinky_y})\n\n'
#                     )
                    
                    

        cv.imshow('Chord-Detector', cv.flip(image, 1))
        
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv.destroyAllWindows()