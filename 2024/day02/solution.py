import numpy as np

reports = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        report = []
        for level in line.split():
            report.append(int(level))
        reports.append(report)


def safe(report):
    report_diff = np.diff(report)
    if (
        (np.all(0 < report_diff) and np.all(report_diff < 4)) or
        (np.all(-4 < report_diff) and np.all(report_diff < 0))
    ):
        return True
    else:
        return False


# Part One
# --------

safe_reports = []
for report in reports:
    report_diff = np.diff(report)
    if safe(report):
        safe_reports.append(report)

print(len(safe_reports))

# Part Two
# --------

safe_reports_with_dampener = []
for report in reports:
    if safe(report):
        safe_reports_with_dampener.append(report)
    else:
        for i in range(len(report)):
            report_cut = report[:i] + report[i+1:]
            if safe(report_cut):
                safe_reports_with_dampener.append(report)
                break

print(len(safe_reports_with_dampener))
