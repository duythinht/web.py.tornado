web.py.tornado
==============

Integrate Web.py to Tornado Server

### Setup virtualenv & install pip dependencies

    pip install -r requirements.txt

### Run Tornado Server

    python pi_server.py

Application run on follow url

    http://localhost:8000/

### Application structure:

    /
        /bootstrap.py   # Bootstrap runtime configuration for project
        /routes.py      # Applicatio routings
        /app            # Application Handlers folder
            /...        # Handlers modules
        /pi_server.py   # Tornado Initial Server
