import boto3
import csv
import pandas as pd
from io import StringIO

# import requests
s3 = boto3.client('s3')

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    
    # Initialize an empty list to store dataframes
    
    dfs = []
    
    bucket_name = 'bankmarketingktconverts'
    
    objects = s3.list_objects_v2(Bucket=bucket_name)
    object_count = len(objects['Contents'])
    object_count = int(object_count)
    
    for i in range(1, object_count + 1) :
        url = url = f"https://bankmarketingktconverts.s3.us-west-2.amazonaws.com/predict_df_{i}_convert.csv"
        df = pd.read_csv(url)
        dfs.append(df)
        
    combined_df = pd.concat(dfs, ignore_index=True)
    
    # Save combined_df as a CSV string
    csv_buffer = StringIO()
    combined_df.to_csv(csv_buffer, index=False)
    
    # Upload CSV file to S3 bucket
    s3_filename = 'combined_df.csv'  # Specify the file name in the bucket
    s3.put_object(Body=csv_buffer.getvalue(), Bucket='bankmarketingktcombined', Key=s3_filename)
    print(f"{s3_filename} uploaded to {bucket_name}")
