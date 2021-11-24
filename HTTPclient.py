import requests
class HTTP_Client(): 
    header = None 
    def __init__(self, host): 
        self._session=requests.Session() 
        self._host=host 
        payload = {'key': 'value'} 
        respond=requests.get(host, params=payload) 
        print(respond.url) 
        print(respond.headers) 
        print(respond.request.headers) 
    def set_header(self, header): 
        self.header = header 
        
    def get(self, path, query): 
        return requests.get(self._host + path, headers=self.header, params=query) 
        
    def post(self, path, query): 
        return requests.post(self._host + path, headers=self.header, params=query) 
        
    def __del__(self): 
        self._session.close()