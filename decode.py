import cv2
import os

def decode_image(encoded_image_path, password):
    try:
        # Check if file exists
        if not os.path.isfile(encoded_image_path):
            print("Error: File not found. Please check the filename and try again.")
            return

        img = cv2.imread(encoded_image_path, cv2.IMREAD_UNCHANGED)  # Read image without modifications

        if img is None:
            print("Error: The file is not a valid image.")
            return

        # Get password input
        user_password = input("Enter the password to decode: ")

        if user_password != password:
            print("Error: Incorrect password! Access denied.")
            return

        # Extract message from the Blue channel
        extracted_message = ""
        rows, cols, _ = img.shape

        found_terminator = False  # Flag to break all loops when "~" is found

        for i in range(rows):
            for j in range(cols):
                char = chr(img[i, j, 0])  # Read from Blue channel
                if char == "~":  # Stop at the termination character
                    found_terminator = True
                    break
                extracted_message += char
            if found_terminator:
                break  # Stop the outer loop as well

        print("\nDecoded Message:", extracted_message)

    except Exception as e:
        print("Error:", e)

# User input
encoded_image_path = input("Enter the encoded image filename (with extension): ")
if encoded_image_path.strip() == "":
    print("Error: No filename provided.")
else:
    original_password = "Python123"  # Ensure this matches the one used in encoding
    decode_image(encoded_image_path, original_password)