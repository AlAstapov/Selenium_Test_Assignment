import pytest
import unittest
import json

from business.test_contexts.httpbin_api_test_context import HttpBinApiTestContext


class BlazeMeter(unittest.TestCase):

    _expected_response_fields = ["args", "data", "files", "form", "json", "method", "origin", "url", "headers"]
    _expected_response_headers = ["Accept", "Accept-Encoding", "Content-Type", "Host", "User-Agent", "X-Amzn-Trace-Id"]

    """return message with missing  fields from  the response content"""
    @staticmethod
    def get_not_existing_fields(content, fields):
        message = ''
        for field in fields:
            if field not in content:
                message += f"{field} "

        return message

    @pytest.mark.test_id(100002)
    def test_verify_get_anything(self):
        response = HttpBinApiTestContext.get_anything()
        self.assertEqual(200, response.status_code)

        # check for response missing fields
        content = json.loads(response.content)
        missing_fields_msg = self.get_not_existing_fields(content, self._expected_response_fields)
        self.assertTrue(len(missing_fields_msg) == 0, f"{missing_fields_msg} fields are missed in the response")

        # check response missing headers
        headers = content["headers"]
        missing_headers_msg = self.get_not_existing_fields(headers, self._expected_response_headers)
        self.assertTrue(len(missing_headers_msg) == 0, f"{missing_headers_msg} headers are missed in the response")

    @pytest.mark.test_id(100003)
    def test_verify_post_anything(self):
        post_data = 'Some data'
        response = HttpBinApiTestContext.post_anything(post_data)
        self.assertEqual(200, response.status_code)

        # check for response missing fields
        content = json.loads(response.content)
        missing_fields_msg = self.get_not_existing_fields(content, self._expected_response_fields)
        self.assertTrue(len(missing_fields_msg) == 0, f"{missing_fields_msg} fields are missed in the response")
        self.assertEqual(f'"{post_data}"', content["data"])

        # check response missing headers
        headers = content["headers"]
        missing_headers_msg = self.get_not_existing_fields(headers, self._expected_response_headers)
        self.assertTrue(len(missing_headers_msg) == 0, f"{missing_headers_msg} headers are missed in the response")