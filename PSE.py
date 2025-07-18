from utils import make_swarm_plot
from config import PSE_TITLE, PSE_X_LABEL
# Total Incidence
def run_post_sec_enroll():
    make_swarm_plot(
                excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
                sheet_name="Post Secondary Enrollment",
                score_column="Percentage",
                group_column="Comparison School Type",
                title= PSE_TITLE,
                xlabel= PSE_X_LABEL,
                output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/PSE.png",
                figsize=(8,4),
                ylim=(-.5,1.5),
                dot_size=6
    )
if __name__ == "__main__":
    run_post_sec_enroll()