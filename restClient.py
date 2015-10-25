import requests as r
import json

class RestClient:
    address = ""
    def __init__(self, _address):
        self.address = _address;

    def postJson(self, _value):
        print "sending" + json.dumps(_value)

        # r.headers['content-type'] = 'application/json'
        result = r.post(url=self.address, json={"data_point":_value})
        # print(result)
        return result


if __name__ == '__main__':
    client = RestClient("http://open-evolution-machine.herokuapp.com/data_points")
    client.postJson({"hi":10});