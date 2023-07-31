# Raw Material Inventory Management System

## Overview

Raw Material Inventory Management System is a Python-based application designed to help manage raw material inventory in a user-friendly way. 
The system allows users to add, update, and delete raw material entries, view the current stock, and generate transaction records. 
The application has been developed using Python 3.7 and can be run on Windows operating systems as a stand-alone executable file.

## System Requirements

- Python 3.7 (venv) or higher installed on your machine
- Operating System: Windows (the .exe file is specific to Windows)
- Required Python libraries: PyQt5

## How to Run the Application

1. Clone the GitHub repository to your local machine using the following command:
 ```bash
git clone [https://github.com/bkumaranbk/Raw-Material-Management-System.git]
```

2. Navigate to the project directory:
 ```bash
cd Raw-Material-Management-System
```

3. Install required Python libraries (if not already installed):
 ```bash
pip install PyQt5
 ```

4. Generate the executable (.exe) file using pyinstaller:
 ```bash
pyinstaller stockmanager.py --onefile
```
5. Double-click the generated .exe file to run the Raw Material Inventory Management System.

# Application Features
- **Add New Raw Material:** Allows users to add a new raw material entry by providing the name, quantity, and cost of the material.

- **Update Quantity:** Enables users to update the quantity of an existing raw material. It also records the transaction as "ADD" or "REDUCE" depending on whether the quantity is increased or decreased.

- **Delete Raw Material:** Allows users to delete an existing raw material entry from the inventory.

- **View Current Stock:** Displays the current stock of raw materials in the inventory.

- **Transaction Records:** Maintains a transaction log, recording all additions and reductions in raw material quantities with date and time.

# Contributing
Contributions to this project are welcome. If you find any bugs, have new feature ideas, or want to enhance the application, feel free to open an issue or submit a pull request.

# License
This project is licensed under the MIT License.

# Acknowledgments
Special thanks to Mr.Kasun sir for creating this Raw Material Inventory Management System.

# Contact
If you have any questions or need further assistance, feel free to contact us at bkumaran98@gmail.com.
