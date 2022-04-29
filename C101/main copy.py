import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb')as f:
            dbx.files_upload(f.read(),file_to)

def main():
    access_token='**'
    transferData=TransferData(access_token)

    file_from='./test.txt'
    file_to='/test_dropbox/test.txt'

    transferData.upload(file_from,file_to)

main()