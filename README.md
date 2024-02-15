# world.ly

world.ly is now hosted on the web!
You can visit world.ly [here](http://worldly.live/) or visit http://worldly.live with Google Chrome!

## **Configuration Instructions For Windows**

1. Clone the world.ly repository to your local machine.
```console
git clone https://github.com/rqian239/world.ly.git
```

2. Install Python (developed with Version 3.10.4).

3. Add Python Installation to PATH environment variable.
      - Here is a helpful link: https://www.educative.io/answers/how-to-add-python-to-path-variable-in-windows
   
   To check if setup correctly, open type in the command prompt
```console
python --version
pip --version
```
    
4. Download the Oracle Instant Client package from the Oracle website for Windows (https://www.oracle.com/database/technologies/instant-client/downloads.html)

5. Extract the contents of the Oracle Instant Client and place in a directory.
   - For example, I placed the extracted install directory into an "Oracle" directory with path *D:\Program Files\Oracle\instantclient_21_9* on my Windows machine

6. Add Oracle Instant Client to PATH environment variable. 
    - The steps are the same as adding your python installation to PATH. Except, add  the path of the oracle instant client installation (for example, D:\Program Files\Oracle\instantclient_21_9)
  
7.  Download Microsoft C++ Build Tools (https://visualstudio.microsoft.com/visual-cpp-build-tools/)

8.  Install 'Visual Studio Community 2022' (or latest version) with the Visual Studio Installer. (https://visualstudio.microsoft.com/downloads/)
    - When prompted to install workloads, select 'Desktop development with C++' 
    - If this is not prompted, finish installing 'Visual Studio Community 2022'
        - Then go to the 'Installed' tab and select 'Modify' under 'Visual Studio Community 2022'
        - Select the box labled 'Desktop development with C++' and install

9.  Open the cloned worldly project in your IDE (VSCode is recommended).

10.  Open a command prompt or terminal in the project directory and run 
```console
pip install -r requirements.txt
```
    
11.    In functions.py, change the "path_of_oracle_instant_client" variable to the path of the oracle instant client on your machine.


## **Running On Local Host for Windows**

1. Download UFL VPN, if you do not have it (https://net-services.ufl.edu/provided-services/vpn/clients/)

2. Connect to UFL VPN using the Cisco AnyConnect Secure Mobility Client

3. Type 'vpn.ufl.edu' in the bar if prompted to and insert ufl credentials

4. Open a Command Prompt and navigate to the world.ly project root directory

5. Run
```console
python main.py
```
    
6. Open http://127.0.0.1:8050/ in your web browser

7. Have fun with world.ly!



    
## **Configuration Instructions For Mac**

1. Install the latest version of Python (https://www.python.org/downloads/)
2. Install pip     
    
        python3 get-pip.py
3. Download the Oracle Instant Client package from the Oracle website for your operating system    (https://www.oracle.com/database/technologies/instant-client/downloads.html)

4. After extraction (see download instructions), add the directory containing the Instant Client files to your system's PATH environment variable.

        export DYLD_LIBRARY_PATH="Instant Client Directory"

5. Install the cx_Oracle package

        pip3 install cx_Oracle

6. Install Dash and its required packages

        pip3 install dash dash-renderer dash-html-components dash-core-components




## **Running On Local Host For Mac**

1. Connect to UFL VPN.
2. Set environment variable

        export DYLD_LIBRARY_PATH="Instant Client Directory"
3. In terminal, navigate to project directory and run the Python Dash App 

        python3 app.py
4. Open http://127.0.0.1:8050/ in your web browser
5. Have fun with world.ly!
   

## Database
Demographic data is accessed from a UFL CISE Oracle Database Server, which requires the UF VPN or an on-campus network.

If you are unable to access the database, download [this SQL file](https://drive.google.com/file/d/1K6WxXwEoS9A_q16n0QVXxLz7tYWS55e-/view?usp=drive_link) to build the database.

Use an Oracle SQL Database and modify the `cx_Oracle.connect` function with details of your user and database.


### **Credits:**
Created by Richard Qian, William Sobczak, and Nikhil Pandya
