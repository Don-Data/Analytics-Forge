from dagster import job, op
from dagster_airbyte import airbyte_sync_op
from dagster_dbt import dbt_run_op

# Step 1: Define an operation for syncing Airbyte data to Snowflake
@op
def sync_airbyte():
    # This would typically be an API call to Airbyte or a trigger mechanism
    # For now, assume Airbyte sync is triggered manually
    print("Syncing Airbyte data...")
    return "Sync complete!"

# Step 2: Define an operation to run dbt
@op
def run_dbt_transforms():
    print("Running dbt transformations...")
    # Here, dbt commands like dbt run could be triggered via subprocess
    return "dbt complete!"

# Step 3: Create the job to define the pipeline
@job
def airbyte_sync_dbt_pipeline():
    airbyte_sync = sync_airbyte()
    dbt_transform = run_dbt_transforms()

    airbyte_sync >> dbt_transform