
# Blood Group Detection Using Image Processing and Fingerprint

## 📌 Overview
This project presents an innovative **deep learning-based system** for blood group detection using **two distinct methods**:  
1. **Blood Image Analysis** – Traditional blood group detection using blood sample images.  
2. **Fingerprint Image Classification** – A novel, non-invasive approach to predict blood group from fingerprint patterns.  

The system is built using **Python**, **Flask**, **HTML**, **CSS**, and **JavaScript**, with **MobileNetV2** as the backbone deep learning model.

---

## 🚀 Features
- **Dual Detection Modes**: Blood image-based and fingerprint image-based detection.
- **Non-Invasive Method**: Fingerprint-based detection eliminates the need for blood samples.
- **High Accuracy**:
  - Blood images: **100% training & validation accuracy**
  - Fingerprints: **94% training & 90% validation accuracy**
- **Web-Based Interface** for easy access and real-time results.
- **Portable & Scalable** for integration in healthcare systems.

---

## 🛠 Tech Stack
- **Backend**: Python, Flask  
- **Frontend**: HTML, CSS, JavaScript  
- **Deep Learning**: TensorFlow/Keras, MobileNetV2  
- **Dataset Sources**:
  - Blood images dataset: 750 samples  
  - Fingerprint images dataset: 10,477 samples  

---

## 📂 Project Structure
```
BloodGroupDetection/
│── dataset/
│   ├── blood_images/
│   ├── fingerprints/
│── static/
│   ├── css/
│   ├── js/
│── templates/
│   ├── index.html
│── model/
│   ├── blood_model.h5
│   ├── fingerprint_model.h5
│── app.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/BloodGroupDetection.git
   cd BloodGroupDetection
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

---

## 📊 System Workflow
1. **Image Input** – Blood sample or fingerprint image is uploaded.  
2. **Preprocessing** – Image resized, normalized, and augmented.  
3. **Feature Extraction** – MobileNetV2 extracts deep features.  
4. **Classification** – Model predicts blood group (A-, A+, AB-, AB+, B-, B+, O-, O+).  
5. **Result Display** – Prediction shown on web interface.

---

## 📈 Results
- **Blood Images**: 100% accuracy on test and validation sets.
- **Fingerprints**: 94% training accuracy, 90% validation accuracy.
- **Fast Processing**: Real-time prediction within seconds.

---

## 🔮 Future Enhancements
- Mobile application for field use.
- Additional biometric methods (e.g., iris scan).
- Integration with hospital databases for automated patient record updates.
- Real-time image capture through the web interface.

---

## 📜 References
- [MobileNetV2 Paper](https://arxiv.org/abs/1801.04381)
- [Kaggle Blood Dataset](https://www.kaggle.com/datasets/jayaprakashpondy/blood-dataset)

---

## 👨‍💻 Authors
- Shaik Sameera  
- Kampasati Prakash  
- Kanchu Ramesh  
- Tappetla Keerthisri  

Under the guidance of **Mr. A. Srinivas Rao**  
Sai Spurthi Institute of Technology
