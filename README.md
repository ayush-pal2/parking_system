# 🚗 Smart Parking Lot System

A web-based **Smart Parking Lot Management System** built using **HTML, CSS, JavaScript, and Django**.  
The application automatically manages parking slots and allocates the nearest suitable slot based on vehicle requirements such as **EV charging** and **covered parking**.

---

## 📌 Features

### ✅ Add Parking Slot
- Add new parking slots with the following attributes:
  - Slot Number
  - Covered / Uncovered
  - EV Charging Availability
  - Occupied Status

### ✅ View All Slots
- Display all parking slots in a structured and user-friendly layout.
- Shows real-time slot status (Available / Occupied).

### ✅ Park Vehicle
- Allocate the **nearest available matching slot** based on:
  - EV charging requirement
  - Covered parking requirement
- Displays **“No slot available”** if no suitable slot is found.

### ✅ Remove Vehicle
- Free up an occupied parking slot.
- Instantly updates the slot availability.

---

## 🧠 Logic Used
- Filters parking slots based on:
  - Availability (`isOccupied = false`)
  - EV requirement
  - Covered requirement
- Allocates the **lowest slot number first** to ensure nearest-slot assignment.

---

## 🖥️ Tech Stack

- **Frontend:**  
  - HTML  
  - CSS  
  - JavaScript  

- **Backend:**  
  - Django (Python)

- **Database:**  
  - SQLite (default Django database)

- **Deployment:**  
  - Render

---

## 📂 Project Structure
parking_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── parking/
    ├── __init__.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    │   └── __init__.py
    └── templates/
        └── parking/
            ├── index.html
            ├── add_slot.html
            └── park_vehicle.html


