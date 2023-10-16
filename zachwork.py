#!/usr/bin/python3
"""
"""

# python3 -m pip install pyyaml
import yaml

def networkreader():

    with open("network_topology.yml", "r") as ntopo:
        return yaml.safe_load(ntopo)  # pass back to the caller python data
