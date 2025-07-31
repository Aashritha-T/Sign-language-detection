# 🖐️ Sign Language Detection Using Machine Learning
A machine learning project that identifies American Sign Language (ASL) alphabets (A–Z) from hand gesture images. Designed with the vision to bridge the communication gap between the speech/hearing impaired and the rest of the world through computer vision and AI.

## 📌 Table of Contents

- [📌 Table of Contents](#-table-of-contents)
- [🚀 Project Overview](#-project-overview)
- [📂 Dataset](#-dataset)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Model Training & Evaluation](#-model-training--evaluation)
- [💻 How to Run Locally](#-how-to-run-locally)
- [🧠 Future Scope](#-future-scope)
- [🙌 Acknowledgements](#-acknowledgements)
- [👩‍💻 Author](#-author)

## 🚀 Project Overview

This project uses machine learning and image classification techniques to recognize static hand gestures representing the 26 English alphabets in ASL. It helps translate visual signs into textual output, promoting inclusivity and accessibility.

> 🧠 **Why this matters:**  
> Communication barriers can isolate individuals with hearing impairments. This project is a step toward building assistive tech that empowers communication for all.

## 📂 Dataset

- The dataset consists of **thousands of labeled images** representing the alphabets A to Z.
- Each class (A–Z) contains images of hand gestures in varying lighting, angles, and skin tones to ensure model robustness.
- Preprocessing includes:
  - Grayscale conversion
  - Resizing (e.g., 64x64 or 128x128)
  - Normalization
---

##  Sample Output

Hand gesture - alphabet-accuracy

## 🛠️ Tech Stack

- Language: Python  
- Libraries/Frameworks:
  - Scikit-learn / TensorFlow / Keras  
  - NumPy, Pandas  
  - OpenCV (for image preprocessing)  
  - Matplotlib / Seaborn (for visualization)  

## 📈 Model Training & Evaluation

- **Model Used:** [e.g., CNN, SVM, Random Forest]  
- **Training Accuracy:** ~[85]%  
- **Testing Accuracy:** ~[80]%  
- **Confusion Matrix & Classification Report** to evaluate per-class performance.

## 💻 How to Run Locally

### 🔧 Prerequisites

Make sure Python 3.7+ is installed.

```bash
pip install -r requirements.txt
````

### 🚦 Training the Model

```bash
python train.py
```

### 📤 Predicting on Test Images

```bash
python predict.py --image path_to_image.jpg
```

### 🎥 (Optional) Real-time Webcam Detection

```bash
python realtime_detection.py
```

---

## 🧠 Future Scope

* ✨ Add dynamic gestures (words/sentences)
* 🌐 Build a web app or mobile app for real-time detection
* 📱 Integrate with voice assistant or text-to-speech
* 🇮🇳 Extend support to Indian or other regional sign languages.

## 👩‍💻 Author

**Aashritha Thirunahari**
Aspiring ML Developer | Passionate about AI for social good
[GitHub](https://github.com/Aahritha-T) | [LinkedIn](https://linkedin.com/in/thiruaashritha)

> 💬 *“Technology is most powerful when it empowers everyone.”*
> — Tim Cook

⭐ If you found this project interesting, give it a star!
📬 Feel free to open issues or contribute with pull requests.

