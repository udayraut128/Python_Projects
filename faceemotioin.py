import cv2
from deepface import DeepFace

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not access webcam")
        break

    try:
        # Analyze face emotion
        result = DeepFace.analyze(
            frame,
            actions=["emotion"],
            enforce_detection=False
        )

        # DeepFace can return a list
        if isinstance(result, list):
            result = result[0]

        # Get dominant emotion
        emotion = result["dominant_emotion"]

        # Get emotion confidence
        emotions = result["emotion"]
        confidence = emotions[emotion]

        # Display result
        text = f"Emotion: {emotion} ({confidence:.1f}%)"

        cv2.putText(
            frame,
            text,
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2
        )

    except Exception as e:
        cv2.putText(
            frame,
            "No face detected",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 0, 255),
            2
        )

    # Show webcam
    cv2.imshow("Face Emotion Detection", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()