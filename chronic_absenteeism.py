from utils import make_swarm_plot

grade_spans = ["09-12", "07-12", "06-12", "KG-08", "PK-06","PK-08"]

for span in grade_spans:
    make_swarm_plot(
        excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
        sheet_name="Chronic Absenteeism",
        score_column="Percentage of Students Chronically Absent",
        group_column="Comparison School Type",
        filter_column={"Grade Span": span},
        title=f"Figure X.X: Chronic Absenteeism for Grades {span}",
        xlabel="Percentage of Students Chronically Absent",
        output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/Chronic_Absenteeism/Chronic_Absenteeism-{span}.png",
        figsize=(8,4),
        ylim=(-.75,1.25),
        dot_size=8
)
