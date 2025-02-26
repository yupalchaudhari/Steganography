# **Steganography Image Encryption & Decryption**
A simple **steganography tool** that hides a **secret message** inside an image by modifying pixel values. It supports **password protection** and works with **all image formats** by converting them to **PNG** before encryption.

---

## **Features**
✅ Supports **any image format** (JPG, PNG, BMP, etc.)  
✅ Converts images to **PNG** to ensure lossless encryption  
✅ **Password protection** for message security  
✅ Uses **full pixel channel modification** instead of traditional LSB steganography  
✅ Ensures **message integrity** with a termination marker  
✅ **Efficient compression** to avoid excessive file size increase  

---

## **Installation**
### **🔹 Requirements**
Ensure you have **Python 3.x** and required libraries installed.

```bash
pip install opencv-python
```

### **🔹 Libraries Used**
- **OpenCV (`cv2`)** - For image processing  
- **OS (`os`)** - For file handling and execution  

---

## **Usage**
### **1️⃣ Encrypt a Message into an Image**
Run the `1_Encrypt.py` script:

```bash
python 1_Encrypt.py
```

📌 **Inputs:**  
- **Image Path:** Provide any image (JPG, PNG, BMP, etc.)  
- **Secret Message:** Enter the message to hide  
- **Passcode:** Set a password for decryption  

📌 **Output:**  
- An encrypted image `your_encrypted_image.png` will be created.  

---

### **2️⃣ Decrypt the Message from an Image**
Run the `2_Decrypt.py` script:

```bash
python 2_Decrypt.py
```

📌 **Inputs:**  
- The encrypted image (`your_encrypted_image.png`)  
- The correct passcode  

📌 **Output:**  
- If the password is correct, the **hidden message is revealed**.  
- If the password is wrong, access is **denied**.  

---

## **How It Works**
### **🔹 Encryption Method**
This method **modifies the entire pixel channel values** instead of using traditional **Least Significant Bit (LSB) steganography**.  

📌 **Key Differences from LSB Steganography:**  
✅ **Modifies full pixel values**, storing ASCII values directly in RGB channels.  
✅ **More resistant to compression** than LSB (useful for PNG images).  
✅ **Easier to extract** using direct pixel value retrieval.  

📌 **Steps:**  
1. **Convert image to PNG** (if not already).  
2. **Store password length** in the first pixel `(0,0,0)`.  
3. **Store password** by modifying pixel values sequentially.  
4. **Encode the message** in pixels across the image.  
5. **Add a termination marker (`null byte`)** to signal the end of the message.  

---

### **🔹 Decryption Process**
1. **Extract password length** from `(0,0,0)`.  
2. **Retrieve stored password** and compare it with user input.  
3. If the **password matches**, extract the **hidden message** until the termination marker.  

---

## **Limitations**
⚠️ **JPEG images expand in size** due to loss of compression. Use PNG for best results.  
⚠️ **Only short messages** should be stored in small images to avoid distortions.  

---

## **Contributors**
👨‍💻 **Yupal_Chaudhari**  
Feel free to contribute and improve this project! 🚀

