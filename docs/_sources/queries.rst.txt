Queries
=======
The following queries were used for:

* Create final informative table by joining various tables:
TODO


* Fetch the column name in the final table created:
`SELECT column_name from INFORMATION_SCHEMA.columns where table_name = 'final_table3'`

* Fetching the features for datapoints:
`SELECT snapshot_count, total_targets, original_date, num_revision, last_revision, num_releases FROM final_table3`

* Fetching the labels (lifespan) for the datapoints:
`SELECT lifespan from final_table3`


