import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

# Camera check
if not cap.isOpened():
    print("Camera open nahi ho raha!")
    exit()

# -------------------------
# STEP 1: BACKGROUND CAPTURE
# -------------------------

print("Background capture hone wala hai...")
print("Camera ke saamne se hat jao!")

start_time = time.time()

while True:

    ret, frame = cap.read()

    if not ret:
        print("Camera frame nahi mil raha!")
        break

    frame = cv2.flip(frame, 1)

    # Countdown
    elapsed = int(time.time() - start_time)
    remaining = 5 - elapsed

    if remaining > 0:

        cv2.putText(
            frame,
            "PLEASE MOVE AWAY",
            (120, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "Background in: " + str(remaining),
            (150, 130),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

        cv2.imshow("Invisible Cloak", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            exit()

    else:

        # Capture clean background
        background = frame.copy()
        break

# -------------------------
# STEP 2: CLOAK DETECTION
# -------------------------

print("Background captured!")
print("Ab white cloth camera ke saamne lao.")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    # HSV conversion
    hsv = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2HSV
    )

    # White color
    lower_white = np.array([0, 0, 120])
    upper_white = np.array([180, 100, 255])

    mask = cv2.inRange(
        hsv,
        lower_white,
        upper_white
    )

    # Clean mask
    kernel = np.ones(
        (7, 7),
        np.uint8
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        kernel
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_CLOSE,
        kernel
    )

    # Smooth edges
    mask = cv2.GaussianBlur(
        mask,
        (7, 7),
        0
    )

    # Background at white-cloth area
    cloak_area = cv2.bitwise_and(
        background,
        background,
        mask=mask
    )

    # Everything except white cloth
    inverse_mask = cv2.bitwise_not(mask)

    normal_area = cv2.bitwise_and(
        frame,
        frame,
        mask=inverse_mask
    )

    # Final result
    result = cv2.add(
        cloak_area,
        normal_area
    )

    cv2.putText(
        result,
        "WHITE CLOAK",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        result,
        "Press Q to quit",
        (20, 75),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    cv2.imshow(
        "Invisible Cloak - Final",
        result
    )

    # Q = quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()