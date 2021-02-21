# WaimeaBuoy
Python refresher and analysis of Waimea Buoy off the NS of Oahu

Reading data buoy data from National Data Buoy Center (NDCB) Station 51201:
https://www.ndbc.noaa.gov/station_page.php?station=51201

Downloaded data from previous website for years 2007-2019. 2004-2006 recorded less variables and therefore needed to be read differently.

Plenty of fun things to do here... 
Clearly from results, only a portion of the data was collected/analyzed, need to check this out
Change x axis from datapoints to date
Wavelet analysis?
Fourier Transform?
Model the waveheights of future years?
Can add the date from the original txt file to the array containing the data
Other available information in the data that I didn't use (from NDBC website):

"WDIR	Wind direction (the direction the wind is coming from in degrees clockwise from true N) during the same period used for WSPD. 
See Wind Averaging Methods

WSPD	Wind speed (m/s) averaged over an eight-minute period for buoys and a two-minute period for land stations. Reported Hourly. See Wind Averaging Methods.

GST	Peak 5 or 8 second gust speed (m/s) measured during the eight-minute or two-minute period. The 5 or 8 second period can be determined by payload, See the Sensor Reporting, Sampling, and Accuracy section.

WVHT	Significant wave height (meters) is calculated as the average of the highest one-third of all of the wave heights during the 20-minute sampling period. See the Wave Measurements section.

DPD	Dominant wave period (seconds) is the period with the maximum wave energy. See the Wave Measurements section.

APD	Average wave period (seconds) of all waves during the 20-minute period. See the Wave Measurements section.

MWD	The direction from which the waves at the dominant period (DPD) are coming. The units are degrees from true North, increasing clockwise, with North as 0 (zero) degrees and East as 90 degrees. See the Wave Measurements section.

PRES	Sea level pressure (hPa). For C-MAN sites and Great Lakes buoys, the recorded pressure is reduced to sea level using the method described in NWS Technical Procedures Bulletin 291 (11/14/80). ( labeled BAR in Historical files)

ATMP	Air temperature (Celsius). For sensor heights on buoys, see Hull Descriptions. For sensor heights at C-MAN stations, see C-MAN Sensor Locations

WTMP	Sea surface temperature (Celsius). For buoys the depth is referenced to the hull's waterline. For fixed platforms it varies with tide, but is referenced to, or near Mean Lower Low Water (MLLW).

DEWP	Dewpoint temperature taken at the same height as the air temperature measurement.

VIS	Station visibility (nautical miles). Note that buoy stations are limited to reports from 0 to 1.6 nmi.

PTDY	Pressure Tendency is the direction (plus or minus) and the amount of pressure change (hPa)for a three hour period ending at the time of observation. (not in Historical files)

TIDE	The water level in feet above or below Mean Lower Low Water (MLLW)."
