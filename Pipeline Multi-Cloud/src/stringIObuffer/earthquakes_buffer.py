import io

def dataframe_to_buffer(df):
    buffer = io.StringIO()

    df.to_csv(
        buffer,
        index=False,
        header=True
    )

    buffer.seek(0)

    return buffer