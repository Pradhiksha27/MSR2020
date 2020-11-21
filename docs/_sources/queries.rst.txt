Queries
=======
The following queries were used for:


.. highlight:: none

* Create final informative table by joining various tables:: 

CREATE TABLE final_table3 
AS
SELECT
    o.id as id,
    count(snap.object_id) as snapshot_count,
    count(snap.target) as total_targets,
    ov.date as original_date,
    count(snap.revisions) as num_revision,
    max(snap.latest_revision) as last_revision,
    count(snap.num_releases) as num_releases,
FROM
    origin o
    JOIN
    origin_visit ov
    ON
    o.is = ov.origin
    JOIN
    (
        SELECT 
            snapshot.object_id as object_id,
            count(snaptarget.revisions) as num_revision,
            count(snaptarget.num_releases) as num_releases,
            max(snaptarget.latest_revision) as latest_revision,
            count(snaptarget.target) as total_targets
        FROM
            snapshot s
            JOIN
            snapshot_branches snapbranch
            ON
            s.object_id = snapbranch.snapshot_id
            JOIN
            (    SELECT
                    sbranch.object_id as object_id,
                    count(rev.revisions) as num_revision,
                    count(rev.num_releases) as num_releases,
                    max(rev.latest_revision) as latest_revision,
                    count(sbranch.target) as total_targets
                FROM
                    snapshot_branch sbranch
                    JOIN
                    (
                        SELECT
                            count(id) as num_releases,
                            r.id as revisions,
                            max(r.date) as latest_revision
                        FROM
                            release rel
                            JOIN
                            revision r
                            ON
                            rel.target = r.id
                        GROUP BY
                            r.id
                    ) AS rev
                ON
                    sbranch.target = rev.id
                GROUP BY
                    sbranch.object_id
            ) AS snaptarget
            ON
            snaptarget.object_id = snapbranch.branch_id
        GROUP BY
            snapshot.object_id
    ) AS snap
    ON
    ov.snapshot_id = snap.object_id
GROUP BY
    o.id;
 


.. highlight:: none

* Fetch the column name in the final table created::

SELECT
    column_name
FROM
    INFORMATION_SCHEMA.columns
WHERE
    table_name = 'final_table3'


.. highlight:: none

* Fetching the features for datapoints::

SELECT
    snapshot_count,
    total_targets,
    original_date,
    num_revision,
    last_revision,
    num_releases
FROM
    final_table3


.. highlight:: none

* Fetching the labels (lifespan) for the datapoints::

SELECT
    lifespan
FROM
    final_table3


