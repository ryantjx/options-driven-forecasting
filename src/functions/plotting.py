import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

def plot_dual_axis(df_plot, left_column, right_columns, x_column='timestamp', title=None, 
                   left_label=None, right_label=None, colors=None, figsize=(20, 6),
                   right_columns_labels=None):
    """
    Plot data with dual y-axes: one variable on the left axis and multiple variables on the right axis.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame containing the data to plot
    left_column : str
        Column name for the left y-axis
    right_columns : list
        List of column names for the right y-axis
    x_column : str, default='timestamp'
        Column name for the x-axis
    title : str, optional
        Plot title
    left_label : str, optional
        Label for the left y-axis
    right_label : str, optional
        Label for the right y-axis
    colors : list, optional
        List of colors for the right axis lines
    figsize : tuple, default=(12, 6)
        Figure size (width, height) in inches
    right_columns_labels : list, optional
        Labels for the right columns in the legend (if None, uses column names)
    
    Returns:
    --------
    fig, ax1, ax2 : The figure and axis objects
    """
    df = df_plot.copy()
    # Create figure and primary axis
    fig, ax1 = plt.subplots(figsize=figsize)
    
    # Ensure the x-axis is datetime type
    if pd.api.types.is_datetime64_any_dtype(df[x_column]):
        x = df[x_column]
    else:
        try:
            x = pd.to_datetime(df[x_column], unit='ms')
        except:
            x = df[x_column]
    
    # Plot left axis data
    ax1.plot(x, df[left_column], color='#1f77b4', linewidth=1, label=left_column)
    ax1.set_xlabel('Time')
    
    # Set left y-axis label
    if left_label:
        ax1.set_ylabel(left_label, color='#1f77b4')
    else:
        ax1.set_ylabel(left_column, color='#1f77b4')
    
    # Format ticks on left axis
    ax1.tick_params(axis='y', labelcolor='#1f77b4')
    
    # Create second y-axis
    ax2 = ax1.twinx()
    
    # Default colors if not provided
    if colors is None:
        # Use color cycle excluding blue (which is used for left axis)
        colors = plt.cm.tab10.colors[1:]
        # If we need more colors, cycle through the palette
        if len(right_columns) > len(colors):
            colors = colors * (len(right_columns) // len(colors) + 1)
    
    # Use provided labels or default to column names
    if right_columns_labels is None:
        right_columns_labels = right_columns
    
    # Plot right axis data
    for i, col in enumerate(right_columns):
        color_idx = i % len(colors)
        ax2.plot(x, df[col], color=colors[color_idx], linewidth=1, 
                 label=right_columns_labels[i], alpha=0.4)
    
    # Set right y-axis label
    if right_label:
        ax2.set_ylabel(right_label, color='#ff7f0e')
    else:
        ax2.set_ylabel('/'.join(right_columns_labels[:min(3, len(right_columns_labels))]) + 
                      ('...' if len(right_columns_labels) > 3 else ''), 
                      color='#ff7f0e')
    
    # Format ticks on right axis
    ax2.tick_params(axis='y', labelcolor='#ff7f0e')
    
    # Format x-axis if it's datetime
    if pd.api.types.is_datetime64_any_dtype(x):
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax1.xaxis.set_major_locator(mdates.AutoDateLocator())
        fig.autofmt_xdate()
    
    # Add title if provided
    if title:
        plt.title(title)
    
    # Add grid
    ax1.grid(True, linestyle='--', alpha=0.6)
    
    # Create combined legend
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    # ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', bbox_to_anchor=(0, -0.15),
    #           ncol=min(5, len(lines1) + len(lines2)), frameon=True)
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')
    
    # Adjust layout
    plt.tight_layout()
    
    plt.show()