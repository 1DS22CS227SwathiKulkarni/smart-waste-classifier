# Smart Waste Classifier using Keras, OpenCV & cvzone

This project is a **real-time waste classification system** using a webcam feed, powered by a trained **Keras model (`keras_model.h5`)**, **OpenCV**, and the **cvzone** overlay library. It helps automate waste sorting by identifying objects and visually guiding users to dispose of them in the correct bin — such as food, hazardous, recyclable, or residual.

---

## Features

- Real-time classification of waste from webcam input  
- Uses a custom-trained Keras `.h5` model (from Teachable Machine or similar)  
- Automatically matches waste item to the correct bin  
- Visual overlays of item, arrow, and bin on a background UI  
- Modular and easy to extend (add more classes, change models)  

---

## Project Structure

```
smart-waste-classifier/
├── Resources/
│   ├── Model/
│   │   ├── keras_model.h5       # Trained classification model
│   │   └── labels.txt           # Class labels
│   ├── Waste/                   # PNG images of detected waste items
│   ├── Bins/                    # PNG images of bin types
│   ├── arrow.png                # Arrow indicator image
│   └── background.png           # GUI background template
├── main.py                      # Main Python script for classification
├── requirements.txt             # Required Python packages
└── README.md                    # This file
```

---

## How It Works

1. Webcam captures a frame using OpenCV.  
2. The image is passed into the pre-trained Keras model (`keras_model.h5`).  
3. The class is predicted using `cvzone.ClassificationModule`.  
4. Based on the class:
   - A waste image is shown in the top-right corner.
   - An arrow points to the correct bin.
   - The corresponding bin image is shown on the bottom-right.  
5. The processed frame is shown on top of a background layout.

---

## Waste-to-Bin Mapping

The class prediction returned by the model is mapped to a bin using the following dictionary in `main.py`:

```python
classDic = {
    0: None,
    1: 0,  # ziptopcans → Recyclable
    2: 0,  # newspaper → Recyclable
    3: 3,  # oldshoes → Residual
    4: 3,  # watercolorpen → Residual
    5: 1,  # disinfectant → Hazardous
    6: 1,  # battery → Hazardous
    7: 2,  # vegetableleaf → Food
    8: 2   # apple → Food
}
```

| Class ID | Waste Item       | Bin Type     |
|----------|------------------|--------------|
| 1        | Ziptop Cans      | Recyclable   |
| 2        | Newspaper        | Recyclable   |
| 3        | Old Shoes        | Residual     |
| 4        | Watercolor Pen   | Residual     |
| 5        | Disinfectant     | Hazardous    |
| 6        | Battery          | Hazardous    |
| 7        | Vegetable Leaf   | Food         |
| 8        | Apple            | Food         |

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/1DS22CS227SwathiKulkarni/smart-waste-classifier.git
cd smart-waste-classifier
```

### 2. Create Virtual Environment (Optional)

```bash
python -m venv venv
# Activate:
# Windows
venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

> Make sure to use `cvzone` version **1.5.6** as used in this project.

If you don’t have a `requirements.txt`, create one with:

```
opencv-python
cvzone==1.5.6
numpy
```

---

## Run the App

Ensure your webcam is working, then:

```bash
python main.py
```

The webcam feed will display with the classification output and corresponding visual overlays.

---

## Train Your Own Model

This project uses a `.h5` model trained via [Teachable Machine by Google](https://teachablemachine.withgoogle.com/) or any custom-trained Keras image classifier.

**Steps to integrate your model:**
- Export your model in `.h5` format.
- Copy it to `Resources/Model/keras_model.h5`
- Ensure `labels.txt` contains class names in the same order used during training.
- Add matching PNG images in `Resources/Waste/` and `Resources/Bins/`.

---

## Extending the Project

You can add more functionality like:
- Sound alerts for incorrect disposal  
- Flask/FastAPI interface for web deployment  
- Mobile/Jetson Nano version using TensorFlow Lite  
- Database/log storage of classified waste items  
- Integration with smart dustbins or robotic arms  

---

## Author

**Swathi Kulkarni**  
B.E Computer Science  
GitHub: [@1DS22CS227SwathiKulkarni](https://github.com/1DS22CS227SwathiKulkarni)

---

## Feedback

Feel free to open an issue or contribute via pull requests if you want to improve the accuracy, extend the features, or integrate new components!
