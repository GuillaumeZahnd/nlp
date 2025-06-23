import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from termcolor import colored


def nice_colorbar(im, axx):
    divider = make_axes_locatable(axx)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    cbar = plt.colorbar(im, cax=cax)
    return cbar


def pc(key, value, color='blue', break_line=False):
    new_line = '\n' if break_line else ''
    print(colored(key, color) + ': {}{}'.format(value, new_line))
