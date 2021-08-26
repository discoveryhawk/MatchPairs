import os

if os.environ.get('TOKEN'):
    TOKEN = os.environ.get('TOKEN')
    DeveloperId = os.environ.get('DEVELOPER_ID')
    DataBaseURI = os.environ.get('DataBaseURI')
else:
    TOKEN = '1886839244:AAHk_B_hQlGsVBRe7UJRwsjTc8wKZeO-fm4'
    DeveloperId = 675416572
    DataBaseURI = 'postgres://dhmdqjibvchppj:e2910571f9856c08a8c3737959f7945161d48d3bec1ae79e49978d5ef65344e3@ec2-54' \
                  '-220-195-236.eu-west-1.compute.amazonaws.com:5432/d7b4h4m6g1k28b'
