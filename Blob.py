from azure.storage.blob import ContainerClient

import Connections

cnx = Connections.sas_token


class Blob:

    def create_container(self):
        container_client = ContainerClient.from_connection_string(
            self.cnx, container_name="myTestcontainer")
        # [END auth_from_connection_string_container]

        # [START auth_from_connection_string_blob]
        from azure.storage.blob import BlobClient
        blob_client = BlobClient.from_connection_string(
            self.cnx, container_name="myTestcontainer", blob_name="pradeepTestblob.txt")
