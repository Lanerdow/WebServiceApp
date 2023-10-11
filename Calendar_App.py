from flask import Flask, render_template, request
import requests

app = Flask(__name__)


# Route par défault / index
@app.route('/')
def index():
    return render_template('index.html')


# Route vers l'API
@app.route('/calendar', methods=['GET'])
def get_calendar():

    # Récupération de la variable year en GET
    year = request.args.get('year')

    # Récupération de la variable month en GET
    month = request.args.get('month')

    # URL de l'API
    api_url = 'http://localhost:8080/calendar?year=' + year + '&month=' + month

    try:
        # Requête HTTP
        response = requests.get(api_url)
    except:
        # Cas si exception
        print(f"Erreur lors de la requête")
        return render_template('error.html')
    else:
        # Cas si réussite
        if response.status_code == 200:
            # Cas si code == 200
            data = response.json()
            print(data["calendar"])
            return render_template('calendar.html', calendar=data['calendar'])
        else:
            # Cas si cde != 200
            print(f"Error for the request with status code {response.status_code}")
            return render_template('error.html')


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
