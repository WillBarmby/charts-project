from utils import make_swarm_plot

# Total Incidence
make_swarm_plot(
            excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
            sheet_name="Post Secondary Enrollment",
            score_column="Percentage",
            group_column="Comparison School Type",
            filter_column="Population",
            filter_value="All Students",
            title=f"Figure X.X: Rate of Post Secondary Enrollment",
            xlabel="Rate of Post Secondary Enrollment",
            output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/PSE.png",
            figsize=(8,4),
            ylim=(-.75,1.25),
            dot_size=6
)
