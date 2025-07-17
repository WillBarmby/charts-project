from utils import make_swarm_plot

grade_spans = ["03-06", "03-08", "09-12", "07-12", "06-12"]
subjects = ["Math", "English Language Arts", "Science"]
for subject in subjects:
    for span in grade_spans:
        make_swarm_plot(
            excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
            sheet_name="All_Together",
            score_column="Percentage of Students at Achievement Level",
            group_column="Comparison School Type",
            filter_column={"Comparison Grade Span": span, "Assessment": subject},
            title=f"Figure X.X: {subject} Achievement for Grades {span}",
            xlabel="Percentage of Students Below Achievement Level",
            output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/{subject} - {span}.png",
            figsize=(8,4),
            ylim=(-.75,1.25),
            dot_size=7
)
