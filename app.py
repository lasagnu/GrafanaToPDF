import json
import time
import os

from flask import Flask, send_from_directory, request, render_template, redirect, url_for

import Config
from PyDFiler import *

app = Flask(__name__)
pdf = PyDFiler()

@app.route('/')
def index():
    dashboards = json.dumps(pdf.get_dashboards())
    return render_template('index.html', message=dashboards)

@app.route('/dashboard')
def dashboard_list():
    dashboards_dict = pdf.get_dashboards()
    return json.dumps(dashboards_dict)

@app.route('/dashboard/<string:dashboard_uid>')
def generate_pdf(dashboard_uid):
    range_time_from = request.args.get('from', default='now-1d', type=str)
    range_time_to = request.args.get('to', default='now', type=str)
    try:
        if pdf.dashboard_exists(dashboard_uid):
            timestamp = str(time.time()).replace(".", "")
            output_folder = Config.Application.generated_files_dir / timestamp
            os.makedirs(output_folder)
            pdf_path = pdf.generate_PDF_from_dashboard(dashboard_uid, output_folder=output_folder,
                                                            range_time_from=range_time_from,
                                                       range_time_to=range_time_to,
                                                       print_title=True)

            url = url_for('serve_existing_pdf', timestamp = timestamp)
            return redirect(url)
        else:
            return '{"error":"dashboard nie istnieje"}'

    except Exception as ex:
        print(ex)
        return f'{{"error":"cannot serve_pdf for dashboard: {ex}"}}'

@app.route('/dashboard/<int:timestamp>')
def serve_existing_pdf(timestamp):
    '''

    :param timestamp:
    :return: existing (pre-generated) PDF report
    '''
    pdf_dir = Config.Application.generated_files_dir / str(timestamp)

    if pdf.dir_exists(pdf_dir):
        return send_from_directory(pdf_dir, 'raport.pdf')
    else:
        return f'{timestamp} raport does not exist!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
