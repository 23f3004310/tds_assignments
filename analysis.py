import marimo

__generated_with = "unknown"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    slider = mo.ui.slider(1, 22)
    return (slider,)


@app.cell
def _(slider):
    slider
    return


@app.cell
def _(slider):
    number = slider.value
    squared = number ** 2
    (number, squared)
    return number, squared


@app.cell
def _(mo, number, squared):
    # This cell depends on the computed values 
    mo.md(f"""
        ### Dynamic Report  
        - You selected: **{number}**  
        - Its square is: **{squared}**  
        """)
    return


if __name__ == "__main__":
    app.run()
