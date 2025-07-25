import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import seaborn as sns
from config import TEST_SCORE_SUBJECTS, TEST_SCORE_GRADE_SPANS as grade_spans
plt.rcParams['font.family'] = 'Georgia'
def make_swarm_plot_auto_adjusting(
    excel_path,
    sheet_name,
    score_column,
    group_column,
    filter_column=None,
    filter_value=None,
    title="Swarm Plot",
    xlabel="Score",
    ylabel="School Type",
    output_path="swarm_plot.png",
    ylim=(-0.5, 1.5),
    figsize=(8, 2.8),
    title_pad=20,
    bottom_margin=0.3,
    top_margin=0.8,
    dot_size=6,
    format_as_percent=True
):
    # Load data
    df = pd.read_excel(excel_path, sheet_name=sheet_name)

    # Validate group column
    if not set(df[group_column].unique()).issubset({'Charter', 'Non Charter'}):
        raise ValueError(f"Unexpected group values in '{group_column}'.")

    # Create output folder if necessary
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Apply filters
    if isinstance(filter_column, dict):
        for col, val in filter_column.items():
            df = df[df[col] == val]
    elif filter_column and filter_value:
        df = df[df[filter_column] == filter_value]

    # Prepare plot data
    df_plot = df[[score_column, group_column]].dropna()
    df_plot.columns = ['Score', 'Group']
    if df_plot.empty:
        print("No data to plot.")
        return

    # Dynamic x-axis limits
    x_min = df_plot["Score"].min()
    x_max = df_plot["Score"].max()
    x_range = x_max - x_min if x_max > x_min else 1
    x_pad = 0.05 * x_range
    xlim = (x_min - x_pad, x_max + x_pad)

    # Set order
    group_display_order = ["Non Charter", "Charter"]

    # Plot
    fig, ax = plt.subplots(figsize=figsize)

    sns.swarmplot(
        data=df_plot,
        x="Score",
        y="Group",
        order=group_display_order,
        size=dot_size,
        palette={"Charter": (1.0, 200/250, 0.0), "Non Charter": (5/250, 86/250, 165/250)},
        edgecolor="black",
        linewidth=0.5,
        ax=ax,
        hue="Group",
        legend=False
    )

    # Add vertical lines at group means
    for group in group_display_order:
        group_scores = df_plot[df_plot["Group"] == group]["Score"]
        if not group_scores.empty:
            avg = group_scores.mean()
            y_center = group_display_order.index(group)
            line_height = 0.15
            ax.vlines(
                x=avg,
                ymin=y_center - line_height,
                ymax=y_center + line_height,
                color="black",
                linewidth=1.8,
                alpha=0.9
            )

    # Format plot
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_title(title, fontsize=14, pad=title_pad, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    if format_as_percent:
        ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0, decimals=0))
    ax.grid(axis='x', linestyle='--', alpha=0.5)

    ax.set_yticks([0, 1])
    ax.set_yticklabels(ax.get_yticklabels(), fontsize=12, fontweight='normal')
    ax.yaxis.set_label_coords(-0.15, 0.50)

    # Finalize and save
    plt.subplots_adjust(top=top_margin, bottom=bottom_margin)
    plt.tight_layout()
    plt.savefig(output_path, dpi=600, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")

def make_swarm_plot(
    excel_path,
    sheet_name,
    score_column,
    group_column,
    filter_column=None,
    filter_value=None,
    title="Swarm Plot",
    xlabel="Score",
    ylabel="School Type",
    output_path="swarm_plot.png",
    ylim=(-0.5, 1.5),
    figsize=(8, 2.8),
    title_pad=20,
    bottom_margin=0.3,
    top_margin=0.8,
    dot_size=6,
    format_as_percent=True
):
    import os
    import pandas as pd
    import matplotlib.pyplot as plt
    import matplotlib.ticker as mtick
    import seaborn as sns

    # Load data
    df = pd.read_excel(excel_path, sheet_name=sheet_name)

    # Validate group column
    if not set(df[group_column].unique()).issubset({'Charter', 'Non Charter'}):
        raise ValueError(f"Unexpected group values in '{group_column}'.")

    # Create output folder if necessary
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Apply filters
    if isinstance(filter_column, dict):
        for col, val in filter_column.items():
            df = df[df[col] == val]
    elif filter_column and filter_value:
        df = df[df[filter_column] == filter_value]

    # Prepare plot data
    df_plot = df[[score_column, group_column]].dropna()
    df_plot.columns = ['Score', 'Group']
    if df_plot.empty:
        print("No data to plot.")
        return

    # Dynamic x-axis limits
    x_min = df_plot["Score"].min()
    x_max = df_plot["Score"].max()
    x_range = x_max - x_min if x_max > x_min else 1
    x_pad = 0.05 * x_range
    xlim = (x_min - x_pad, x_max + x_pad)

    # Set order
    group_display_order = ["Non Charter", "Charter"]

    # Plot
    fig, ax = plt.subplots(figsize=figsize)

    sns.swarmplot(
        data=df_plot,
        x="Score",
        y="Group",
        order=group_display_order,
        size=dot_size,
        palette={"Charter": (1.0, 200/250, 0.0), "Non Charter": (5/250, 86/250, 165/250)},
        edgecolor="black",
        linewidth=0.5,
        ax=ax,
        hue="Group",
        legend=False
    )

    # Add vertical lines at group means
    for group in group_display_order:
        group_scores = df_plot[df_plot["Group"] == group]["Score"]
        if not group_scores.empty:
            avg = group_scores.mean()
            y_center = group_display_order.index(group)
            line_height = 0.15
            ax.vlines(
                x=avg,
                ymin=y_center - line_height,
                ymax=y_center + line_height,
                color="black",
                linewidth=1.8,
                alpha=0.9
            )

    # Format plot
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_title(title, fontsize=14, pad=title_pad, fontweight='bold')
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    if format_as_percent:
        ax.xaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0, decimals=0))
    ax.grid(axis='x', linestyle='--', alpha=0.5)

    ax.set_yticks([0, 1])
    ax.set_yticklabels(ax.get_yticklabels(), fontsize=12, fontweight='normal')
    ax.yaxis.set_label_coords(-0.15, 0.50)

    # ✏️ Add right-hand annotations safely outside plot
    annotation_x = xlim[1] + 0.02 * x_range  # slight offset outside the visible area
    for i, group in enumerate(group_display_order):
        group_data = df_plot[df_plot["Group"] == group]
        if group_data.empty:
            print(f"No data for group: {group}")
            continue
        n = group_data.shape[0]
        avg = group_data["Score"].mean()
        if format_as_percent:
            annotation_text = f"n = {n}\navg = {avg:.0%}"
        else:
            annotation_text = f"n = {n}\navg = {avg:.2f}"

        ax.text(
            annotation_x, i,
            annotation_text,
            va='center',
            fontsize=12,
            fontstyle='italic'
        )

    # Finalize and save
    plt.subplots_adjust(top=top_margin, bottom=bottom_margin)
    plt.tight_layout()
    plt.savefig(output_path, dpi=600, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")


def run_financial_efficacy():
    h = 0
    subjects = [""] * 3
    for subject in TEST_SCORE_SUBJECTS:
        if subject == "English Language Arts":
            subjects[h] = "ELA"
        else:
            subjects[h] = subject
        h += 1

    i = 1
    for subject in subjects:
        for span in grade_spans:
            make_swarm_plot(
                excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
                sheet_name="Per Pupil Spending",
                score_column=f"{subject} Score",
                group_column="Comparison School Type",
                filter_column={f"{subject} Blank": False, "Comparison Grade Span": span},
                title=f"Figure F-{i}: Financial Efficacy of {subject} Achievement for Schools Serving Grades {span}",
                xlabel="Cost per Successful Student Outcome (USD)",
                output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/fe/Cost Per Success {subject} - {span}.png",
                figsize=(8, 4),
                ylim=(-0.5, 1.5),
                dot_size=5,
                format_as_percent=False
            )
            i += 1

        make_swarm_plot(
            excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
            sheet_name="Per Pupil Spending",
            score_column=f"{subject} Score",
            group_column="Comparison School Type",
            filter_column={f"{subject} Blank": False},
            title=f"Figure F-{i}: Financial Efficacy of {subject} Achievement (All Schools)",
            xlabel="Normalized Cost per Successful Student Outcome (USD)",
            output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/fe/Cost Per Success {subject} total.png",
            figsize=(8, 4),
            ylim=(-0.5, 1.5),
            dot_size=2,
            format_as_percent=False
        )
        i += 1


if __name__ == "__main__":
    run_financial_efficacy()
