#!/usr/bin/env python

import os
import time
import datetime
from Fetcher import copy_file_from_loc_dir


def files_to_timestamp(path):
    files = [os.path.join(path, f) for f in os.listdir(path)]
    return dict([(f, os.path.getmtime(f)) for f in files])


def file_to_timestamp(src_file_loc):
    try:
        final_dictionary = dict([(src_file_loc, os.path.getmtime(src_file_loc))])
    except WindowsError:
        final_dictionary = dict()
    except:
        final_dictionary = dict()

    return final_dictionary


def watch_local_file(path_to_watch, destination_location, source_type_folder_or_file, hours_to_watch = 0 ,sleep_time = 2):

    print('Watching {source_type} {watch}'.format(source_type= source_type_folder_or_file,
                                                  watch= path_to_watch))

    current_date_and_time = datetime.datetime.now()
    print(current_date_and_time)
    hours_added = datetime.timedelta(hours=hours_to_watch)
    end_date_and_time = current_date_and_time + hours_added
    print(end_date_and_time)

    before = file_to_timestamp(path_to_watch)

    # Below Commented code is to include folder watch

    # if source_type_folder_or_file=="file" : before = file_to_timestamp(path_to_watch)
    # elif source_type_folder_or_file=="folder" : before = files_to_timestamp(path_to_watch)
    # else : sys.exit('source_type_folder_or_file can only be either file or folder type')

    while datetime.datetime.now() < end_date_and_time:
        time.sleep(sleep_time)
        after = file_to_timestamp(path_to_watch)

        added = [f for f in after.keys() if not f in before.keys()]
        removed = [f for f in before.keys() if not f in after.keys()]
        modified = []

        for f in before.keys():
            if not f in removed:
                if os.path.getmtime(f) != before.get(f):
                    modified.append(f)

        if added :
            print('Added: {}'.format(', '.join(added)))
            print('Moving File: {}'.format(', '.join(added)))
            filename = path_to_watch.split("\\")[-1]
            filepath = path_to_watch.replace("\\" + path_to_watch.split("\\")[-1], "")

            destination_filename = destination_location.split("\\")[-1]
            destination_filepath = destination_location.replace("\\" + destination_location.split("\\")[-1], "")
            copy_file_from_loc_dir(filepath, filename, destination_filepath, destination_filename)

        if removed: print('Removed: {}'.format(', '.join(removed)))

        if modified:
            print('modified: {}'.format(', '.join(modified)))
            print('Moving File: {}'.format(', '.join(modified)))
            filename = path_to_watch.split("\\")[-1]
            filepath = path_to_watch.replace("\\" + path_to_watch.split("\\")[-1], "")

            destination_filename = destination_location.split("\\")[-1]
            destination_filepath = destination_location.replace("\\" + destination_location.split("\\")[-1], "")
            copy_file_from_loc_dir(filepath, filename, destination_filepath, destination_filename)

        print(datetime.datetime.now())
        before = after