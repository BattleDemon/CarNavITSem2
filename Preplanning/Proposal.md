<div style="text-align: right;"> Dexter Hart </div>
## Project Overview

I intend to design and produce an integrated system for GPS navigation, which will be similar to commercial options such as Garmin, or Navig8r. It will use a Raspberry Pi 5, GPS receiver, and touch screen, for the physical system. While connected with a PyQT UI, and python route calculation using OpenStreetData. It is designed for my own use, as a test of my skills, and to learn new systems. As I should soon get my provisional license, and my car doesn't have a navigation system of its own, along with the restrictions to phone, I found it useful and within my ability to make my own. 

## Research

### Commercial Systems and Other Alternatives

Existing navigation systems form in two categories of hardware and software. With dedicated GPS systems such as Garmin and Navig8r, useing inbuilt GPS receiver, processor, storage, and a touchscreen, combined into a single device. With these devices ranging in price form $100 - $1000, while my system should be around $300, and repurposable in the future. These standalone devices are often used offline, and store their maps locally, but prevents traffic or map updates.

Software such as Google Maps, Waze, and Organic Maps offer a system that utilised your phone or other hardware. With Google Maps and Waze providing features such as live traffic, automatic rerouting, and frequent updates, although these depend on an active internet connection. While Organic Maps, acts fully offline with navigation possible using open street maps similar to my proposed project.
### Data Sources

Navigation systems require detailed geographical data, including roads, intersections, and points of interest. With commercial options such as HERE Technologies, TomTom, and Google Maps offering accurate datasets and other services like traffic information, but their licensing cost range from HERE and TomTom, which offer free initial use but with steep prices if those limits are breach, and google starting at $100 per month causing too many risks especially if my code is inefficient or making too many API calls. This combined with excellent free and open source options been available such as OpenStreetMaps. Which contains roads, intersections, and some additional data, making it susceptible for my needs. Although the quality for some regions can vary, although this shouldn't be as big of a problem since, it will be primarily used within the ACT which has been mapped. 
### Route Calculation Algorithms

Route calculations rely on graph based search algorithms to determine the most efficient path between two locations. Dijkstra's Algorithm is one of the most well known and is generally efficient at finding the optimal routes but can become ineffective on larger road networks. With A* improving on this by less perfectionist search, reducing the number of paths checked while still been usable. More advanced option can also be used, such as a Bidirectional search either A* or Dijkstra's, allowing it to search from start to end and end to start. Along with Contraction Hierarchies, which reduces the use of smaller streets in the algorithm. Companies don't publicly showcase their algorithms, but most are adaptations of A* or Dijkstra's, with some combining historic traffic in the weighting. Due to the scale of this project and complexities in this assignment I will be using A* with possibilities for growth. 

## Core Features / Minimal Viable Product

The core features will consist of an offline navigation system integrating custom hardware and software. The system will be built around a Raspberry Pi 5 with a GPS receiver and touchscreen display. The software will interpret GPS data to determine the user's location and display this position using locally stored OpenStreetMap data through a Qt-based UI. The interface will include destination searching, triggering route calculation.

## Beyond Minimum Viable Product

#### Expanded Route Algorithm
Implement bidirectional and heirachical, and or offline traffic estimations. 
#### Additional UI Features
Be able to have multi destination routes, saved locations, along with other user settings.
#### Voice Instructions
Add "Turn Left", "Turn Right" notifications, require adding a speaker or integration into the cars speaker.
#### 3D Printed Chassis 
3D model and print a chassis designed to mount the system in my car. 

## Timeline

### Timeline of Design

##### Milestone 1: Research and Initial set up 
Start/End Date: Project assigned - 7th August

Research navigation systems and algorithms
Research OpenStreetMap data, format, and download
Setup rough file structure and plan
Setup raspberry pi
Test hardware

##### Milestone 2: Extract data and GPS system
Start/End Date: 7th August - 19th August

Connect GPS to Raspberry Pi
Decode GPS NMEA data
Transform into usable location data
Import and process OpenStreetMap data
link GPS location and map
Test GPS in multiple locations and in differing conditions

##### Milestone 3: Navigation Backend
Start/End Date: 19th August - 3rd September

Create testing node route system
Implement and test A* 
Optimise route calculation 
Test routes using various data / route length

##### Milestone 4: UI and Last MVP
Start/End Date: 3rd - 17th September

Make Qt touchscreen UI
Render map
Display current location
Add destination search
Render route information
Integrate GPS, routing, and UI as one thing
Complete the minimum viable product

