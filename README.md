# BrightnessControl
# Hand Tracking Brightness Control

This project allows you to control the screen brightness of a computer using hand gesture detection. By measuring the distance between the thumb and index finger, the application adjusts the screen brightness accordingly.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Source Code](#source-code)
- [Contributing](#contributing)
- [Warnings](#warnings)

## Features

- Real-time hand detection using the MediaPipe library.
- Screen brightness adjustment based on the distance between the thumb and index finger.
- Visual interface displaying the current distance and brightness.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Python libraries:
  - `opencv-python`
  - `mediapipe`
  - `screen-brightness-control`

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo

2. **Create a virtual environment:**
   ```bash
   python -m venv venv

3. **Activate the virtual environment:**
   
   - On Windows:
     ```bash
     .\venv\Scripts\activate

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     
4. **Install the dependencies:**
   ```bash
   pip install opencv-python mediapipe screen-brightness-control

  ## Usage

  1. **Run the Python script:**
     ```bash
     python hand_brightness_control.py

  2. **Adjust the distance between your thumb and index finger to control the brightness:**
     -Brightness will increase when the distance is short and decrease when the distance is long.
     -To exit the program, press the q key.

## Source Code

The source code for the project is available in the hand_brightness_control.py file.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## Warnings

  -Ensure your webcam is functioning correctly before running the script.
  -This project is designed to work on operating systems that support the libraries used.


  
Feel free to modify it as needed!
