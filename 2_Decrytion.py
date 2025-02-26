import cv2 #type:ignore
import os

def decrypt_message(image_path):
    img = cv2.imread(image_path) 
    if img is None:
        print("Error: Image not found!")
        return

    png_image_path = "your_encrypted_image.png"
    cv2.imwrite(png_image_path, img)
    img = cv2.imread(png_image_path, cv2.IMREAD_UNCHANGED)

    c = {i: chr(i) for i in range(256)}

    password_length = img[0, 0, 0]
    stored_password = ""
    n, m, z = 0, 1, 0
    for _ in range(password_length):
        stored_password += c[img[n, m, z]]
        m += 1
        if m >= img.shape[1]:
            m, n = 0, n + 1
        z = (z + 1) % 3

    input_password = input("Enter passcode for decryption: ")

    if stored_password == input_password:
        print("Password correct! Decrypting message...")
        message = ""
        while True:
            char_value = img[n, m, z]
            if char_value == 0: 
                break
            message += c[char_value]
            m += 1
            if m >= img.shape[1]:
                m, n = 0, n + 1
            z = (z + 1) % 3

        print("Decrypted message:", message)
    else:
        print("YOU ARE NOT AUTHORIZED")

if __name__ == "__main__":
    image_path = "your_encrypted_image.png"  
    decrypt_message(image_path)
