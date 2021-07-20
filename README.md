# flask-prometheus

## Running Locally

~~~~
pip install pipenv
pipenv shell
pipenv sync
FLASK_APP=main.py flask run --host=0.0.0.0
~~~~

## Testing

~~~~
for i in {1..100}; do curl localhost:5000/test/ ; sleep 1 ; done
~~~~

## Source

https://www.cloudbees.com/blog/monitoring-your-synchronous-python-web-applications-using-prometheus