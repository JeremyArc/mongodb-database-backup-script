# MongoDB collection backup scheduler

This Python script provide a periodical MongoDB's collection backup script, there are also included docker-compose file
for demonstrate when user have MongoDB database running with web based client to manipulate data within database.


## Overview

This script are going to do the following:

1. Ask user for database credential, database name and collection to be backed up.
2. Periodically back up data in .csv form based on configuration in the code.

## Prerequisite

1. install Python 3.12.x on your machine.

    ```bash
    brew install python
    ```

2. install pipenv

    ```bash
    brew install pipenv
    ```

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/JeremyArc/mongodb-database-backup-script.git
   cd mongodb-database-backup-script
   ```

2. Create and activate a virtual environment within this project:

    ```bash
    pipenv shell
    ```

3. Install dependencies 

    ```bash
    pipenv install
    ```

4. (Optional) Run MongoDB database using docker-compose.yaml file

## Usage

1. Run the script:

    ```bash
    python index.py
    ```
