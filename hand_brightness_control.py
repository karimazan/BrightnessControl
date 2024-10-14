import cv2
import mediapipe as mp
import math
import screen_brightness_control as sbc

# Initialize MediaPipe Hands and Drawing utilities
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

# Function to calculate the distance between two points
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Maximum distance for brightness control
MAX_DISTANCE = 200 
previous_brightness = None

# Start hand tracking
with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        # Capture frame-by-frame
        success, image = cap.read()
        if not success:
            print("Error capturing image.")
            break

        # Convert the image from BGR to RGB
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image_rgb)

        # If hands are detected
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks on the image
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Get the positions of thumb and index finger tips
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

                # Convert normalized coordinates to pixel values
                thumb_x, thumb_y = int(thumb_tip.x * image.shape[1]), int(thumb_tip.y * image.shape[0])
                index_x, index_y = int(index_tip.x * image.shape[1]), int(index_tip.y * image.shape[0])

                # Calculate distance between thumb and index finger
                distance = calculate_distance(thumb_x, thumb_y, index_x, index_y)
                screen_brightness = max(0, min(int((distance / MAX_DISTANCE) * 100), 100))

                # Adjust screen brightness if the change is significant
                if previous_brightness is None or abs(previous_brightness - screen_brightness) > 5:
                    sbc.set_brightness(screen_brightness)
                    previous_brightness = screen_brightness
                    print(f"Brightness set to: {screen_brightness}%")

                # Draw circles around the thumb and index finger
                cv2.circle(image, (thumb_x, thumb_y), 10, (0, 0, 255), -1)
                cv2.circle(image, (index_x, index_y), 10, (255, 255, 0), -1)

                # Draw a line between the thumb and index finger
                cv2.line(image, (thumb_x, thumb_y), (index_x, index_y), (255, 0, 255), 3)

                # Display current brightness and distance
                cv2.putText(image, f'Brightness: {screen_brightness}%', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                cv2.putText(image, f'Distance: {int(distance)} pixels', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Show the image with hand tracking
        cv2.imshow('Brightness Control by Hand Tracking', image)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

# Release resources and close windows
cap.release()
cv2.destroyAllWindows()
