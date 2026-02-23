 Smart Exam Proctoring System



 1. Problem Statement



With the rapid growth of online examinations, maintaining academic integrity has become a major challenge. 

Traditional invigilation methods are not feasible in remote settings, making online exams vulnerable to:



\- Impersonation

\- Multiple person presence

\- Use of unauthorized objects (mobile phones, books, etc.)

\- Leaving the screen during the exam



This project aims to design and implement an AI-based Smart Exam Proctoring System that automatically monitors candidate behavior using computer vision and flags suspicious activities.



---



 2. System Architecture



The system follows a modular pipeline-based architecture:



1\. Video Upload Interface (Flask Web App)

2\. Error Validation Layer

3\. Frame Extraction (OpenCV)

4\. Face Detection (Haarcascade)

5\. Person Detection (YOLOv8)

6\. Forbidden Object Detection (YOLOv8)

7\. Behavior Analysis Engine

8\. Risk Scoring Module

9\. Evidence Storage

10\. Report Generation



Each task is implemented in a separate module under the `src` directory for clean structure and maintainability.



---



\## 🔍 3. Detection Logic



\### 🔹 Frame Extraction

Video frames are captured using OpenCV’s `VideoCapture`.



\### 🔹 Face Monitoring

Haarcascade model detects faces in each frame.

\- If no face detected → flagged as suspicious

\- If multiple faces detected → flagged as high risk



\### 🔹 Person Counting

YOLOv8 detects number of persons in frame.

\- More than 1 person → violation



\### 🔹 Forbidden Object Detection

YOLOv8 model identifies objects like:

\- Mobile phones

\- Books (if trained class available)



\### 🔹 Behavior Logic

Suspicious events are triggered when:

\- Face not visible for continuous frames

\- Multiple persons detected

\- Unauthorized object detected



Each event increases a cumulative risk score.


4. Major Challenges Faced \& How They Were Solved



\###1️⃣ Folder Structure \& Import Errors



\*\*Problem:\*\*  

Python modules inside `src` were not importing correctly.



\*\*Solution:\*\*  

Reorganized project structure properly and ensured execution from root directory. Used relative imports carefully.



---



\### 2️⃣ Nested `src` Folder Issue



\*\*Problem:\*\*  

Files were accidentally being pasted inside another `src` folder, causing import conflicts.



\*\*Solution:\*\*  

Cleaned directory structure and understood how current working directory affects imports.



---



\### 3️⃣ Application Crashing on Invalid Video Files



\*\*Problem:\*\*  

When a corrupted or fake `.mp4` file was uploaded, OpenCV threw errors like:



```

moov atom not found

```



The Flask app crashed with:

```

ERR\_CONNECTION\_RESET

```



\*\*Solution:\*\*  

Implemented a backend error handling module that:

\- Validates video before processing

\- Detects corrupted files

\- Safely returns error message using `error.html`

\- Prevents server crash



This significantly improved system stability.



---



\### 4️⃣ TemplateNotFound Error



\*\*Problem:\*\*  

After implementing error handling, Flask crashed because `error.html` did not exist.



\*\*Solution:\*\*  

Created proper template file inside `templates/` directory and ensured Flask rendering worked correctly.



---



\### 5️⃣ GitHub Large File Rejection



\*\*Problem:\*\*  

YOLO model file (`.pt`) exceeded GitHub size limits.



\*\*Solution:\*\*  

Created `.gitignore` to exclude:

\- Model files

\- \_\_pycache\_\_

\- Virtual environment

\- Logs



Improved repository cleanliness and professionalism.


\## 5. Error Handling \& Validation



The system includes a backend validation layer that:

\- Detects corrupted or non-video files

\- Prevents OpenCV crashes

\- Returns user-friendly error messages

\- Maintains server stability



This ensures robustness and production-level reliability.



---



\## 6. Technologies Used



\- Python

\- Flask

\- OpenCV

\- YOLOv8 (Ultralytics)

\- Haarcascade

\- HTML/CSS

\- Git \& GitHub


\## 7. Key Learning Outcomes



\- Modular project structuring

\- Backend error handling

\- Debugging Flask applications

\- Managing large ML models

\- Git version control best practices

\- Writing professional documentation

## 8. Project structure

smart_exam_proctoring/
│
├── static/
│   ├── uploads/
│   ├── evidence/
│
├── docs/
│   └── screenshots/
│
├── data/
├── models/
├── app.py
├── requirements.txt
└── README.md

🧠 9. How It Works

User uploads exam video.

Frames are processed using YOLOv8 model.

Suspicious objects/behaviors are detected.

Evidence images are automatically saved.

Web interface displays results.

🎯 10. Use Cases

Online university exams

Remote certification tests

Competitive exam monitoring

Classroom AI surveillance

\## 11. Key Learning Outcomes



\- Modular project structuring

\- Backend error handling

\- Debugging Flask applications

\- Managing large ML models

\- Git version control best practices

\- Writing professional documentation

\## 12. Limitations



\- Works only on recorded video (not live streaming)

\- Accuracy depends on lighting conditions

\- YOLO model limited to available trained classes

\- No real-time alert system

\- No database integration (local report only)


\## 🚀 13. Future Improvements



\- Live webcam monitoring integration

\- Real-time alert dashboard

\- Cloud deployment (AWS / Render)

\- Database integration (MySQL / MongoDB)

\- Improved UI/UX design

\- Custom trained detection model

\- Email notification system for suspicious events

---



\##  Author



Developed as an AI-based academic integrity monitoring system to explore practical applications of Computer Vision in online examinations.



