import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import os
from scipy.stats import ttest_ind

# Set global font
plt.rcParams['font.family'] = 'Georgia'

def make_swarm_plot(
    excel_path,
    sheet_name,
    score_column,
    group_column,
    filter_column=None,  # Can now be dict for multiple filters
    filter_value=None,   # Legacy support
    title="Swarm Plot",
    xlabel="Percentage",
    ylabel="School Type",
    output_path="swarm_plot.png",
    xlim=(-.05, 1),
    ylim=(-0.5, 1.5),
    figsize=(8, 2.8),
    title_pad=20,
    bottom_margin=0.3,
    top_margin=0.8,
    dot_size = 6,
    format_as_percent = True
    ):
    # Load data
    df = pd.read_excel(excel_path, sheet_name=sheet_name)

    # Validate group values
    if not set(df[group_column].unique()).issubset({'Charter', 'Non Charter'}):
        raise ValueError(f"Unexpected group values found in '{group_column}'. Only 'Charter' and 'Non Charter' allowed.")
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True,)
    # Apply filters
    if isinstance(filter_column, dict):
        for col, val in filter_column.items():
            df = df[df[col] == val]
    elif filter_column and filter_value:
        df = df[df[filter_column] == filter_value]

    # Drop NA and rename for plotting
    df_plot = df[[score_column, group_column]].dropna()
    df_plot.columns = ['Score', 'Group']

    if df_plot.empty:
        print("No data to plot.")
        return
    # Define order
    group_display_order = ["Non Charter", "Charter"]

    # Plot
    fig, ax = plt.subplots(figsize=figsize)

    sns.swarmplot(
        data=df_plot,
        x="Score",
        y="Group",
        order=group_display_order,
        size= dot_size,
        palette={"Charter": (1.0, 200/250, 0.0), "Non Charter": (5/250, 86/250, 165/250)},
        edgecolor="black",
        linewidth=0.5,
        ax=ax,
        hue="Group",
        legend=False
    )
    

    # Add short black vertical lines at group averages
    for group in group_display_order:
        group_scores = df_plot[df_plot["Group"] == group]["Score"]
        if not group_scores.empty:
            avg = group_scores.mean()
            y_center = group_display_order.index(group)
            line_height = 0.15  # Adjust to taste: height of vertical bar

            ax.vlines(
                x=avg,
                ymin=y_center - line_height,
                ymax=y_center + line_height,
                color="black",
                linewidth=1.8,
                alpha=0.9
            )


    # Format
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_title(title, fontsize=14, pad=title_pad, fontweight ='bold')
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    if format_as_percent:
        ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0, decimals=0))
    ax.grid(axis='x', linestyle='--', alpha=0.5)

    ax.set_yticks([0, 1])
    ax.set_yticklabels(ax.get_yticklabels(), fontsize=12, fontweight='normal')
    
    ax.yaxis.set_label_coords(-0.15, 0.60)  


    for i, group in enumerate(group_display_order):
        group_data = df_plot[df_plot["Group"] == group]
        if group_data.empty:
            print(f"no data for {group}")
            return
        n = group_data.shape[0]
        avg = group_data["Score"].mean()
        if format_as_percent:
            ax.text(
                1.02, i,
            f"n = {n}\navg = {avg:.0%}",
                transform=ax.get_yaxis_transform(),
                va='center',
                fontsize=12,
                fontstyle='italic'
            )
        else:
            ax.text(
                1.02, i,
            f"n = {n}\navg = {avg:.2f}",
                transform=ax.get_yaxis_transform(),
                va='center',
                fontsize=12,
                fontstyle='italic'
            )

        
        
    # Adjust layout
    plt.subplots_adjust(top=top_margin, bottom=bottom_margin)
    plt.tight_layout()
    plt.savefig(output_path, dpi=600, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")

def run_t_test(
    score_column,
    sheet_name,
    excel_path = "/Users/willbarmby/Python-Projects/charts/data.xlsx",
    group_column="Comparison School Type",
    p_value_text = "/Users/willbarmby/Python-Projects/charts/p_vals.txt"
):
    # Load data
    df = pd.read_excel(excel_path, sheet_name=sheet_name)

    # Drop NA and rename for plotting
    df_plot = df[[score_column, group_column]].dropna()
    df_plot.columns = ['Score', 'Group']

    assert not df_plot.empty, "No data to plot."

    charter_schools = df_plot[df_plot['Group'] == 'Charter']['Score']
    non_charter_schools = df_plot[df_plot['Group'] == 'Non Charter']['Score']

    t_test, p_value = ttest_ind(charter_schools, non_charter_schools, equal_var=False)

    p_value_text = "/Users/willbarmby/Python-Projects/charts/p_vals.txt"
    with open(p_value_text, mode='a',) as f:
        f.write(f"the p value for sheet: {sheet_name} : {p_value}\n")
