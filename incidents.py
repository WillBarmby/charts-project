from utils import make_swarm_plot

# Total Incidence
make_swarm_plot(
            excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
            sheet_name="Total Incidents",
            score_column="Total Incidence",
            group_column="Comparison School Type",
            filter_column="Grade Span",
            filter_value="09-12",
            title=f"Figure X.X: Behavioral Incident Rate per Student in Grades 09–12 Schools",
            xlabel="Behavioral Incidents per Student",
            output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/Total_Incidence.png",
            figsize=(8,4),
            ylim=(-.75,1.25),
            dot_size=6,
            format_as_percent= False
)

# make_swarm_plot(
#             excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
#             sheet_name="Violent Incidents With Injury",
#             score_column="Rate Per Total Students",
#             group_column="Comparison School Type",
#             filter_column="Grade Span",
#             filter_value="09-12",
#             title=f"Figure X.X: Rate of Violent Incidents per Student",
#             xlabel="Violent Incidence Rate Per Student",
#             output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/Violent_Incidence.png",
#             figsize=(8,4),
#             ylim=(-.75,1.25),
#             dot_size=3
# )