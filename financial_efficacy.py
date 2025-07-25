from utils import make_swarm_plot
from config import TEST_SCORE_SUBJECTS as subjects

make_swarm_plot(
        excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
        sheet_name="Regression Results",
        score_column=f"ELA Standard Residuals",
        group_column="Comparison School Type",
        title=f"Figure X.X Residuals for ELA Scores",
        # filter_column={"Assessment": subject},
        xlabel="Residual Scale",
        output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/financial_efficacy/ELA - Residuals Overall.png",
        figsize=(8,4),
        ylim=(-.5,1.5),
        xlim=(-3.05, 3.05),
        dot_size=3,
        format_as_percent=False
        )

make_swarm_plot(
        excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
        sheet_name="Regression Results",
        score_column="Science Standard Residuals",
        group_column="Comparison School Type",
        title=f"Figure X.X Residuals for Science Scores",
        # filter_column={"Assessment": subject},
        xlabel="Residual Scale",
        output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/financial_efficacy/Science - Residuals Overall.png",
        figsize=(8,4),
        ylim=(-.5,1.5),
        xlim=(-3.05, 3.05),
        dot_size=3,
        format_as_percent=False
        )
make_swarm_plot(
        excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
        sheet_name="Regression Results",
        score_column="Math Standard Residuals",
        group_column="Comparison School Type",
        title="Figure X.X Residuals for Math Scores",
        # filter_column={"Assessment": subject},
        xlabel="Residual Scale",
        output_path="/Users/willbarmby/Python-Projects/charts/graphs/financial_efficacy/Math - Residuals Overall.png",
        figsize=(8,4),
        ylim=(-.5,1.5),
        xlim=(-3.05, 3.05),
        dot_size=3,
        format_as_percent=False
        )