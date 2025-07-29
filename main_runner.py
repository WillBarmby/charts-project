from chronic_absenteeism import run_chronic_absent_grades, run_chronic_absent_total
from grad_rate import run_grad_rate
from incidents import run_incidents
from PSE import run_post_sec_enroll
from test_scores import run_test_scores
from disability_scores import run_disability_test_scores
from financial_efficacy import run_financial_efficacy
if __name__ == "__main__":
    run_chronic_absent_grades()
    run_chronic_absent_total()
    run_post_sec_enroll()
    run_grad_rate()
    run_incidents()
    run_test_scores()
    run_disability_test_scores()
    run_financial_efficacy()