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

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PicEnhance - Image Background Remover</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        h1, h2 {
            color: #333;
        }
        pre {
            background: #333;
            color: #fff;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        code {
            color: #ffcc00;
        }
    </style>
</head>
<body>

    <h1>🚀 PicEnhance - Image Background Remover</h1>
    <p>PicEnhance is a Python-based tool that removes backgrounds from images and enhances their quality.</p>

    <h2>📥 Clone the Repository</h2>
    <p>Use Git to clone the repository:</p>
    <pre><code>git clone https://github.com/yourusername/PicEnhance.git
cd PicEnhance</code></pre>

    <h2>🛠️ Create a Virtual Environment (Optional)</h2>
    <p>To avoid package conflicts, create a virtual environment:</p>
    <pre><code>python -m venv env</code></pre>
    
    <h3>Activate the Virtual Environment:</h3>
    <p><strong>Windows:</strong></p>
    <pre><code>env\Scripts\activate</code></pre>
    
    <p><strong>Mac/Linux:</strong></p>
    <pre><code>source env/bin/activate</code></pre>

    <h2>📦 Install Dependencies</h2>
    <p>Run the following command to install the required Python packages:</p>
    <pre><code>pip install rembg pillow onnxruntime</code></pre>

    <h2>📂 Folder Structure</h2>
    <pre><code>PicEnhance/
│── input/      (Folder containing original images)
│── output/     (Folder where processed images are saved)
│── BGRemover.py (Python script)
│── README.md   (This file)</code></pre>

    <h2>💡 Usage</h2>
    <p>1️⃣ Place images in the <code>input/</code> folder.</p>
    <p>2️⃣ Run the script using:</p>
    <pre><code>python BGRemover.py</code></pre>
    <p>3️⃣ Processed images will be saved in the <code>output/</code> folder.</p>

    <h2>❓ Troubleshooting</h2>
    <p><strong>ModuleNotFoundError: No module named 'rembg'</strong></p>
    <pre><code>pip install rembg</code></pre>

    <p><strong>ModuleNotFoundError: No module named 'onnxruntime'</strong></p>
    <pre><code>pip install onnxruntime</code></pre>

    <p><strong>cv2.imshow Error in OpenCV</strong></p>
    <pre><code>pip install opencv-python-headless</code></pre>

    <h2>📄 License</h2>
    <p>This project is licensed under the <strong>MIT License</strong>.</p>

    <h2>🤝 Contributing</h2>
    <p>Feel free to submit pull requests or open issues to improve this project!</p>

    <h2>📩 Contact</h2>
    <p>For any questions, reach out at <strong>your-email@example.com</strong>.</p>

    <p>🚀 <strong>Enjoy hassle-free background removal!</strong> 🎨✨</p>

</body>
</html>
