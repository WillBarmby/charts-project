from utils import make_swarm_plot
from config import DISABILITY_SCORE_FIG_NUMS, TEST_SCORE_GRADE_SPANS, TEST_SCORE_SUBJECTS

def run_disability_test_scores():
    grade_spans = TEST_SCORE_GRADE_SPANS
    subjects = TEST_SCORE_SUBJECTS
    i = 0

    assert len(DISABILITY_SCORE_FIG_NUMS) == (len(TEST_SCORE_SUBJECTS) * len(TEST_SCORE_GRADE_SPANS)), "mismatched number of fig nums to graphs for score graphs"

    for subject in subjects:
        for span in grade_spans:
            make_swarm_plot(
                excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
                sheet_name="Disabilities Scores",
                score_column="Percentage of Students at Achievement Level",
                group_column="Comparison School Type",
                filter_column={"Comparison Grade Span": span, "Assessment": subject},
                title=f"Figure {DISABILITY_SCORE_FIG_NUMS[i]}: {subject} Achievement of Student with Disabilities for Schoools Serving {span}",
                xlabel="Percentage of Students Below Achievement Level",
                output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/disability_scores/disabilities-{subject} - {span}.png",
                figsize=(8,4),
                ylim=(-.75,1.25),
                dot_size=7
    )
            i += 1
    for subject in subjects:
        make_swarm_plot(
            excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
            sheet_name="Disabilities Scores",
            score_column="Percentage of Students at Achievement Level",
            group_column="Comparison School Type",
            filter_column={"Assessment": subject},
            title=f"Figure X.X: {subject} Achievement of Students with Disabilities",
            xlabel="Percentage of Students Below Achievement Level",
            output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/disability_scores/disabilities {subject} total.png",
            figsize=(8,4),
            ylim=(-1.75,2.75),
            dot_size=5
)


if __name__ == "__main__":
    run_disability_test_scores()