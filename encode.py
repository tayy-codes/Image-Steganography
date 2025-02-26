import cv2
import os

# Function to encode a message into an image
def encode_image(image_path, secret_message, password):
    try:
        if not os.path.isfile(image_path):
            print("Error: File not found. Please check the filename and try again.")
            return

        img = cv2.imread(image_path)  # Read the image

        if img is None:
            print("Error: The file is not a valid image.")
            return

        rows, cols, _ = img.shape  # Get image dimensions

        # Append a termination character (~) to signal the end of the message
        secret_message += "~"

        if len(secret_message) > rows * cols:
            print("Error: Message is too long for this image. Try a larger image.")
            return

        # Encode the message into image pixels
        index = 0
        for i in range(rows):
            for j in range(cols):
                if index < len(secret_message):
                    img[i, j, 0] = ord(secret_message[index])  # Store ASCII in Blue channel
                    index += 1
                else:
                    break  # Stop encoding when message is fully stored

        # Save the encoded image
        encoded_image_path = "encrypted_image.png"
        cv2.imwrite(encoded_image_path, img)
        print(f"Message encoded successfully! Saved as '{encoded_image_path}'")

    except Exception as e:
        print("Error:", e)

# User input
image_path = input("Enter the image filename (with extension): ")
if image_path.strip() == "":
    print("Error: No filename provided.")
else:
    message = input("Enter the secret message: ")
    password = input("Enter a password for decoding: ")  # Currently unused but can be added for security

    encode_image(image_path, message, password)