from dagster import ScheduleDefinition
from datetime import time

from orchestration.airbyte_sync_dbt_pipeline import airbyte_sync_dbt_pipeline

# Schedule to run at 6am every day
daily_sync_schedule = ScheduleDefinition(
    job=airbyte_sync_dbt_pipeline,
    cron_schedule="0 6 * * *",  # Every day at 6 AM
)