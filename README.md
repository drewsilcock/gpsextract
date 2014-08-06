gpsextract
==========

A small Python program to extract the GPS metadata from a series of photos and write it to a csv file.

Currently this serves no purpose for anyone other than me, but I plan on generalising it soon to a simple library for using Python to extract GPS metadata from photos and output them to csv, etc., as it was a more tricky task than I initially imagined.

At the moment, this program takes a series of photos, extracts the metadata and converts it into a simple float in degrees. It then writes this GPS metadata to a csv file, containing photo name, longitude, latitude and altitude as columns.
