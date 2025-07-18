from utils import make_swarm_plot
from config import TEST_SCORE_SUBJECTS, TEST_SCORE_GRADE_SPANS, TEST_SCORE_FIG_NUMS

def run_test_scores():
    grade_spans = TEST_SCORE_GRADE_SPANS
    subjects = TEST_SCORE_SUBJECTS
    i = 0

    assert len(TEST_SCORE_FIG_NUMS) == (len(TEST_SCORE_SUBJECTS) * len(TEST_SCORE_GRADE_SPANS)), "mismatched number of fig nums to graphs for score graphs"

    for subject in subjects:
        for span in grade_spans:
            make_swarm_plot(
                excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
                sheet_name="All_Together",
                score_column="Percentage of Students at Achievement Level",
                group_column="Comparison School Type",
                filter_column={"Comparison Grade Span": span, "Assessment": subject},
                title=f"Figure {TEST_SCORE_FIG_NUMS[i]}: {subject} Achievement for Schools Serving Grades {span}",
                xlabel="Percentage of Students Below Achievement Level",
                output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/{subject} - {span}.png",
                figsize=(8,4),
                ylim=(-.5,1.5),
                dot_size=7
    )
            i += 1

if __name__ == "__main__":
    run_test_scores()