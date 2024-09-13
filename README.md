# COVID Patients Management System

## Overview

The COVID Patients Management System is a Python application designed to manage and monitor COVID-19 patient data. It provides functionalities for administrators to manage patient and staff records, track COVID-19 cases, and handle login credentials. The system uses a MySQL database to store and retrieve data.

## Features

### Admin Features
- **Add Patients:** Add new patient records with details like name, age, gender, and COVID-19 confirmation date.
- **Add Staff:** Add new staff records with details such as name, age, gender, post, and salary.
- **Display Patients Record:** View details of patients stored in the database.
- **Display Staff Record:** View details of staff members.
- **Change Password:** Update the admin password for secure access.
- **Remove Patients:** Delete patient records from the system.
- **Remove Staff:** Delete staff records from the system.

### Patient Features
- **Self-Assessment:** Answer questions to assess symptoms and determine if you might be COVID-19 positive.

## Usage

### Admin Login
1. **Select the Admin Option:**
   - Choose the "Admin" option from the main menu.
2. **Enter Password:**
   - Input the admin password to access the admin functionalities.

### Admin Functionalities
- **Add Patients:**
  - Input patient details including name, age, gender, and COVID-19 confirmation date.
  - The system updates the database with the new patient record.
- **Add Staff:**
  - Input staff details including name, age, gender, post, and salary.
  - The system updates the database with the new staff record.
- **Display Patients Record:**
  - View details of patients stored in the database.
- **Display Staff Record:**
  - View details of staff members.
- **Change Password:**
  - Update the admin password for secure access.
- **Remove Patients:**
  - Delete patient records from the system based on patient ID.
- **Remove Staff:**
  - Delete staff records from the system based on staff ID.

### Patient Interaction
1. **Select the Patient Option:**
   - Choose the "Patient" option from the main menu.
2. **Self-Assessment:**
   - Answer questions about symptoms and body temperature to assess COVID-19 risk.
   - The system will provide feedback based on your responses and record patient data if necessary.

## Code Structure

### Database Schema
- **`staff` Table:**
  - **Columns:**
    - `sno`: Staff ID
    - `name`: Name of the staff member
    - `age`: Age of the staff member
    - `gender`: Gender of the staff member
    - `post`: Post or designation of the staff member
    - `salary`: Salary of the staff member

- **`patients` Table:**
  - **Columns:**
    - `sno`: Patient ID
    - `name`: Name of the patient
    - `age`: Age of the patient
    - `gender`: Gender of the patient
    - `date`: Date of COVID-19 confirmation

- **`login` Table:**
  - **Columns:**
    - `admin`: Username for admin login
    - `password`: Password for admin login

- **`sno` Table:**
  - **Columns:**
    - `patient`: Current count of patients
    - `staff`: Current count of staff

### Main Code
- **Database Connection:**
  - Establishes a connection to the MySQL database using `mysql.connector`.

- **Database Initialization:**
  - Creates the necessary database and tables if they do not already exist.

- **Interactive Menu:**
  - Provides an interactive menu for both admin and patient functionalities.
  - **Admin Functionalities:**
    - Adding, removing, and displaying records.
    - Changing the admin password.
  - **Patient Functionalities:**
    - Answering symptom-related questions.
    - Recording patient data based on the assessment.
