python -m venv venv
source ./venv/bin/activate
pip install < requirements.txt
flask db init
flask db migrate
flask db upgrade
python ./main.py


http://127.0.0.1:5000