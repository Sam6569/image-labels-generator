import boto3

def detect_labels(bucket, photo):
    client = boto3.client('rekognition')

    response = client.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
        MaxLabels=10
    )

    print("Detected labels for " + photo)
    for label in response['Labels']:
        print(f"{label['Name']} : {label['Confidence']:.2f}%")


def main():
    bucket = "image-labels-bucket-1234"   
    photo = "test1.png"                      

    detect_labels(bucket, photo)


if __name__ == "__main__":
    main()
