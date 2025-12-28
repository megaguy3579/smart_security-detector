# Smart Security Log Analyzer (Python)

## Overview
Smart Security Log Analyzer is a Python-based mini cybersecurity project that analyzes system logs to detect suspicious activities such as brute-force login attempts and DoS-like request flooding.

The project demonstrates how basic data structures like stack and queue can be used to understand IP behavior from logs and generate security alerts.

---

## Features
- Auto log generation
- Dynamic IP extraction
- Brute-force attack detection (Stack)
- DoS attack detection (Queue)
- Top attacking IP analysis
- Alerts saved in a file

---

## Project Structure
log_generator.py     - Generates sample logs  
log_reader.py        - Reads logs from file  
stack_detector.py    - Brute-force detection logic  
queue_detector.py    - DoS detection logic  
stats.py             - Finds top attacking IPs  
alert_manager.py     - Saves alerts  
main.py              - Main controller  
logs.txt             - Generated logs  
alerts.txt           - Detected alerts  

---

## How It Works
1. Logs are generated automatically.
2. Logs are read line by line.
3. Stack logic detects repeated login failures.
4. Queue logic detects excessive requests.
5. Alerts are generated based on thresholds.
6. All alerts are saved into alerts.txt.

---

## How to Run
Open terminal in the project folder and run:

python main.py

---

## Output
- logs.txt contains generated logs
- alerts.txt contains detected security alerts

---

## Concepts Used
- Python file handling
- Stack and Queue (DSA)
- Log analysis
- Threshold-based alert detection

---

