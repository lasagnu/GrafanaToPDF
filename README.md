# grafana-pdf-reporter

independent service for generating PDF based on Grafana dashboards, developed mainly for CentOS 7, but might work on different distros/OS with small tweaks.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

For docker-based installation:

```
CentOS 7, docker, docker-compose
```

For regular Python-app installation:

```
CentOS 7, docker, docker-compose, Python3.6+, venv
```

### Installing

Clone repository

```
git clone https://github.com/lasagnu/grafana-pdf-reporter/
```

Enter the dir with reporter:

```
cd grafana-pdf-reporter/
```

Make it possible to execute wkhtmltopdf_setup.sh

```
chmod +x wkhtmltopdf_setup.sh
```

Execute the script and allow wkhtmltopdf to be installed locally

```
./wkhtmltopdf_setup.sh
```

Edit configuration file and provide the IP address and port of Grafana as well as the API key:

```
Config/__init__.py

Example:

class Grafana:
    address = '192.168.0.1:3000'
    api_key = 'BlAhBlAHblAhBlaHblahsdladOoPaDoOpAdOopAdoOpa=='

```

## Execute as a docker container

Simply run this command to build a container and mount it:

```
docker-compose -p CONTAINER_NAME up -d
```

Service should be available on the HOST_IP:5000 by default. It could be changed in the docker-compose.yml:

```
ports:
            - "<host_port>:5000"
```

## Execute locally as a regular Python app:

I would recommend to install the virtualenv first:

```
python3 -m venv venv
```

Once the virtual environment has been established, activate it by:

```
source venv/bin/activate
```

And install all dependencies:

```
pip install -r requirements.txt
```

Once installed you should be able to run it by using this command:

```
python3 app.py
```
## Usage

Once the application is up and running, you should be able to generate the PDF with all panels of a dashboard by passing it's UID to the /dashboard endpoint:

```
localhost:5000/dashboard/<dashboard_uid>
```

You can view the generated raport once again by accessing the same /dashboard enpoint and passing the ID generated previously

```
example: localhost:5000/dashboard/1581089563394252
```

## Setting up the link in Grafana

![Example](https://i.imgur.com/e8P57hs.png)

## Authors

* **Marek Mackiewicz** - [marej.dev@gmail.com](https://github.com/lasagnu)

