# COVID Patients Management System

This project is a **COVID Patients Management System** developed using Python and MySQL. It allows admins to manage COVID-19 patient and staff records, including adding, displaying, and removing records, and automating the process of tracking COVID-positive patients based on symptoms.

## Features

- **Admin Panel**: 
  - Add/Remove Patients
  - Add/Remove Staff
  - Display Patient and Staff Records
  - Change Admin Password

- **Patient Panel**:
  - Symptom-based COVID diagnosis
  - Automatic patient record generation for positive cases
  - Information about quarantine and active cases

## Requirements

- **Python** (version 3.6 or above)
- **MySQL Connector for Python**
- **MySQL Database**

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/covid-patient-management-system.git
    ```

2. Install the required packages:
    ```bash
    pip install mysql-connector-python
    ```

3. Set up MySQL database:
    - Ensure MySQL is installed and running on your system.
    - Change the database credentials in the code (`host`, `user`, `passwd`).

4. Run the script:
    ```bash
    python covid_management.py
    ```

## Usage

### Admin

1. Login using the default admin credentials:
    - **Username**: `Admin`
    - **Password**: `ng` (you can change this later in the application)

2. Admin has the following options:
    - Add Patients
    - Add Staff
    - Display Patients Record
    - Display Staff Record
    - Change Password
    - Remove Patients
    - Remove Staff
    - Logout

### Patient

1. Symptom-based self-assessment can be done by selecting the `Patient` option.
2. The system provides a diagnosis and, if positive, automatically saves the patient's details.

## Screenshots

### 1. Admin Login

![Admin Login](ss/s1.png)

### 2. Add Patient

![Add Patient](./ss/s2.png)

### 3. Display Patient Records

![Display Patient Records](./ss/s3.png)

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
