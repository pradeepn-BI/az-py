import Connections

cnx = Connections()


def execute_pipeline():
    try:
        run_response = cnx.adf_client.pipelines.create_run(cnx.resource_group_name, cnx.datafactory_name,
                                                           cnx.pipeline_name, cnx.run_id,
                                                           parameters={})
    except Exception as e:
        print(e)
    if run_response.status != "Success":
        print(f"The pipeline: , {cnx.datafactory_name, cnx.run_id} is failed")
    return run_response.status



