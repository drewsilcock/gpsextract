from __future__ import division
import exifread

# Custom imports
import gpsread
import gpswrite

def gpsextract():
    path = "/Users/Guest/Pictures/avon-gorge/Pass-2/geotagged/unmasked"
    
    # Luckily for me, the photographs are sequentially numbered
    photo_names = ["IMG_0{num}_geotag.JPG".format(num=photo_num)
                   for photo_num in range(595, 656)]
    
    # Gather all the GPS data from all the files and put them into a dictionary
    photo_dict = gpsread.process_gps(path, photo_names)
    
    print "GPS metadata successfully extracted from photos."
    
    # Change the extensions of the photo names to .tif from .jpg
    photo_dict = gpswrite.jpg_to_tif_ext(photo_dict)
    
    print "Filename extensions successfully altered from JPG to tif."
    
    # PhotoScan demands that the csv files have extension .txt
    csv_fname = "gps_metadata.txt"
    gpswrite.write_gps_to_csv(photo_dict, csv_fname)
    
    print "Photo names and GPS location successfully written to csv",
    print "file {0}".format(csv_fname)
    
    return 0

if __name__ == "__main__":
    gpsextract()