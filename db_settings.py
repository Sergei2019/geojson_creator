import sqlalchemy


HOST = 'MSKDB'
LOGIN = 'WBDB'
PASS = 'DBWB'

engine = sqlalchemy.create_engine(f"""
        oracle+cx_oracle://{LOGIN}:{PASS}@{HOST}
        """)


query = """
        SELECT
            N_CLUST AS CLUSTER_ID,
            MACRO_CLUSTER,
            SDO_UTIL.TO_WKTGEOMETRY(GEOM) AS geometry
            FROM FEDSON.TEST_CLUSTER_TABLE
        """
