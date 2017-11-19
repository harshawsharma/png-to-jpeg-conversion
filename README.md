# image-conversion (png to jpeg)

This stack triggers a lambda function upon upload of a .png object to a S3 bucket, which is also created during the stack creation.

## Prerequisites

- Create Python Deployment Package  
Download the python file 'lambda_function.py' from this repo and follow the steps in this [AWS Documentation](http://docs.aws.amazon.com/lambda/latest/dg/with-s3-example-deployment-pkg.html#Python) to create the final deployment package.

 
## SAM template creates the following resources:

- 1 Lambda Function
- 1 IAM Role with 2 Policies
- 1 Lambda Trigger, that triggers the created lambda function whenever a .png file is uploaded using the PUTObject call

## High Level Flow

Once setup, this would work as follows

- A PNG image is uploaded to S3 bucket
- This triggers Lambda which converts the image to JPEG and uploads it back to the same bucket
 

## Note

- The lambda code currently does not support converting objects uploaded to a folder in the bucket. The PNG has to be uploaded to the root of the S3 bucket and the converted JPEG will be made available in the same location

