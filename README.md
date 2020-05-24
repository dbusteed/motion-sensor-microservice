# motion sensor microservice

lil' example of a microservice implemented with a REST API

## usecase

imagine you are making your own home security system with various IoT devices. for this example, you are only concerned with tracking motion around your devices

## architecture

1) IoT devices send data to the API microservice when they detect motion
2) Microservice processes data and writes to database
3) Browser / other client application can request past motion event data 

`**NOTE** ` Rather than using actual IoT devices with motion sensors, I used a Python program (`motion_sensor.py`) to simulate a device with an active motion sensor

## quickstart

1) clone the repo
2) install Flask and Flask-CORS
    ```
    pip install flask flask-cors
    ```
3) create the database
    ```
    python db_init.py
    ```
4) in one terminal window, start the microservice
    ```
    python api.py
    ```
5) in another terminal window, start the motion sensor simulator
    ``` bash
    #
    # pass deviceID and deviceName as parameters 
    #
    python motion_sensor.py 42 "front door"
    ```
6) (OPTIONAL) start some more motion sensor programs
7) hit `ENTER` inside the motion sensor program to simulate motion detection
8) navigate your browser to `http://localhost:5000/events` to view event data
9) navigate to `http://localhost:5000` for details on how to use query parameters

## other notes

* to make your scripts executable, you will most likely need to change the `#!/usr/bin/python3.8` at the top of each file to the correct location for your Python installtion