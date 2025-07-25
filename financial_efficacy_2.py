from utils import make_swarm_plot
from config import TEST_SCORE_SUBJECTS as subjects
subjects = ["ELA", "Math", "Science"]
for subject in subjects:
    print(f"{subject} Score")
    make_swarm_plot(
        excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
        sheet_name="Per Pupil Spending",
        score_column=f"{subject} Score Normalized",
        group_column="Comparison School Type",
        filter_column={f"{subject} Blank": False},
        title=f"Figure X.X Residuals for {subject} Scores",
        xlabel="Residual Scale",
        output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/financial_efficacy/Cost Per Success {subject}.png",
        figsize=(8,4),
        ylim=(-.5,1.5),
        dot_size=2,
        format_as_percent=False
        )
