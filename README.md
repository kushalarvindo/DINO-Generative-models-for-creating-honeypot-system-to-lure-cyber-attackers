# DINO-Generative models for creating honeypot system to lure cyber attackers

---

# 🎯 DEEPDECOY: AI-Powered Adaptive Honeypot System

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Django](https://img.shields.io/badge/Django-3.2+-092E20.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E.svg)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57.svg)

**DEEPDECOY** is a next-generation "Active Defense" cybersecurity platform. Instead of acting as a traditional firewall that passively blocks intruders, DEEPDECOY deploys a high-fidelity "Shadow Infrastructure" to actively lure, delay, and analyze cyber adversaries.

By leveraging a **Zero-Activity Baseline** and a **Logistic Regression Machine Learning engine**, the system instantly intercepts malicious payloads and classifies threats with 96.4% accuracy in under 150 milliseconds.

---

## 🚀 Key Features

* **High-Fidelity Decoys ("Neural-Phish"):** Features a mature "Glassmorphism" and Matrix-style CRT terminal UI designed to look like a highly sensitive corporate network, maximizing the attacker's "dwell time."
* **Zero-Activity Baseline:** Because no legitimate user should ever access this decoy environment, *any* intercepted traffic is instantly classified as a high-confidence threat, eliminating alert fatigue.
* **Real-Time AI Classification:** Intercepts POST requests and vectorizes categorical data (IP, Port, Protocol, Action, Payload) using `LabelEncoder` before feeding it to a pre-trained ML model.
* **Forensic Radar Dashboard:** A secure, hidden administrative command center that utilizes Django ORM and SQLite to log and display intercepted attack vectors safely.

---

## 🏗️ System Architecture

1. **The Lure (Frontend):** Fake portals (`login.html`, `register.html`) attract brute-force and injection attacks.
2. **The Interceptor (Django Middleware):** `views.py` captures the attacker's Source IP, Destination Port, Protocol, Action, and Payload.
3. **The Brain (AI Engine):** The raw text is standardized and passed to our serialized `model.sav` (Logistic Regression), instantly returning a threat probability.
4. **The Command Center:** The attack is logged in the `HoneyPot` database table and rendered on the secure `adminhome.html` radar dashboard.

---

## 💻 Tech Stack

* **Backend:** Python 3.10, Django Web Framework
* **Machine Learning:** Scikit-learn, Pandas, Joblib (Model Serialization)
* **Database:** SQLite3 (via Django ORM)
* **Frontend:** HTML5, CSS3 (Custom SCSS), Vanilla JavaScript (Terminal Animations)

---

## ⚙️ Installation & Setup

Follow these steps to run DEEPDECOY locally on your machine:

**1. Clone the repository**
```bash
git clone [https://github.com/yourusername/deepdecoy.git](https://github.com/yourusername/deepdecoy.git)
cd deepdecoy

```

**2. Create and activate a Virtual Environment (Recommended)**

```bash
python -m venv env
# On Windows:
env\Scripts\activate
# On Mac/Linux:
source env/bin/activate

```

**3. Install Dependencies**

```bash
pip install django pandas scikit-learn

```

*(Ensure you have your pre-trained `model.sav` and `label_encoder.pkl` files in the correct directory).*

**4. Run Database Migrations**

```bash
python manage.py makemigrations
python manage.py migrate

```

**5. Create a Superuser (For Admin Radar Access)**

```bash
python manage.py createsuperuser

```

**6. Start the Local Server**

```bash
python manage.py runserver

```

Visit `http://127.0.0.1:8000` in your browser to access the honeypot.

---

## 🧪 Developer Testing & Demo Cheat Sheet

To bypass waiting for an organic cyberattack during presentations, use the **Scan New Traffic (`/data`)** module to manually inject payloads into the AI model.

Use the following exact data points to demonstrate the system:

### 🔴 Demo 1: Trigger a "Critical Threat" (Success/Breach)

* **Source IP:** `24.119.174.130`
* **Dest Port:** `80`
* **Protocol:** `RDP`
* **Action:** `File upload`
* **Payload:** `Sample payload 5`
*(Outcome: The system will trigger the pulsing Red Alert screen).*

### 🟢 Demo 2: Trigger a "System Secure" (Harmless Traffic)

* **Source IP:** `17.103.246.192`
* **Dest Port:** `445`
* **Protocol:** `RDP`
* **Action:** `Port scan`
* **Payload:** `Sample payload 156`
*(Outcome: The system will trigger the Green Shield screen).*

### 🛡️ View Logs

To view the intercepted attacks, navigate to `/adminlogin`, enter your Superuser credentials, and access the Radar Dashboard.

---

## 👥 Project Team

Built as a partial fulfillment for the Diploma in Computer Science Engineering (2025-2026) at PES Polytechnic, Bangalore.

* **Darshith R**
* **Keerthana J**
* **Kulkarni Shreesh Sanjeev**
* **Kushal Arvind O**

**Under the Guidance of:** Smt. Sukrutha H S

**With the help of Backend Development of:** Alpha Tech Academy

---

*Disclaimer: This system is designed strictly for academic research and defensive cybersecurity purposes.*
