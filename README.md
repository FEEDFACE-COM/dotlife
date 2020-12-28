# dotlife


## Overview

**dotlife** is a python3 library and scripts to drive lowres pixel displays. Work in Progress.

## HowTo - PanelOLED

The **oledlife** script drives a PanelOLED M8trix display.

### Usage

```
## Usage

  oledlife [-hSWCFPfvV] <MODE> [-h] ...

## Flags
  -S, --serial=               paneloled serial device, default: /dev/ttyusb0
  -W, --nowrite               no writes to paneloled?
  -C, --clear                 clear paneloled?, default: true
  -F, --forever               run continuously?, default: true
  -P, --preview               buffer preview on stdout?
  -f, --framerate=            paneloled update interval (fps), default: 60.0

## Modes
  test, clear, fyi, glider, fill, fire, tunnel, 
  invader, plasma, pulser, scroller, tetris, 
  palette, draft, symbol, clock
```


### Links

*  <https://www.youtube.com/watch?v=CD2jJZe2YUY>


## HowTo - Fluepdot

The **fliplife** script drives a Fluepdot display.

### Usage
```
## Usage

  fliplife [-hHWRCFPfvV] <MODE> [-h] ...

## Flags
  -H, --host                  fluepdot host, default: 87.193.3.53
  -W, --nowrite               no writes to fluepdot?
  -R, --noread                no reads from fluepdot?
  -C, --clear                 clear fluepdot?, default: true
  -F, --forever               run continuously?
  -P, --preview               buffer preview on stdout?
  -f, --framerate             fluepdot update interval (f/s), default: 1.0

## Modes
  test, read, clear, reset, fill, echo, exec, 
  grow, pixel, dots, life, glider, guns, 
  spawn, flueptext, pipe, scroll, clock, 
  smooth, invader

```

### Links


* <https://fluepdot.readthedocs.io/en/latest/>
* <https://github.com/Fluepke/Fluepdot>

