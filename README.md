# OctoPrint-ProgressPixel

A plugin to control a strip of NeoPixels (ws2812b) like a progress bar.

## Setup

### Prerequisites

You need a strip of Neopixels of arbitrary length that you are going to control with this. How you wire them up is up to you, but the data line must be attached to the Raspberry Pi along with a connection to ground. For example: 

![wiring example](/uploads/19316fa12e105ec4bd46c0a18d7471c3/ws2812b_rpi_wiring.svg)

### Installation

- Install the plugin via the [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
- Install the `rpi_ws281x` package globally: `sudo pip install rpi_ws281x`
- Add `pi ALL=(ALL) NOPASSWD: ALL` to your sudoers file to allow running the NeoPixel script in the plugin without prompt

### Configuration

Using the settings tab in the OctoPrint webinterface some parameters must/can be changed such as:
- Number of LEDs (required)
- Pin that the strip is connected to (required)
- Brightness
- Background color
- Bar color

### Pin Selection

The default setup uses pin BCM18 (PWM0).

If you are feeling adventurous or definitely need to use another pin, you can find more information on how to control the NeoPixel [here](https://github.com/jgarff/rpi_ws281x)

## License
This project is licensed under the GPLv3 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgements
- Jan Odvárko, for providing the [jscolor](https://github.com/EastDesire/jscolor) library
- [OctoPrint-Enclosure](https://github.com/vitormhenrique/OctoPrint-Enclosure), for giving me the inspiration
