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
    data = pl.read_csv(".data/Work Packages.csv", try_parse_dates=True)
    data = data.with_columns(
        (pl.col("due") + dt.timedelta(days=1)).alias("due"),
        (pl.col("project").str.strip_chars("[]").alias("project")),
    )
    data
    return (data,)


@app.cell
def _(data):
    altair.Chart(data).mark_bar().encode(x="start", x2="due", y="name", color="project")
    return


if __name__ == "__main__":
    app.run()
