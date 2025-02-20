# PicEnhance - Image Background Remover & Enhancer

PicEnhance is a Python-based tool that removes backgrounds from images and enhances them by reducing noise and improving color quality. It uses the `rembg` library for background removal and `PIL` for image processing.

---

## 🚀 Features
- Automatically removes backgrounds from images.
- Processes multiple images in a folder.
- Saves the edited images in an output directory.
- Handles `.png`, `.jpg`, and `.jpeg` image formats.

---

## 🛠️ Installation Guide

### **1️⃣ Install Python**
Ensure Python is installed. Check using:
```bash
python --version

Here is your **README.md** file with HTML formatting for GitHub:  

---

### **📄 README.md**
```markdown
# 🚀 PicEnhance - Image Background Remover & Enhancer

PicEnhance is a Python-based tool that removes backgrounds from images and enhances their quality.

---

## 📥 Clone the Repository
Use Git to clone the repository:
```bash
git clone https://github.com/yourusername/PicEnhance.git
cd PicEnhance
```

---

## 🛠️ Create a Virtual Environment (Optional)
To avoid package conflicts, create a virtual environment:
```bash
python -m venv env
```

### **Activate the Virtual Environment**
#### **Windows:**
```bash
env\Scripts\activate
```
#### **Mac/Linux:**
```bash
source env/bin/activate
```

---

## 📦 Install Dependencies
Run the following command to install the required Python packages:
```bash
pip install rembg pillow onnxruntime
```

---

## 📂 Folder Structure
```
PicEnhance/
│── input/      (Folder containing original images)
│── output/     (Folder where processed images are saved)
│── BGRemover.py (Python script)
│── README.md   (This file)
```

---

## 💡 Usage
1️⃣ Place images in the `input/` folder.  
2️⃣ Run the script using:
```bash
python BGRemover.py
```
3️⃣ Processed images will be saved in the `output/` folder.

---

## ❓ Troubleshooting
### **ModuleNotFoundError: No module named 'rembg'**
```bash
pip install rembg
```

### **ModuleNotFoundError: No module named 'onnxruntime'**
```bash
pip install onnxruntime
```

### **cv2.imshow Error in OpenCV**
If OpenCV GUI functions fail, install:
```bash
pip install opencv-python-headless
```

---

## 📄 License
This project is licensed under the **MIT License**.

---

## 🤝 Contributing
Feel free to submit pull requests or open issues to improve this project!

---

## 📩 Contact
For any questions, reach out at **your-email@example.com**.

---

🚀 **Enjoy hassle-free background removal!** 🎨✨
```

### **How to Use This README File**
1. Save this content in a file named **README.md**.
2. Upload it to your GitHub repository.
3. It will be displayed on your repository’s homepage.

This **README.md** provides clear instructions and troubleshooting tips. Let me know if you need modifications! 🚀😊
