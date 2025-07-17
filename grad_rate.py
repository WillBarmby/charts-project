from utils import make_swarm_plot

# Total Incidence
make_swarm_plot(
            excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
            sheet_name="Graduation Rate",
            score_column="Rate (%)",
            group_column="Comparison School Type",
            title=f"Figure X.X: Percentage of Students who Graduate at Schools Serving at Least Grade 12",
            xlabel="Graduation Rate",
            output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/Graduation_Rate.png",
            figsize=(8,4),
            # xlim=(.4,1.05),
            xlim=(0,1.05),
            ylim=(-.75,1.25),
            dot_size=6.5,
)