import matplotlib.pyplot as plt

class Render(object):
    fig = None
    rows = None
    cols = None

    def __init__(self, rows = 3, cols = 2):
        self.fig = plt.figure()
        self.fig.subplots_adjust(left = 0.05, right = 0.95)
        self.rows = rows
        self.cols = cols

    def drawSubplot(self, data, loc, name = "Default Plot Name", type="scatter",
        xlims = [-100, 100], ylims = [-100, 100], bars = [], log = False):

        self.ax = self.fig.add_subplot(self.rows, self.cols, loc)
        self.ax.set_title(name)

        if(log):
            plt.yscale("log")
        plt.xlim(xlims[0], xlims[1])
        plt.ylim(ylims[0], ylims[1])

        if(type == "scatter"):
            self.ax.scatter(data[0], data[1])
        elif(type == "plot"):
            self.ax.plot(data[0], data[1])
        elif(type == "connect"):
            self.ax.plot(data[0], data[1], '-o')

        for x in bars:
            plt.axvline(x=x, color="red", linestyle="--")

    def show(self):
        mng = plt.get_current_fig_manager()
        mng.full_screen_toggle()
        plt.show()
