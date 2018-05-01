from copy import deepcopy
import unittest
import json

import app

BASE_URL = 'http://127.0.0.1:5000/api/v1.0/items'
BAD_ITEM_URL = '{}/5'.format(BASE_URL)
GOOD_ITEM_URL = '{}/2'.format(BASE_URL)


class FlaskTestApi(unittest.TestCase):

    def setUp(self):
        self.backup_items = deepcopy(app.items)
        self.app = app.app.test_client()
        self.app.testing = True

    def test_get_all(self):
        response = self.app.get(BASE_URL)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['items']), 3)

    def test_get_item(self):
        # good url
        response = self.app.get(GOOD_ITEM_URL)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['items'][0]['name'], 'chair')

        # bad url
        response = self.app.get(BAD_ITEM_URL)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)

    def test_post(self):
        item = {'name': 'some_item'}
        response = self.app.post(BASE_URL, data=json.dumps(item), content_type='application/json')
        self.assertEqual(response.status_code, 400)

        item = {'name': 'screen', 'value': 'string'}
        response = self.app.post(BASE_URL, data=json.dumps(item), content_type='application/json')
        self.assertEqual(response.status_code, 400)

        item = {"name": "screen", "value": 200}
        response = self.app.post(BASE_URL, data=json.dumps(item), content_type='application/json')
        self.assertEqual(response.status_code, 201)

        data = json.loads(response.get_data())
        #print(data)
        self.assertEqual(data['item']['name'], 'screen')

    def test_update(self):

        # bad url
        item = {}
        response = self.app.put(BAD_ITEM_URL, data=json.dumps(item), content_type='application/json')
        self.assertEqual(response.status_code, 404)

        # good url, but value not integer
        item = {'value': '30'}
        response = self.app.put(GOOD_ITEM_URL, data=json.dumps(item), content_type='application/json')
        self.assertEqual(response.status_code, 400)

        # good url
        item = {'value': 30}
        response = self.app.put(GOOD_ITEM_URL, data=json.dumps(item), content_type='application/json')
        self.assertEqual(response.status_code, 200)

        # deepcopy. Update of app.items should not affect self.backup_items
        self.assertEqual(self.backup_items[1]['value'], 300)

    def tearDown(self):
        app.items = self.backup_items


if __name__ == '__main__':
    unittest.main()