# world.ly


## **Configuration Instructions**

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


<br >

## **Running On Local Host**

1. Conect to ufl VPN.
2. Set environment variable

        export DYLD_LIBRARY_PATH="Instant Client Directory"
3. In terminal, navigate to project directory and run the Python Dash App 

        python3 app.py
4. Open http://127.0.0.1:8050/ on a web browser
   
   <br />

### **UFL CISE Oracle Database Server Used**
Username: williamsobczak <br />
Password= REBY7TpizLTdOp5dZHa9qJS0

<br />

### **Credits:**
Created by Group 2 