##### Milestone 5: Stress Testing and Documenting
Start/End Date: 17th September - 25th 

Test navigation accuracy IRL in many situations
Test different routes, accuracy, and compare to other alternatives
Complete MVP documentation

Steps following MVP might not follow same order as shown and all have same time frame

##### Milestone 6: Stretch Goal - Expanded route Algorithm
Start/End Date: 25th September - 6th November

Implement bidirectional search into testing program
Implement heirachical into testing program
Improve on algorithm and test various cases
Implement into full program

##### Milestone 7: Stretch Goal - Voice Instructions
Start/End Date: 25th September - 6th November

Research into connecting into car speaker or deticated speakers 
Implement best option
Record voice lines
Connect to full system

##### Milestone 8: Stretch Goal - UI Improvements and addional features
Start/End Date: 25th September - 6th November

Research into similar options specifically their UI
Test how other individuals find my UI
Improve on others suggestions
Implement found features 
Implement multi location search
Allow user settings

##### Milestone 9: Stretch Goal - 3D printed chassis
Start/End Date: 25th September - 6th November

Design 3D printed chassis
Print chassis
mount chassis 
Test system in car with chassis
Test system with other drivers


## Bibliography

Codecademy 2025, _A complete guide to Dijkstra’s shortest path algorithm_, _Codecademy_, viewed 6 August 2026, <https://www.codecademy.com/article/dijkstras-shortest-path-algorithm>.

Gakstatter, E 2015, _What exactly is GPS NMEA data?_, _GPS World_, 4 February, viewed 6 August 2026, <https://www.gpsworld.com/what-exactly-is-gps-nmea-data/>.

Garmin 2026, _Garmin product updates_, Garmin.com, viewed 6 August 2026, <https://aoem.garmin.com/>.

GeeksforGeeks 2012, _Dijkstra’s algorithm to find shortest paths from a source to all_, _GeeksforGeeks_, 25 November, viewed 6 August 2026, <https://www.geeksforgeeks.org/dsa/dijkstras-shortest-path-algorithm-greedy-algo-7/>.

GeeksforGeeks 2016, _A* search algorithm_, _GeeksforGeeks_, 16 June, viewed 6 August 2026, <https://www.geeksforgeeks.org/dsa/a-search-algorithm/>.

GeeksforGeeks 2017, _Bidirectional search_, _GeeksforGeeks_, 11 June, viewed 6 August 2026, <https://www.geeksforgeeks.org/dsa/bidirectional-search/>.

Google 2025, _Google maps platform pricing - subscriptions and pay as you go_, _Google Maps Platform_, viewed 6 August 2026, <https://mapsplatform.google.com/pricing/#pay-as-you-go>.

Here 2026, _HERE base plan | location services | pricing | HERE_, _www.here.com_, viewed 6 August 2026, <https://www.here.com/get-started/pricing>.

Lazarsfeld, J 2018, _1-Intro_, Contraction Hierarchies Guide, viewed 6 August 2026, <https://jlazarsfeld.github.io/ch.150.project/sections/1-intro/>.

LazerCo 2026, ‘Laser corporation product feed’, _Laserco.com.au_, viewed 6 August 2026, <https://www.laserco.com.au/brands/navig8r>.

Navigation Systems Authority Network America 2026, _Navigation map data providers: Comparing HERE, TomTom, Google, and others_, Navigation Systems Authority, viewed 6 August 2026, <https://navigationsystemsauthority.com/map-data-providers-comparison/>.

Navone, EC 2020, _Dijkstra’s shortest path algorithm - a detailed and visual introduction_, _freeCodeCamp.org_, 28 September, viewed 6 August 2026, <https://www.freecodecamp.org/news/dijkstras-shortest-path-algorithm-visual-introduction/>.

Open Street Map 2026, _OpenStreetMap_, OpenStreetMap, viewed 6 August 2026, <https://www.openstreetmap.org/#map=11/-35.2891/149.1466>.

Organic Maps 2025, _Organic Maps: Offline Hike, Bike, Trails and Navigation_, _organicmaps.app_, viewed 6 August 2026, <https://organicmaps.app/>.

Patel, A 1997, _Introduction to A*_, _theory.stanford.edu_, viewed 6 August 2026, <https://theory.stanford.edu/~amitp/GameProgramming/AStarComparison.html>.

TomTom 2026, _Pricing_, TomTom Documentation, viewed 6 August 2026, <https://docs.tomtom.com/pricing>.

Waze 2026, _Driving directions, live traffic & road conditions updates_, _Waze_, viewed 6 August 2026, <https://www.waze.com/live-map>.
