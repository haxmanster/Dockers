import docker
import requests
import random
import json

NETWORK = 'grzegorz'
IMAGE = 'nginx'
NAME = 'nginx_'


class DockerHelper:
   
    def __init__(self):
        self.doc_api = docker.APIClient()

    def container_run(self, start, stop, image=IMAGE,
                      name=NAME, network=NETWORK):
        doc = docker.from_env()

        while start < stop:
            ports = {"80": str(random.randrange(int(1000), int(9999)))}
            container = doc.containers.run(image=image, 
                                           name=name + '{}'.format(start),
                                           ports=ports,
                                           detach=True)
            doc.networks.get(network).connect(container)
            start += 1

    def container_start(self, name):
        self.doc_api.start(name)

    def container_stop(self, name):
        self.doc_api.stop(name)

    def container_remove(self, name):
        self.doc_api.remove_container(name)
    
    def container_list(self):
        doc = docker.from_env()
        doc.containers.list(all, filters={"status": "running"})