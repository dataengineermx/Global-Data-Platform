




buffer = dataframe_to_buffer(df)

with psycopg.connect(conn_str) as conn:
    with conn.cursor() as cur:
        with cur.copy(
            """
            COPY earthquakes
            FROM STDIN
            WITH (FORMAT csv, HEADER true)
            """
        ) as copy:

            while chunk := buffer.read(65536):
                copy.write(chunk)