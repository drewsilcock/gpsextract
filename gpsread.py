from __future__ import division
import exifread


def ratio_to_float(ratio):
    # Takes exif tag value ratio as input and outputs float

    if not isinstance(ratio, exifread.utils.Ratio):
        raise ValueError("You passed something to ratio_to_float that isn't "
                         "a GPS ratio.")

    # GPS metadata is given as a number and a density
    return ratio.num / ratio.den


def tag_to_float(gps_tag):
    # Takes GPS exif lat or long tag as input and outputs as simple float in
    # degrees

    if not isinstance(gps_tag, exifread.classes.IfdTag):
        raise ValueError("You passed something to tag_to_float that isn't an "
                         "EXIF tag.")

    _gps_ang = [ratio_to_float(ratio) for ratio in gps_tag.values]

    _gps_float = _gps_ang[0] + _gps_ang[1] / 60 + _gps_ang[2] / 3600

    return _gps_float


def get_gps(photo):
    # Takes exifread photo object as input and outputs a list of the
    # latitude, longitude and altitude as simple floats

    _lat = tag_to_float(photo["GPS GPSLatitude"])
    _long = tag_to_float(photo["GPS GPSLongitude"])
    _alt = ratio_to_float(photo["GPS GPSAltitude"].values[0])

    # If the GPS metadata references South, negate latitude
    if photo["GPS GPSLatitudeRef"].values == "S":
        _lat = -_lat

    # If the GPS metadata references West, negate longitude
    if photo["GPS GPSLongitudeRef"].values == "W":
        _long = -_long

    return [_lat, _long, _alt]


def process_gps(path, photo_names):
    # Takes list of filenames of photos and returns a dictionary containing the
    # name of each photo as keys and a tuple of the GPS latitude, longitude and
    # altitude as the values.

    _fnames = ["{path}/{name}".format(path=path, name=photo_name)
               for photo_name in photo_names]

    _photos = [open(photo_fname, "rb") for photo_fname in _fnames]

    _tags = [exifread.process_file(photo) for photo in _photos]

    _gps_tags = [get_gps(photo) for photo in _tags]

    _photo_gps = {photo_name: gps_data
                  for photo_name, gps_data in zip(photo_names, _gps_tags)}

    return _photo_gps
