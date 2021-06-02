# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 16:53:57 2021

@author: SAKSHAM
"""
import properties
import boto3

# Local FileFetch
import shutil

# Copy src to dst. (cp src dst)
source = properties.src_loc + properties.forward_slash + properties.source_file_name
destination = properties.dst_loc + properties.forward_slash + properties.target_file_name  # type: str
shutil.copy(source, destination)

print("Copied from $source to $destination")

# S3 File Fetch
resource = boto3.resource('s3',
                          aws_access_key_id=properties.aws_access_key,
                          aws_secret_access_key=properties.aws_secret_access_key)
my_bucket = resource.Bucket(properties.bucket_name)
my_bucket.download_file(properties.source_file_name, destination)

print("Copied from S3:$properties.bucket_name/$properties.source_file_name to $destination")