from __future__ import print_function
import boto3
import os
import sys
import uuid
from PIL import Image
import PIL.Image

s3_client = boto3.client('s3')


def convert_image(image_path, resized_path):
    with Image.open(image_path) as image:
        rgb_image = image.convert('RGB')
        rgb_image.save(resized_path)


def handler(event, context):
    for record in event['Records']:

        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), key)
        s3_client.download_file(bucket, key, download_path)

        key = os.path.splitext(key)[0]
        upload_path = '/tmp/{}{}.jpg'.format(uuid.uuid4(), key)
        convert_image(download_path, upload_path)

        s3_client.upload_file(upload_path, '{}'.format(bucket), 'jpeg/{}.jpg'.format(key))