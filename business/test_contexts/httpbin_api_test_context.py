from utilities.http_util import HttpUtil
from business import config

http_bin_anything_end_point = config.end_points['http_bin_anything']


class HttpBinApiTestContext:
    @staticmethod
    def get_anything():
        return HttpUtil.get(http_bin_anything_end_point)

    @staticmethod
    def post_anything(body=""):
        return HttpUtil.post(http_bin_anything_end_point, body)

