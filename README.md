# Washroom-Occupancy-Dashboard
Washroom Occupancy Dashboard

Overview
This project is a web-based dashboard that displays real-time occupancy status for public facilities like washrooms, including icons for female, male, family, disabled, and prayer rooms, with live counters and "Vacant/Occupied" indicators. Inspired by smart building systems in construction projects (e.g., LED signs in malls or offices), it simulates sensor data for demo purposes but can be extended to real IoT sensors.
Why It's Needed in Public Washrooms
Public washrooms in high-traffic areas (airports, malls, offices) often lead to long waits, frustration, and inefficiency. This dashboard addresses key issues:

User Convenience: Travelers or shoppers can quickly check availability without walking around, saving time and reducing crowds.
Accessibility: Highlights disabled or family rooms, aiding vulnerable users like parents or those with disabilities.
Hygiene & Maintenance: Real-time data alerts cleaners to high occupancy, enabling proactive cleaning to prevent overflows or unsanitary conditions.
Efficiency in Construction Projects: For building managers, it optimizes space usage, integrates with smart buildings, and enhances user experience in modern facilities—potentially increasing tenant satisfaction and compliance with accessibility laws (e.g., ADA in the US or similar in Hong Kong/Asia).
Overall, it promotes inclusivity, reduces wait times by 20-30% (based on similar IoT studies), and turns a basic amenity into a smart, user-friendly feature.

Installation

Clone the repo: git clone https://github.com/Saurav20902/washroom-occupancy-dashboard.git
Navigate to folder: cd washroom-occupancy-dashboard
Install dependencies: pip install -r fastapi.txt

Usage

Run the app: python main.py
Open browser: It auto-opens at http://127.0.0.1:8002 (or manually visit the URL shown in terminal).
View the dashboard: Watch live updates every 5 seconds—counters change, colors shift (green for vacant, red for occupied).
Stop: Press Ctrl+C in terminal.
