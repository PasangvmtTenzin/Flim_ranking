# scripts/main.py
import argparse
from src import analysis

def main():
    parser = argparse.ArgumentParser(description="Cinematic Impact Analysis")
    parser.add_argument("--gdp_file", type=str, required=True, help="Path to GDP data file (CSV)")
    parser.add_argument("--population_file", type=str, required=True, help="Path to population data file (CSV)")
    parser.add_argument("--start_year", type=int, required=False, help="Start year for analysis")
    parser.add_argument("--end_year", type=int, required=False, help="End year for analysis")
    args = parser.parse_args()

    analysis.perform_analysis(args.gdp_file, args.population_file, args.start_year, args.end_year)

if __name__ == "__main__":
    main()
