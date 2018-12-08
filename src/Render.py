import matplotlib.pyplot as plt

class Render(object):
    fig = None
    rows = None
    cols = None

    def __init__(self, rows = 3, cols = 3):
        self.fig = plt.figure()
        self.rows = rows
        self.cols = cols

    def drawSubplot(self, data, loc, name = "Default Plot Name", xlims = [-100, 100], ylims = [-100, 100]):
        ax = self.fig.add_subplot(self.rows, self.cols, loc)
        ax.set_title(name)
        plt.xlim(xlims[0], xlims[1])
        plt.ylim(ylims[0], ylims[1])
        ax.scatter(data[0], data[1])

    def show(self):
        mng = plt.get_current_fig_manager()
        mng.full_screen_toggle()
        plt.show()
