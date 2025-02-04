from matplotlib.text import Text

def tidy_axes(ax):
    '''building a function to make my matplotlib figures look a little nicer''' 
    
    # Remove two spines and set color for remaining
    ax.spines['right'].set_visible(False)  # Remove the right vertical line
    ax.spines['top'].set_visible(False)    # Remove the top horizontal line
    ax.spines['left'].set_color((0, 0, 0, 0.3))  # Set the left spine with 50% transparency (alpha = 0.5)
    ax.spines['bottom'].set_color((0, 0, 0, 0.3))  # Set the bottom spine with 50% transparency
    
    # Removes ticks on axes
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')
    
    # Make color of tick labels 0.75
    ax.tick_params(axis='y', labelcolor=(0,0,0,.75))
    ax.tick_params(axis='x', labelcolor=(0,0,0,.75))
    
    # If axis plotted arrays have labels, format legend.
    if ax.get_legend_handles_labels()[-1] != []:
        ax.legend(frameon=False, fontsize=14)
    
    
def append_xticklabel1(ax, unit="keV"):
    
    # This returns a list of Text objects from matplotlib
    currentLabels = ax.get_xticklabels()[1:]
    currentValues = ax.get_xticks()[1:]
    
    # Get last Text Object (x, y, label), extract positions
    lastTextObject = currentLabels[-1]
    lastTextObjectPosition = lastTextObject.get_position()
    x = lastTextObjectPosition[0]
    y = lastTextObjectPosition[1]
    s = lastTextObject.get_text()
    
    # Add unit to new text object and add to currentLabels
    newTextObject = Text(x, y, f"{s} {unit}")
    newTextObject.set_alpha(1)
    currentLabels[-1] = newTextObject
    
    ax.set_xticks(currentValues)
    ax.set_xticklabels(currentLabels)
    
from matplotlib.text import Text

def append_xticklabel2(ax, unit="keV"):
    """
    Appends a unit to the last xtick label on a matplotlib axis and sets alpha.

    Parameters:
    ax : matplotlib.axes.Axes
        The axis object to modify.
    unit : str, optional
        The unit to append to the last xtick label (default is "keV").
    """
    # Get current tick labels and positions, ignoring the first element
    currentLabels = [tick.get_text() for tick in ax.get_xticklabels()][1:]
    currentValues = ax.get_xticks()[1:]
    
    # Update the last label with the unit
    if currentLabels:
        currentLabels[-1] = unit
    
    # Set the updated tick labels and positions
    ax.set_xticks(currentValues)
    ax.set_xticklabels(currentLabels)
    
    # Update alpha for all tick labels
    ax.get_xticklabels()[-1].set_alpha(1)
    ax.get_xticklabels()[-1].set_fontsize(12)
        
