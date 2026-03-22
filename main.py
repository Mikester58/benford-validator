# Pipeline orchestration

"""
1. main.py & data_loader.py ingest the dataset & strip potential symbols.
2. main.py passes cleaned data to profiler.py. Profiler checks the data's characteristics.
3. Based on the profile, main.py decides which tests are valid.
4. main.py calls the appropriate scripts in the detectors/ folder.
5. The results (IE fraud score, flagged rows) are passed to reporter.py, spitting out a final report.
"""

