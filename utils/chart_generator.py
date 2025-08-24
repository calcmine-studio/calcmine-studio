import matplotlib.pyplot as plt

def plot_production(df, x_col=None, y_col=None):
    if x_col is None:
        x_col = df.columns[0]
    if y_col is None:
        y_col = df.columns[1]

    fig, ax = plt.subplots()
    ax.plot(df[x_col], df[y_col], marker="o")
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title("Production Over Time")
    return fig
