from azure.storage.filedatalake import (
    DataLakeServiceClient)
import DataLake
import Blob




def upload_download_sample():
    try:
        global service_client

        service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
            "https", 'azdlsgrpdevrubixbi'),
            credential="nmF3vOXT8PHsToYT+ZPCIIbS5LMx+lcGeHkBPtGYHnKYb5qeK0yeDpV2TX9LZzvz0YXGmBT6aCsumv6QMYvSMQ==")

    except Exception as e:
        print(e.args)

    try:
        global file_system_client

        file_system_client = service_client.get_file_system_client(file_system="my-file-system")

    except Exception as e:
        print(e)
    file_system_client.create_directory("landing")
    #print([(i.name, i.is_directory) for i in file_system_client.get_paths("")])
    #print(file_system_client.get_directory_client('incoming'))

    data = """name,population
    Berlin, 3406000
    Munich, 1275000
    """

    file_client = file_system_client.create_file("cities.txt")
    file_client.append_data(data, 0, len(data))

    # data is only committed when flush is called
    file_client.flush_data(len(data))

    # read the data back
    print("Downloading data from '{}'.".format('cities.txt'))
    downloaded_bytes = file_client.read_file()

    # verify the downloaded content#


#DataLake.upload_file_to_directory()
Blob.ContainerClient()

