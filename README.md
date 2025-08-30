AWS Rekognition Image Labeling Script

This project is a simple Python script that demonstrates how to use the AWS SDK for Python (boto3) to interact with Amazon Rekognition. The script analyzes an image stored in an S3 bucket and returns a list of detected labels, such as objects, scenes, and concepts.

 Features

Connects to an AWS S3 bucket to access images.

Uses the Amazon Rekognition detect_labels API to perform image analysis.

Prints the detected labels and their confidence scores to the console.

 Prerequisites

Before you get started, make sure you have the following installed and configured:

Python 3.x

An AWS Account: If you don't have one, you can sign up on the AWS website.

AWS CLI: The AWS Command Line Interface must be installed and configured with your credentials. 

Boto3: The AWS SDK for Python. You can install it using pip:

pip install boto3

 Setup & Usage

Create an S3 Bucket: First, create an S3 bucket to store your images. The bucket name in this example is image-labels-bucket-1234.

Upload an Image: Upload the image you want to analyze to your newly created S3 bucket. The example uses test1.jpg.

Write the Script: Save the following code into a file named image_labels.py.

import boto3

def detect_labels(bucket, photo):
    client = boto3.client('rekognition')

    response = client.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
        MaxLabels=10
    )

    print("Detected labels for " + photo)
    for label in response['Labels']:
        print(f"[{label['Name']}] : [{label['Confidence']:.2f}]%")

def main():
    bucket = "image-labels-bucket-1234"
    photo = "test1.png"

    detect_labels(bucket, photo)

if __name__ == "__main__":
    main()

Run the Script: Open your terminal or command prompt, navigate to the directory where you saved the file, and run the script.

python image_labels.py
