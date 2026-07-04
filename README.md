# CyberSecurity_Project
Design and development of a basic antivirus system fpr understanding how antivirus works internally

Completed LEVEL-1: At this level, the goal is to build a simple antivirus program that scans files on a computer and checks
whether any of them match known malware. The system works by reading each file, generating a
cryptographic hash (digital fingerprint), and comparing it with a database of known malicious hashes.
If a match is found, the file is marked as infected. This level focuses on understanding how files are
scanned, how malware signatures work, and how detection based on known threats is implemented.

The task was to create:
-> Build a file scanning script
-> Create malware signature list
-> Detect and report infected files

_
******Future improvements added:**_**


#####
# Behavioral Monitoring Antivirus Module

A lightweight behavior-based antivirus system that monitors system activity in real time to detect and respond to potentially malicious behavior. Instead of relying solely on signature-based detection, this project analyzes process, file, and network activities to identify suspicious behavior.

---

## Features

- **Process Monitoring**
  - Monitors running processes using `psutil`
  - Detects suspicious or unauthorized process behavior

- **File System Monitoring**
  - Watches file system events using `watchdog`
  - Detects unexpected file creation, modification, deletion, and movement

- **Network Monitoring**
  - Captures and analyzes network traffic using `scapy`
  - Identifies suspicious network activity

- **Rule-Based Anomaly Detection**
  - Applies predefined behavioral rules
  - Flags potentially malicious activities in real time

- **Automatic Response**
  - Terminates processes identified as malicious
  - Helps minimize potential damage

---

**##########**

# AI-Assisted Malware Detection

An AI-powered malware detection system that identifies malicious software based on **dynamic API call behavior** using machine learning. The project leverages behavioral analysis instead of traditional signature-based detection, enabling the detection of previously unseen malware patterns.

---

##  Project Objective

The objective of this project is to detect malware by analyzing **dynamic API call sequences** generated during program execution. A **Random Forest Classifier** is trained on behavioral data to accurately distinguish between benign and malicious software.

---

##  Features

- Behavior-based malware detection
- Dynamic API call analysis
- Machine learning-based classification
- High detection accuracy
- Model persistence using Joblib
- Performance evaluation using ROC-AUC and cross-validation
- Data visualization with Matplotlib

---

##  Dataset

**Dataset:** Dynamic API Call Dataset

The dataset contains API call behavior collected during program execution and is labeled as **benign** or **malicious**.

---

##  Machine Learning Algorithm

- **Random Forest Classifier**

The model is trained using Scikit-learn and optimized to classify malware based on runtime API behavior.

---

##  Model Performance

| Metric | Score |
|---------|-------|
| Accuracy | **98.91%** |
| Cross-validation Accuracy | **98.95%** |
| ROC-AUC Score | **0.9899** |

---

##  Technologies Used

- Python
- Google Colab
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Matplotlib

---
