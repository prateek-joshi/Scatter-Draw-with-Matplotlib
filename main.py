from matplotlib.backend_bases import MouseButton
import matplotlib.pyplot as plt
import numpy as np
import os

ticks = np.linspace(0,100,5)
FILE_PATH = os.path.join('coords.txt')
global click_id, release_id, move_id

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xticklabels(ticks)
ax.set_yticklabels(ticks)
ax.set_xlim(0,100)
ax.set_ylim(0,100)

def write_coords_into_file(path, ix, iy):
    with open(path, 'a+') as fp:
        fp.write(str(ix)+':'+str(iy)+'!')

def on_move(event):
    # get the x and y pixel coords
    x, y = event.xdata, event.ydata
    if event.inaxes:
        ax = event.inaxes  # the axes instance
        ax.plot(x, y, '.', color='b')
        fig.canvas.draw()
        write_coords_into_file(FILE_PATH, event.xdata, event.ydata)


        # print('data coords %f %f' % (event.xdata, event.ydata))


def on_click(event):
    global move_id, release_id
    release_id = fig.canvas.mpl_connect('button_release_event', onrelease)
    if event.button is MouseButton.LEFT:
        move_id = plt.connect('motion_notify_event', on_move)

def onrelease(event):
    fig.canvas.mpl_disconnect(move_id)

if __name__=='__main__':
    click_id = fig.canvas.mpl_connect('button_press_event', on_click)
    plt.show()
