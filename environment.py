# from os import environ
#
#
# class Environment:
#     DEV = 'dev'
#     PROD = 'prod'
#
#     URLS = {
#         DEV: 'https://playground.learnqa.ru/api_dev',
#         PROD: 'https://playground.learnqa.ru/api'
#     }
#
#     def __int__(self):
#         try:
#             self.env = environ['ENV']
#         except KeyError:
#             self.env = self.DEV
#
#     def get_base_url(self):
#         if self.env in self.URLS:
#             return self.URLS[self.env]
#         else:
#             raise Exception(f"Unknown value of ENV {self.env}")
#
#
# ENV_OBJECT = Environment()
