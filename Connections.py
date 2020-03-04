from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.storage.blob import BlobClient, ContainerClient
from azure.storage.filedatalake import DataLakeServiceClient
from msrestazure.azure_active_directory import ServicePrincipalCredentials



class Connections:
    # Datalake Connections
    try:
        global service_client

        service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
            "https", 'azdlsgrpdevrubixbi'),
            credential="nmF3vOXT8PHsToYT+ZPCIIbS5LMx+lcGeHkBPtGYHnKYb5qeK0yeDpV2TX9LZzvz0YXGmBT6aCsumv6QMYvSMQ==")
    except Exception as e:
        print(e)


# DataFactory Connections
subscription_id = "c597ef8f-9990-4e55-ac28-6da1ddd6ae9e"
resource_group_name = "RG-RBX-WEU-DEV-GRP-BI-RubixBI"
pipeline_name = "PL_Files_LoadTo_ADLS"
datafactory_name = "AZDF-GRPDEV-RUBIXBI"

subscription_id = 'c597ef8f-9990-4e55-ac28-6da1ddd6ae9e'
credentials = ServicePrincipalCredentials(client_id="84c71c22-7e17-46ad-9c89-94142980afe6",
                                          secret="cLhwBQs_n=Ot]0j[eb0jBAnCiDIFGj39",
                                          tenant="7e7582b6-e2aa-455c-8352-be9fd4a411dd")
adf_client = DataFactoryManagementClient(credentials, subscription_id)

# Blob Connections

ContainerClient("https://azbsgrpdevrubixbi.dfs.core.windows.net/", "group", credential=None)
try:
    sas_token = "?sv=2019-02-02&ss=bfqt&srt=sco&sp=rwdlacup&se=2021-03-03T00:14:03Z&st=2020-03-02T16:14:03Z&spr=https&sig=PyGpqF94ywN17Q%2FWvYJgk%2B5fuWRI97LYc8JztL5ZSCk%3D"
    blob_client = BlobClient.from_blob_url(sas_token)
except Exception as e:
    print(e)
