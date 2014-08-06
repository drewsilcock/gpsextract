from __future__ import division
import csv


def write_gps_to_csv(gps_dict, output_fname):
    # Takes a dictionary of photo names and GPS locations and outputs a csv
    # file  with names in first column and GPS latitude, longitude and
    # altitude in the other columns

    with open(output_fname, "wb") as f:
        writer = csv.writer(f)

        writer.writerow(["Photo", "Longitude", "Latitude", "Altitude"])

        for photo_name, gps_data in gps_dict.items():
            writer.writerow([photo_name,
                             gps_data[1],
                             gps_data[0],
                             gps_data[2]])
            # PhotoScan likes to have GPS in different order to everyone else
    return 0


def jpg_to_tif_ext(jpg_dict):
    # Change the filename extension of the photo filenames in photo_dict to
    # .tif instead of .jpg

    _tif_dict = {key.replace("JPG", "tif"): value
                 for key, value in jpg_dict.items()}

    return _tif_dict
