# -*- coding: utf-8 -*-
"""
Created on Fri Jun  11 12:03:00 2021

@author: SAKSHAM
"""

from properties import *
# S3 File Fetch
import boto3
# Local FileFetch
import shutil
# SFTP File Fetch
import paramiko


# Copy src to dst. (cp src dst)

def copy_file_from_loc_dir(src_loc, source_filename, dst_loc, target_filename):
    shutil.copy(src_loc + forward_slash + source_filename, dst_loc + forward_slash + target_filename)
    print("Copied file from {source} to {destination}.\n".format(source=src_loc + forward_slash + source_filename,
                                         destination =dst_loc + forward_slash + target_filename))


# S3 File Fetch

def copy_file_from_s3(bucket_name, source_filename, dst_loc, target_filename):
    resource = boto3.resource('s3',
                              aws_access_key_id=aws_access_key,
                              aws_secret_access_key=aws_secret_access_key)
    my_bucket = resource.Bucket(bucket_name)
    my_bucket.download_file(source_filename, dst_loc + forward_slash + target_filename)
    print("Copied file from S3:{source} to {destination}.\n".format(source=bucket_name + source_filename,
                                          destination=dst_loc + forward_slash + target_filename))


#SFTP File Fetch

def copy_file_from_sftp(sftp_remote_path, sftp_source_filename, dst_loc, target_filename):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(sftp_hostname, username=sftp_username, password=sftp_password)
    sftp = ssh.open_sftp()
    sftp.get(sftp_remote_path + forward_slash + sftp_source_filename, dst_loc + forward_slash + target_filename)
    sftp.close()
    ssh.close()
    print("Copied file from SFTP:{source} to {destination}.\n"
          .format(source=sftp_remote_path + forward_slash + sftp_source_filename,
                  destination=dst_loc + forward_slash + target_filename))
