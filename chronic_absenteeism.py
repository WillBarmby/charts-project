from utils import make_swarm_plot
from config import TOTAL_CHRON_ABSENT_TITLE, CHRON_ABSENT_TITLE, CHRON_ABSENT_X_LABEL, CHRON_ABSENT_GRADE_SPANS, CHRON_ABSENT_FIG_NUMS

def run_chronic_absent_grades():

        assert len(CHRON_ABSENT_GRADE_SPANS) == len(CHRON_ABSENT_FIG_NUMS), "figure numbers don't match up with grade spans"
        for i in range(len(CHRON_ABSENT_GRADE_SPANS)):
                make_swarm_plot(
                        excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
                        sheet_name="Chronic Absenteeism",
                        score_column="Percentage of Students Chronically Absent",
                        group_column="Comparison School Type",
                        filter_column={"Grade Span": CHRON_ABSENT_GRADE_SPANS[i]},
                        title=f"Figure {CHRON_ABSENT_FIG_NUMS[i]}: {CHRON_ABSENT_TITLE} {CHRON_ABSENT_GRADE_SPANS[i]}",
                        xlabel= CHRON_ABSENT_X_LABEL,
                        output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/Chronic_Absenteeism/Chronic_Absenteeism-{CHRON_ABSENT_GRADE_SPANS[i]}.png",
                        figsize=(8,4),
                        ylim=(-.5,1.5),
                        dot_size=7
                )

def run_chronic_absent_total():
        make_swarm_plot(
                excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
                sheet_name="Chronic Absenteeism",
                score_column="Percentage of Students Chronically Absent",
                group_column="Comparison School Type",
                title= TOTAL_CHRON_ABSENT_TITLE,
                xlabel= CHRON_ABSENT_X_LABEL,
                output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/Chronic_Absenteeism/Chronic_Absenteeism-Total.png",
                figsize=(8,4),
                ylim=(-.5,1.5),
                dot_size=3.2
        )

if __name__ == "__main__":
      run_chronic_absent_grades()
      run_chronic_absent_total()
