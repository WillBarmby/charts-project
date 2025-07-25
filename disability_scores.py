from utils import make_swarm_plot
from config import DISABILITY_SCORE_FIG_NUMS, TEST_SCORE_GRADE_SPANS, TEST_SCORE_SUBJECTS
from pathlib import Path

def run_disability_test_scores():
    grade_spans = TEST_SCORE_GRADE_SPANS
    subjects = TEST_SCORE_SUBJECTS
    i = 19

    assert len(DISABILITY_SCORE_FIG_NUMS) == (len(TEST_SCORE_SUBJECTS) * len(TEST_SCORE_GRADE_SPANS)), "mismatched number of fig nums to graphs for score graphs"

    for subject in subjects:
        subject_title = ""
        if subject == "English Language Arts":
            subject_title = "ELA"
        else: 
            subject_title = subject
        for span in grade_spans:
            path = Path(f"/Users/willbarmby/Python-Projects/charts/graphs/disability_scores/disabilities-{subject_title} - {span}.png")
            make_swarm_plot(
                excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
                sheet_name="Disabilities Overall",
                score_column="Percentage of Students at Achievement Level",
                group_column="Comparison School Type",
                filter_column={"Comparison Grade Span": span, "Assessment": subject},
                title=f"Figure B-{i}: {subject_title} Achievement of Student with Disabilities for Schools Serving Grades {span}",
                xlabel="Percentage of Students Below Achievement Level",
                output_path=str(path),
                figsize=(8,4),
                ylim=(-.5,1.5),
                dot_size=7
            )
            if path.exists():
                i += 1
        path = Path(f"/Users/willbarmby/Python-Projects/charts/graphs/disability_scores/disabilities {subject_title} total.png")
        make_swarm_plot(
            excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
            sheet_name="Disabilities Overall",
            score_column="Percentage of Students at Achievement Level",
            group_column="Comparison School Type",
            filter_column={"Assessment": subject},
            title=f"Figure B-{i}: {subject_title} Achievement of Students with Disabilities (All Schools)",
            xlabel="Percentage of Students Below Achievement Level",
            output_path=str(path),
            figsize=(8,4),
            ylim=(-.5,1.5),
            dot_size=4
        )
        if path.exists():
                i += 1

if __name__ == "__main__":
    run_disability_test_scores()