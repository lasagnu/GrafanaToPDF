import requests

import Config

class GrafanaAPI:
    def __init__(self, api_key, server_address):
        self.api_key = api_key
        self.server_address = server_address
        self.headers = {
            'Content-Type': "application/json",
            'Accept': "application/json",
            'Authorization': "Bearer " + self.api_key
        }

    def get_dashboard_info(self, dashboard_uid):
        '''
        func for obtaining raw dashboard data from Grafana
        :param dashboard_uid:
            ex. url: http://127.0.0.1:3000/d/<dashboard_uid>/dashboard
        :return:
            raw json() GET /api/dashboards/uid/:uid
        '''
        get_dashboard_info_url = f'http://{self.server_address}/api/dashboards/uid/{dashboard_uid}'
        response = {}

        try:
            response = requests.get(url=get_dashboard_info_url, headers=self.headers)
        except Exception as ex:
            print(ex)

        return response.json()

    def get_panel_id(self, dashboard_uid):
        '''
        func for extracting panel IDs and their title from dashboard data
        :param dashboard_uid:
            ex. url: http://127.0.0.1:3000/d/<dashboard_uid>/dashboard
        :return:
            dict {panel_id : panel_title}
        '''
        dashboard_info = self.get_dashboard_info(dashboard_uid)
        panels = dashboard_info["dashboard"]["panels"]

        panel_data = dict()

        for panel in panels:
            panel_id = panel["id"]
            panel_title = panel["title"]
            panel_data[panel_id] = panel_title

        return panel_data

    def panel_image_url(self, dashboard_uid, panel_id, time_range_from='now-1d', time_range_to='now', image_height = Config.Default.Image.height, image_width = Config.Default.Image.width):
        return  f'http://{self.server_address}/render/d-solo/{dashboard_uid}/' \
                f'_?from={time_range_from}&height={str(image_height)}&panelId={panel_id}' \
                f'&theme=light&to={time_range_to}&width={str(image_width)}'

    def dashboard_exists(self, dashboard_uid):
        get_dashboard_info_url = f'http://{self.server_address}/api/dashboards/uid/{dashboard_uid}'
        response = {}

        try:
            response = requests.get(url=get_dashboard_info_url, headers=self.headers)
        except Exception as ex:
            print(ex)

        if response.status_code == 200:
            return True
        else:
            return False

    def get_dashboard_title(self, dashboard_uid):
        get_dashboard_info_url = f'http://{self.server_address}/api/dashboards/uid/{dashboard_uid}'
        response = {}

        try:
            response = requests.get(url=get_dashboard_info_url, headers=self.headers)
            dashboard_title = response.json()["dashboard"]["title"]
        except Exception as ex:
            print(ex)
            dashboard_title = 'Error'

        return dashboard_title

    def get_dashboards_as_dict(self):
        list_all_dashboards = f'http://{self.server_address}/api/search?folderIds=0&query=&starred=false'
        dashboards = dict()

        try:
            response = requests.get(url=list_all_dashboards, headers=self.headers)
            dashboard_list = response.json()

            for dashboard in dashboard_list:
                dash_uid = dashboard['uid']
                dash_title = dashboard['title']
                dashboards[dash_title] = dash_uid

        except Exception as ex:
            print(ex)
            dashboards = dict()
            dashboards['error'] = 'not able to get dashboard list'

        return dashboards
