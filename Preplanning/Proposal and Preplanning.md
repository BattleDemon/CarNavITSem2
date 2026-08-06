<div style="text-align: right;"> Dexter Hart </div>
## Project Overview

I intend to design and produce an integrated system for GPS navigation, which will be similar to commercial options such as Garmin, or Navig8r. It will use a Raspberry Pi 5, GPS receiver, and touch screen, for the physical system. While been connected with a PyQT based UI, and python route calculation using OpenStreetData. It is mainly designed for my own use, as a test of my skills, and to learn new systems. As I should soon get my provisional license, and my car doesn't have a navigation system of its own, along with the restrictions to phone, I found it useful and within my ability to make my own. 

## Research

### Commercial Systems and Other Alternatives

Existing navigation systems form in two categories of hardware devices and software. With dedicated GPS systems such as Garmin and Navig8r, use an inbuilt GPS receiver, processor, storage, and usually a touchscreen, combined into a single device. With these devices ranging greatly in price for $100 to some around $1000, while my whole system should be around $300, while been repurposable in the future. These standalone devices and also often be used offline, as they store their maps locally, although this prevents traffic or map updates.

Software options such as Google Maps, Waze, and Organic Maps offer a system that utilised your phone or other hardware. With Google Maps and Waze providing features such as live traffic, automatic rerouting, and frequent updated maps, although these often depend on an active internet connection. While Organic Maps, acts fully offline with navigation possible using open street maps similar to my proposed project.
### Data Sources

Navigation systems 

### Route Calculation Algorithms

Dijkstra's Algorithm, A*, and Bidirectional search 

## Core Features
### Physical System
The physical system will be made up of:
	A Raspberry Pi 5
	GPS Receiver
	LCD 7" Touch screen display
With the Raspberry Pi acting as the central unit, and the GPS Receiver soldered on, and screen connected through HDMI and USB. 
The whole system will be powered through USB-C wall connected to a USB-C to Cigarette Lighter port. 
### Pi OS Configuration

Change the config.txt which acts as the bios of the raspberry pi, to allow the gps to connect through the gpio pins. Also eventually strip down the Raspberry Pi OS install to just the required packages. Make it automatically launch my app upon booting. 

### GPS Interpretation

Handle incoming GPS NMEA data, either decode into Longitude and Latitude or keep as is (depends on how the OpenStreetData handles gps location)

### UI System
Design a simple UI system that handles the touch screen input. Allow rendering of map, with route highlighting / traced. Display next action eg. "Turn left in 100m". Allow searching of destination and selection. Configurable setting eg. Font Size, UI Scale, ect. 

### Route Algorithm
Implement a version of a popular route algorithm, based on research.

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
