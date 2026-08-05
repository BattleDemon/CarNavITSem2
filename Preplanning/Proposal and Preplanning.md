<div style="text-align: right;"> Dexter Hart </div>
# Idea Overview

Design and produce an integrated system for use as a GPS navigator, similar to google maps, Waze, ect. Which will use a Raspberry Pi 5, a GPS receiver, and touch screen as the physical system. While been supported by a UI made with QT, a back end for route calculations, and map database. 
# Research

## Commercial Systems and Other Alternatives

## Route Calculation Algorithms

Dijkstra's Algorithm, A*, and Bidirectional search 

## UI Options



# Idea Deep Dive
## Physical System
The physical system will be made up of:
	A Raspberry Pi 5
	GPS Receiver
	LCD 7" Touch screen display
With the Raspberry Pi acting as the central unit, and the GPS Receiver soldered on, and screen connected through HDMI and USB. 
The whole system will be powered through USB-C wall connected to a USB-C to Cigarette Lighter port. 
## Pi OS Configuration

Change the config.txt which acts as the bios of the raspberry pi, to allow the gps to connect through the gpio pins. Also eventually strip down the Raspberry Pi OS install to just the required packages. Make it automatically launch my app upon booting. 

## GPS Interpretation

Handle incoming GPS NMEA data, either decode into Longitude and Latitude or keep as is (depends on how the OpenStreetData handles gps location)

## UI System
Design a simple UI system that handles the touch screen input. Allow rendering of map, with route highlighting / traced. Display next action eg. "Turn left in 100m". Allow searching of destination and selection. Configurable setting eg. Font Size, UI Scale, ect. 

## Route Algorithm
Implement a version of a popular route algorithm, based on research 

## Beyond Minimum Viable Product
#### Route Algorithms
Either custom make my own route calculating algorithm or implement a range of known route algorithms, with some maybe taking into account average traffic at peak times ect, while still staying offline (so not real time traffic).
#### More Advanced UI and system
Be able to have multi destination routes, or saved locations.
#### Voice Instructions
Pre-recorded "Turn Left", "Turn Right" notifications, would require adding a speaker or integration into the cars speaker.
#### 3D Printed Chassis 
3D model and print a chassis specifically designed to mount this system in my car. 

# Timeline

## GitHub Roadmap

## Timeline of Design

Given 22nd of July

Proposal Due 7th of August

Due 6th of November 
