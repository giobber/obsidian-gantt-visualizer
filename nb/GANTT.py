import marimo

__generated_with = "0.16.0"
app = marimo.App(width="medium")

with app.setup:
    import datetime as dt

    import altair
    import marimo as mo
    import polars as pl


@app.cell
def _():
    data = pl.read_csv(".data/table.csv", try_parse_dates=True)
    data = data.with_columns(
        (pl.col("end") + dt.timedelta(days=1)).alias("end"),
        (pl.col("project").str.strip_chars("[]").alias("project")),
    )
    data
    return (data,)


@app.cell
def _(data):
    altair.Chart(data).mark_bar().encode(
        altair.X("start"),
        altair.X2("end"),
        altair.Y("name", sort="id"),
        altair.Color("package", sort="descending"),
    )
    return


if __name__ == "__main__":
    app.run()
