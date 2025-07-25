from utils import make_swarm_plot
from config import TEST_SCORE_SUBJECTS, TEST_SCORE_GRADE_SPANS, TEST_SCORE_FIG_NUMS

def run_test_scores():
    grade_spans = TEST_SCORE_GRADE_SPANS
    subjects = TEST_SCORE_SUBJECTS
    i = 0

    # assert len(TEST_SCORE_FIG_NUMS) == (len(TEST_SCORE_SUBJECTS) * len(TEST_SCORE_GRADE_SPANS)) + len(TEST_SCORE_SUBJECTS), "mismatched number of fig nums to graphs for score graphs"

    for subject in subjects:
        subject_title = ""
        if subject == "English Language Arts":
            subject_title = "ELA"
        else: 
            subject_title = subject
        for span in grade_spans:
            make_swarm_plot(
                excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
                sheet_name="All_Together",
                score_column="Percentage of Students at Achievement Level",
                group_column="Comparison School Type",
                filter_column={"Comparison Grade Span": span, "Assessment": subject},
                title=f"Figure B-{i + 1}: {subject_title} Achievement for Schools Serving Grades {span}",
                xlabel="Percentage of Students Below Achievement Level",
                output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/test_scores/{subject_title} - {span}.png",
                figsize=(8,4),
                ylim=(-.5,1.5),
                dot_size=7
    )
            i += 1
        make_swarm_plot(
                excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
                sheet_name="All Together New",
                score_column="Percentage of Students at Achievement Level",
                group_column="Comparison School Type",
                title=f"Figure B-{i + 1}: {subject_title} Achievement for All Schools",
                filter_column={"Assessment": subject},
                xlabel="Percentage of Students Below Achievement Level",
                output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/test_scores/{subject_title} - Overall.png",
                figsize=(8,4),
                ylim=(-.5,1.5),
                dot_size=3
        )
        i += 1


if __name__ == "__main__":
    run_test_scores()