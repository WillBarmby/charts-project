from utils import make_swarm_plot
import pandas as pd
from config import GRAD_RATE_TITLE, GRAD_RATE_X_LABEL

def run_grad_rate():
    make_swarm_plot(
                excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
                sheet_name="Graduation Rate",
                score_column="Rate (%)",
                group_column="Comparison School Type",
                title=GRAD_RATE_TITLE,
                xlabel=GRAD_RATE_X_LABEL,
                output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/Graduation_Rate.png",
                figsize=(8,4),
                xlim=(.4,1.05),
                ylim=(-.5,1.5),
                dot_size=6,
    )

if __name__ == "__main__":
    run_grad_rate()