import requests
import six

from six.moves.urllib.parse import urlencode
from six.moves.urllib import parse as urlparse  # pylint: disable=import-error
urljoin = urlparse.urljoin

from st2common.runners.base_action import Action

BASE_URL = 'https://slack.com/api/'


class SlackAction(Action):

    def run(self, **kwargs):
        params = kwargs
        if params.get('token', None) is None:
            params['token'] = self.config['action_token']

        end_point = params['end_point']
        url = urljoin(BASE_URL, end_point)

        http_method = params['http_method']

        headers = {}
        headers['Content-Type'] = 'application/x-www-form-urlencoded'

        def encode_obj(in_obj):

            if isinstance(in_obj, six.text_type):
                return in_obj.encode('utf-8')

            return in_obj

        data = urlencode(encode_obj(params))

        response = requests.post(url=url, headers=headers, data=data)

        results = response.json()

        return results
