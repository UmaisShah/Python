<!-- setting up virtual environment for project -->
# Linux
sudo apt-get install python3-venv    # If needed
python3 -m venv .venv
source .venv/bin/activate

# macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
py -3 -m venv .venv
.venv\scripts\activate

<!-- for creating django project use -->
django-admin startproject project_name
<!-- setting up local server -->
python3 manage.py runserver
<!-- create subfolder for project -->
python manage.py startapp hello
