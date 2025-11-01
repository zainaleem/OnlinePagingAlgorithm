# 🧠 Online Paging Algorithms (FIFO Prototype)

A simple FastAPI-based project that simulates **online paging algorithms** for cache management, starting with **FIFO (First-In-First-Out)**.
It visually compares cache performance for different cache sizes using **cache hit/miss ratios** and a **dynamic graph**.

---

## 🚀 Features

* Accepts user input for:

  * Cache capacity range (min–max)
  * Sequence of webpage requests (space-separated URLs)
* Simulates FIFO cache replacement
* Displays cache hit/miss counts and ratios
* Compares results for multiple cache sizes
* Visualizes results with an interactive chart

---

## ⚙️ Requirements

* Python 3.10 or above
* FastAPI
* Uvicorn
* Jinja2

---

## 📦 Installation & Setup

1. **Clone this repository:**

   ```bash
   git clone https://github.com/zainaleem/OnlinePagingAlgorithms.git
   cd OnlinePagingAlgorithms
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**

   ```bash
   uvicorn app:app --reload
   ```

4. **Open the app in your browser:**

   ```
   http://127.0.0.1:8000
   ```

---

## 💡 Example Input

**Cache Capacity Range:**

```
Min: 2  
Max: 6
```

**URLs (space-separated):**

```
https://contoursoft.com/home https://contoursoft.com/about https://contoursoft.com/contact https://contoursoft.com/services https://contoursoft.com/home https://contoursoft.com/blog https://contoursoft.com/contact https://contoursoft.com/careers https://contoursoft.com/services https://contoursoft.com/home https://contoursoft.com/partners https://contoursoft.com/blog https://contoursoft.com/contact https://contoursoft.com/services https://contoursoft.com/home
```

---

## 🧩 Project Structure

```
OnlinePagingAlgorithms/
│
├── app.py                 # FastAPI backend
├── templates/
│   └── index.html         # Frontend (UI)
├── requirements.txt       # Python dependencies
└── README.md              # Documentation
```

---

## 🧠 Future Work (for Final Project)

* Add more algorithms:

  * LRU (Least Recently Used)
  * LFU (Least Frequently Used)
  * Optimal (offline)
* Compare competitive ratios
* Analyze real-world web request traces

---

## 👨‍💻 Authors

**Zain Aleem**
**Khalil Ahmed**
**Haroon**
**Mubashir Ali**
**Ali Ahmed**

