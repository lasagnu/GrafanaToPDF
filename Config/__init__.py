from pathlib import Path
import os

main_dir = Path(os.getcwd())

class Grafana:
    address = 'HOST:IP'
    api_key = 'GRAFANA_API_KEY'

class wkhtmltopdf:
    path = os.path.join(main_dir, 'wkhtmltox/bin/wkhtmltopdf')
    input_html = os.path.join(main_dir, 'generated/index.html')
    output_pdf = os.path.join(main_dir, 'generated/raport.pdf')

class Default:

    class Collage:
        path = Path(str(wkhtmltopdf.input_html).rpartition("\\")[0]) / 'collage.png'
        margin_x = 3
        margin_y = 3

    class Font:
        #needs to be a string as ImageFont.truetype does not accept Path()
        path = str(main_dir / 'core/fonts' / 'Arial.ttf')
        size = 22
        fill = (0, 0, 0)

    class Image:
        width = 300
        height = 150

    class Template:
        dashboard = main_dir / 'templates' / 'dashboard.html'
        index = main_dir / 'templates' / 'index.html'

class Application:
    generated_files_dir = Path(os.path.join(main_dir, 'generated'))

