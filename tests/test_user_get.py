from Lib.base_case import BaseCase
from Lib.my_requests import MyRequests
from Lib.assertions import Assertions


class TestUserGet(BaseCase):
    def test_get_user_details_no_auth(self):
        response = MyRequests.get('/user/2')

        Assertions.assert_json_has_key(response, 'username')
        Assertions.assert_json_has_not_key(response, 'email')
        Assertions.assert_json_has_not_key(response, 'firstName')
        Assertions.assert_json_has_not_key(response, 'lastName')

    def test_get_user_details_auth_as_same_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post('/user/login', data=data)

        self.auth_sid = self.get_cookie(response1, 'auth_sid')
        self.token = self.get_header(response1, 'x-csrf-token')
        user_id_from_auth_method = self.get_json_value(response1, 'user_id')

        response2 = MyRequests.get(
            f'/user/{user_id_from_auth_method}',
            headers={'x-csrf-token': self.token},
            cookies={'auth_sid': self.auth_sid}
            )
        expected_values = ['username', 'email', 'firstName', 'lastName']
        Assertions.assert_json_has_keys(response2, expected_values)
