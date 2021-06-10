# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 16:53:57 2021

@author: SAKSHAM
"""

from properties import *
from Fetcher import *


copy_file_from_loc_dir(src_loc, source_filename, dst_loc, target_filename)
copy_file_from_s3(bucket_name, source_filename, dst_loc, target_filename)
copy_file_from_sftp(sftp_remote_path, sftp_source_filename, dst_loc, target_filename)