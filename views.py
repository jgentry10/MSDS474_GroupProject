import json
import urllib.request
import os

from datetime import datetime
from flask import render_template, request, redirect
from FlaskAppAML import app

from FlaskAppAML.forms import SubmissionForm
# Deployment environment variables defined on Azure (pull in with os.environ)
API_KEY = os.environ.get('API_KEY', "optionally place a default value for local dev here")
URL = os.environ.get('URL', "optionally place a default value for local dev here")
# Construct the HTTP request header
HEADERS = {'Content-Type':'application/json', 'Authorization':('Bearer '+ API_KEY)}
# Our main app page/route
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    """Renders the home page which is the CNS of the web app currently, nothing pretty."""

    form = SubmissionForm(request.form)

    # Form has been submitted
    if request.method == 'POST' and form.validate():

        # Plug in the data into a dictionary object 
        #  - data from the input form
        #  - text data must be converted to lowercase
        data =  {
              "Inputs": {
                "input1": {
                  "ColumnNames": [
                    "Title",
                    "Category",
                    "Text"
                  ],
                  "Values": [ [
                      form.title.data,
                      form.category.data,
                      form.text.data.lower()
                    ]
                  ]
                }
              },
              "GlobalParameters": {}
            }

        # Serialize the input data into json string
        body = str.encode(json.dumps(data))

        # Formulate the request
        req = urllib.request.Request(URL, body, HEADERS)

        # Send this request to the AML service and render the results on page
        try:
            # response = requests.post(URL, headers=HEADERS, data=body)
            response = urllib.request.urlopen(req)
            respdata = response.read()
            result = json.loads(str(respdata, 'utf-8'))
            result = json.dumps(result, indent=4, sort_keys=True)
            return render_template(
                'result.html',
                title="From your friendly AML experiment's Web Service:",
                result=result)

        # An HTTP error
        except Exception as err:
            result = json.loads(str(err.code))
            return render_template(
                'result.html',
                title='There was an error',
                result=result)

    # Just serve up the input form
    return render_template(
        'form.html',
        form=form,
        title='Run App',
        year=datetime.now().year,
        message='Input form to gain insights into a company using Azure Machine Learning')