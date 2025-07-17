from utils import make_swarm_plot

make_swarm_plot(
        excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
        sheet_name="Post Secondary Enrollment",
        score_column="Percentage",
        group_column="Comparison School Type",
        title=f"Figure X.X: Post Secondary Enrollment by School Type",
        xlabel="Percentage of Student Who Enroll in a Post-Secondary Institution",
        output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/post_sec_enrollment.png",
        figsize=(8,4),
        ylim=(-.75,1.25),
        dot_size=8
)