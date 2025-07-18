from utils import make_swarm_plot
from config import INCIDENTS_TITLE, INCIDENTS_X_LABEL
# Total Incidence
def run_incidents():
    make_swarm_plot(
                excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
                sheet_name="Total Incidents",
                score_column="Total Incidence",
                group_column="Comparison School Type",
                filter_column="Grade Span",
                filter_value="09-12",
                title=  INCIDENTS_TITLE,
                xlabel= INCIDENTS_X_LABEL,
                output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/Total_Incidence.png",
                figsize=(8,4),
                ylim=(-.5,1.5),
                dot_size=6,
                format_as_percent= False
    )

if __name__ == "__main__":
    run_incidents()