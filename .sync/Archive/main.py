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
    _client = rc.RestClient("https://open-evolution-machine.herokuapp.com/data_points.json")
    _evm    = ev.EvolutionMachine()
    _data   = _evm.getData()

    print  _data

    print _client.postJson(_data)


