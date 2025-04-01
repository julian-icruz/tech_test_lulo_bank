from typing import Dict, Any
from dataclasses import dataclass


@dataclass
class ReportGeneratorAdapter:
    def generate_report(self, profiling_results: Dict[str, Any]) -> str:
        """
        Generates an HTML report from the profiling results.

        Args:
            profiling_results (Dict[str, Any]): A dictionary containing profiling data
                (e.g., descriptive_statistics, missing_values, duplicates, correlations, column_types).

        Returns:
            str: A string with the HTML content of the report.
        """
        html = "<html><head><title>Data Profiling Report</title></head><body>"
        html += "<h1>Data Profiling Report</h1>"

        for key, value in profiling_results.items():
            section_title = key.replace("_", " ").title()
            html += f"<h2>{section_title}</h2>"
            html += f"<pre>{value}</pre>"

        html += "</body></html>"
        return html
