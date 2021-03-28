import re
from typing import Mapping

import requests

bearer_re = r"index.html\?(.*)"


class Slaves:
    def __init__(self, token: str):
        self.token = token

        # Get bearer
        get = requests.get(
            "https://api.vk.com/method/apps.get",
            params={
                "app_id": 7794757,
                "platform": "ios",
                "v": 5.23,
                "access_token": self.token,
            },
        ).json()
        if "response" not in get:
            raise Exception("invalid response")
        url = get["response"]["mobile_iframe_url"]
        match = re.search(bearer_re, url)
        try:
            self.bearer = match.group(1)
        except:
            raise Exception("can't parse bearer")

    def request(
        self, endpoint: str, query: Mapping = {}, body: Mapping = {}
    ) -> Mapping:
        method = "GET"
        if body != {}:
            method = "POST"
        return requests.request(
            method,
            "https://pixel.w84.vkforms.ru/HappySanta/slaves/1.0.0" + endpoint,
            params=query,
            json=body,
            headers={
                "authorization": "Bearer " + self.bearer,
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
                'origin': 'https://prod-app7794757-c1ffb3285f12.pages-ac.vk-apps.com'
            },
        ).json()

    def start(self, ref_id: int = 0) -> Mapping:
        return self.request("/start", query=({"ref": ref_id} if ref_id != 0 else {}))

    def user(self, id: int = 0) -> Mapping:
        return self.request("/user", query=({"id": id} if id != 0 else {}))

    def slave_list(self, id: int = 0) -> Mapping:
        return self.request("/slaveList", query=({"id": id} if id != 0 else {}))

    def top_users(self) -> Mapping:
        return self.request("/topUsers")

    def sale_slave(self, slave_id: int) -> Mapping:
        return self.request("/saleSlave", body={"slave_id": slave_id})

    def buy_slave(self, slave_id: int) -> Mapping:
        return self.request("/buySlave", body={"slave_id": slave_id})

    def job_slave(self, slave_id: int, job_name: str) -> Mapping:
        return self.request("/jobSlave", body={"slave_id": slave_id, "name": job_name})

    def buy_fetter(self, slave_id: int) -> Mapping:
        return self.request("/buyFetter", body={"slave_id": slave_id})
