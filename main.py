#!/usr/bin/python
# import cherrypy


import restClient as rc
import evolutionMachine as ev

# class HelloWorld(object):
#     @cherrypy.expose
#     def index(self):
#         return "Hello world!"
#
#     @cherrypy.expose
#     def motor(self):
#         return "Motor running"

if __name__ == '__main__':
    _client = rc.RestClient("http://open-evolution-machine.herokuapp.com/data_points.json")
    # _client = rc.RestClient("https://zapier.com/hooks/catch/3r7top/")
    _evm    = ev.EvolutionMachine()

    while True:
        try:
            _data   = _evm.getData()
            print  _data
            #Argh
            print _client.postJson(_data)
            # print _client.postJson(float(str(_data)))
        except ValueError:
            print "Please blank by hitting the button"


