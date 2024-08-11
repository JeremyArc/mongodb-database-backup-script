# MongoDB Backup Project

This project demonstrates how to back up MongoDB data to a CSV file using Python. It uses the `pymongo`, `pandas`, and `schedule` libraries.

## Setup Instructions

1. **Clone the repository** (or download the project files).

2. **Navigate to the MongoDB backup directory**:
    ```sh
    cd web_scraping_project/mongodb_backup
    ```

3. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

4. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

5. **Install the required libraries**:
    ```sh
    pip install -r requirements.txt
    ```

6. **Run the MongoDB backup script**:
    ```sh
    python backup.py
    ```
