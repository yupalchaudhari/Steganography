import cv2 #type:ignore
import os

def encrypt_message(image_path, message, password):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return

    png_image_path = "your_encrypted_image.png"
    cv2.imwrite(png_image_path, img)
    img = cv2.imread(png_image_path, cv2.IMREAD_UNCHANGED)

    d = {chr(i): i for i in range(256)}

    img[0, 0, 0] = len(password)

    n, m, z = 0, 1, 0
    for char in password:
        img[n, m, z] = d[char]
        m += 1
        if m >= img.shape[1]:
            m, n = 0, n + 1
        z = (z + 1) % 3

    for char in message:
        img[n, m, z] = d[char]
        m += 1
        if m >= img.shape[1]:
            m, n = 0, n + 1
        z = (z + 1) % 3

    img[n, m, z] = 0  

    cv2.imwrite("your_encrypted_image.png", img)
    print("Message encrypted successfully in 'your_encrypted_image.png'.")

if __name__ == "__main__":
    image_path = "high_resolution_img.png"  # if the error say: can't find your_encrypted_image than change this path to relative path 
    message = input("Enter secret message: ") # because in vs code it only open if all things are in same folder ...
    password = input("Enter passcode: ")
    print("Please wait for few seconds...")
    encrypt_message(image_path, message, password)
    os.system("start your_encrypted_image.png")
