from utils import make_swarm_plot
from utils import run_t_test
import pandas as pd
from scipy.stats import ttest_ind

# Total Incidence
make_swarm_plot(
            excel_path="/Users/willbarmby/Python-Projects/charts/data.xlsx",
            sheet_name="Graduation Rate",
            score_column="Rate (%)",
            group_column="Comparison School Type",
            title=f"Figure X.X: Four-Year Graduation Rate vs. Type of School",
            xlabel="Graduation Rate {%}",
            output_path=f"/Users/willbarmby/Python-Projects/charts/graphs/Graduation_Rate.png",
            figsize=(8,4),
            xlim=(.4,1.05),
            ylim=(-.75,1.25),
            dot_size=6.5,
)

run_t_test(
    score_column="Rate (%)",
    sheet_name="Graduation Rate"
)

# group_column="Comparison School Type"
# p_value_text = "/Users/willbarmby/Python-Projects/charts/p_vals.txt"

# # Load data
# df = pd.read_excel(excel_path, sheet_name=sheet_name)

# # Drop NA and rename for plotting
# df_plot = df[[score_column, group_column]].dropna()
# df_plot.columns = ['Score', 'Group']

# assert not df_plot.empty, "No data to plot."

# charter_schools = df_plot[df_plot['Group'] == 'Charter']['Score']
# non_charter_schools = df_plot[df_plot['Group'] == 'Non Charter']['Score']

# t_test, p_value = ttest_ind(charter_schools, non_charter_schools, equal_var=False)

# p_value_text = "/Users/willbarmby/Python-Projects/charts/p_vals.txt"
# with open(p_value_text, mode='w',) as f:
#     f.write(f"the p value for graduation rate differences:{p_value}")


