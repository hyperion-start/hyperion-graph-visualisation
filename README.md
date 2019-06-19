[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/DavidPL1/hyperion-graph-visualisation/graphs/commit-activity)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)

# Hyperion graph visualisation extension

## What is Hyperion

Hyperion is an engine designed to launch and monitor user defined components using YAML configuration files.  
Inspired by [vdemo](https://code.cor-lab.org/projects/vdemo) and [TMuLE](https://github.com/marc-hanheide/TMuLE) (see [vdemo and TMuLE assessment](/DavidPL1/Hyperion/wiki/vdemo-and-TMuLE-assessment))

## How does it work
Hyperion (like TMuLE) is written in Python and utilizes the [tmux library for python](https://github.com/tmux-python/libtmux) to start components in detached sessions. For each host defined in the components a master session is created, in which each component will be started in a window. Components are managed by a main server that delegates commands to slave server instances on remote machines and forwards information to subscribed user interfaces.

## Installation

Run ```pip install . ``` in the main directory to install the graph visualisation extension.

## Quick reference

This library unlocks the graph drawing extension for the hyperion application.
It enables using the ```visual``` mode when validating a configuration.

### Validation mode

```
hyperion --config systems/demo.yaml validate [-h] [--visual]

optional arguments:
  -h, --help  show this help message and exit
  --visual    Generate and show a graph image
```

The validation mode parses the dependencies specified in the component configuration files and checks whether they are all met makes sure the directed dependency graph is acyclic (no circular dependencies) to check if starting all components with their dependencies is possible.
Errors (unmet and circular dependencies) are displayed on the cli.
If the configuration is valid, a list showing the order for a full system start is printed on the cli.
 
By specifying the visual argument, the command will generate an image of the the dependency graph (highlighting errors). *Please note:* if a circular dependency error is detected, the graph will be incomplete because the algorithm won't be able to iterate through the remaining nodes!
<p align="center">
  <img src="https://github.com/hyperion-start/hyperion-core/wiki/img/depgraph_1-122018.png?raw=true" alt="Graph generated with the sample components with missing dependency error (December 2018)"/>
</p>

***Image:*** *Graph generated with the sample components with missing dependency error (December 2018)*

<p align="center">
  <img src="https://github.com/hyperion-start/hyperion-core/wiki/img/depgraph_2-122018.png?raw=true" alt="Graph generated from intermediate scale robotic simulation system (December 2018)"/>
</p>

***Image:*** *Graph generated from intermediate scale robotic simulation system (December 2018)*
