import Connections
import csv


class Datalake:
    service_client = Connections.service_client

    def list_directory_contents(self):
        try:
            file_system_client = self.service_client.get_file_system_client(
                file_system="my-file-system")
            paths = file_system_client.get_paths(path="landing")
            for i in file_system_client.get_paths(""):
                print(i.name)
        except Exception as E:
            print(E)

    def read_file_data(self):
        try:
            file_system_client = self.service_client.get_file_client("my-file-system", "landing")
            print(file_system_client)
        except Exception as E:
            print(E)

    def upload_file_to_directory(self):
        try:

            file_system_client = self.service_client.get_file_system_client(file_system="my-file-system")

            directory_client = file_system_client.get_directory_client("landing")

            file_client = directory_client.create_file("CostCentreMapping.csv")
            local_file = open("D:\Test Incremental Load\CostCentreMapping.csv", 'r')

            file_contents = local_file.read()

            file_client.append_data(data=file_contents, offset=0, length=len(file_contents))

            file_client.flush_data(len(file_contents))

        except Exception as e:
            print(e)
