import requests


class HttpUtil:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        result = requests.get(url,
                              headers=HttpUtil.headers,
                              cookies=HttpUtil.cookie)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url,
                               json=body,
                               headers=HttpUtil.headers,
                               cookies=HttpUtil.cookie)
        return result