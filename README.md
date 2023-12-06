# Newspaper agency 
Newspaper agency example, made in Django, a website with custom styles.

## Deployed project could be found here:
[Deployed project](https://newspaper-mate-21bb.onrender.com)

User credentials:
- login: 
```user```
- password: 
```user12345```


Diagram:\
![image](https://i.imgur.com/6r4Ioo2.png)


## How to install

1) Open Terminal and open folder to clone project in.

2) Clone repository into a desirable folder:

    ```
    git clone https://github.com/Wonsky1/newspaper_agency
    ```

3) Open cloned folder in terminal

4) If you don't have **pip** installed  [install it here](https://pip.pypa.io/en/stable/installation/#).

5) Create and activate **Virtual environment**:
   
   **Windows**
   ```
   python -m venv venv
   ```
   
   ```
   venv\Scripts\activate
   ```
   
   **MacOS**
   ```
   python3 -m venv venv
   ```
   
   ```
   source venv/bin/activate
   ```
   
6) Open cloned folder and install needed requirements using:

    ```
    pip install -r requirements.txt
    ```

7) Migrate:

   ```
   python manage.py migrate
   ```

8) Install database fixture:

   ```
   python manage.py loaddata db_data.json
   ```

9) Create .env file using ```env_example``` file

10) Run server:
   
   ```
   python manage.py runserver
   ```

11) Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Pages images:

1. main page: \
![image](https://i.imgur.com/HVoV2W1.png)
2. Header when not logged in: \
![image](https://i.imgur.com/MSAM6gj.png)

3. Create Views:
![image](https://i.imgur.com/z0HNDdx.png)

4. Detail Views:
![image](https://i.imgur.com/CimRPM6.png)

5. Delete Views:
![image](https://i.imgur.com/1vh1ZD9.png)
