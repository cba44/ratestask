# Rates API Task README

## System Requirements

You'll need to have latest versions of **docker** and **docker compose** installed on your machine.\
[Install Docker](https://docs.docker.com/engine/install/)\
[Install Docker Compose](https://docs.docker.com/compose/install/)

---

## How To Build Docker Image For ratestask

- Open the terminal(Command Prompt / Powershell for Windows) in the same folder as this README file.
- The docker image can be built with docker compose in the terminal using

  ```
  docker compose build ratestask_api
  ```

---

## How To Run Locally

- Open the terminal(Command Prompt / Powershell for Windows) in the same folder as this README file.
- The project can be run with docker compose in the terminal using

  ```
  docker compose up -d
  ```

- Now, the API is running on port **80**.

### Port Conflicts

- In case of port conflict for application, change following in **docker-compose.yml** under **ratestask_api** service.

  ```
  ports:
    - "{NEW_PORT}:80"
  ```

- Now the application will run on the new port.

---

## Base URL

- If port is not changed as mentioned in Port Conflicts, the API will run in http://127.0.0.1
- If port is changed for example to port 7575, the Base URL will be http://127.0.0.1:7575

---

## Requests for API

- You can use the **Swagger UI** to view the requests. The URL is **[base_URL]/swagger-ui**

### Getting average prices for each day on a route between port codes origin and destination

- URL :- **[base-url]/rates**
- Request Type :- **GET**
- Required query parameters

  - **date_from** _(\*required)_ :- In _YYYY-MM-DD_ Format
  - **date_to** _(\*required)_ :- In _YYYY-MM-DD_ Format
  - **origin** _(\*required)_ :- Can be a _port code_ or a _region slug_
  - **destination** _(\*required)_ :- Can be a _port code_ or a _region slug_

  Example query

  ```
  http://127.0.0.1/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main
  ```

## Running Tests

- This testcases were tested on python 3.12.3
- To run the testcases, first install and use a virtual environment.

  - For Windows OS, run these commands on command prompt/ powershell in the same folder as this README file.

    ```
    python -m venv .venv
    .venv\Scripts\activate
    ```

  - For other OSes, run these commands on terminal in the same folder as this README file.

    ```
    python3.12 -m venv .venv
    source .venv/bin/activate
    ```

- Then run the following command to install required libraries.

  ```
  pip install -r requirements.txt
  ```

- You need a new postgresql container to run the test cases.

  - First stop instance of postgres container running with ratestask API.
    ```
    docker compose down
    ```
  - Run the postgresql container for test cases.
    ```
    docker-compose -f docker-compose-pytest.yml up -d
    ```

- Then run the following command to run tests.
  ```
  pytest
  ```
