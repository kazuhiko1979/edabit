import boto3


def main():

    client = boto3.client(
        "sns",
        aws_access_key_id = "*****",
        aws_secret_access_key = "****",
        region_name = "ap-northeast-1"
    )

    msg_attr = {'AWS.SNS.SMS.SenderID':
                    {
                        'DataType': 'String',
                        'StringValue': 'SenderName'
                    }
                }

    client.publish(
        PhoneNumber="81*****",
        Message="こんにちは！パイソン講座にようこそ！",
        MessageAttributes=msg_attr
    )

    return

if __name__ == '__main__':
    main()