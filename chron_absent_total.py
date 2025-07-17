from utils import make_swarm_plot
make_swarm_plot(
        excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
        sheet_name="Chronic Absenteeism",
        score_column="Percentage of Students Chronically Absent",
        group_column="Comparison School Type",
        title=f"Figure X.X: Percentage of Students Chronically Absent Overall",
        xlabel="Percentage of Students Chronically Absent",
        output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/Chronic_Absenteeism/Chronic_Absenteeism-Total.png",
        figsize=(8,4),
        ylim=(-.75,1.25),
        dot_size=3.2
)