#!/bin/bash

# Define the path to the dataset
dataset="Global YouTube Statistics.csv"

# Check if the dataset file exists
if [ ! -f "$dataset" ]; then
  echo "Dataset file does not exist."
  exit 1
fi

# Define the output directory
output_dir="United States"

# Check if the 'United States' directory exists
if [ ! -d "$output_dir" ]; then
  echo "Directory 'United States' does not exist."
  exit 1
fi

# Define the categories
categories=("Music" "Entertainment" "Gaming" "Comedy")

# Clear the ws5.txt file before writing
> ws5.txt

# Loop through each category
for category in "${categories[@]}"; do
  # Grep the entries for each category and United States, then count them
  awk -F, -v category="$category" '$8 == "United States" && $5 == category' "$dataset" > "$output_dir/$category.txt"
  count=$(wc -l < "$output_dir/$category.txt")
  echo "$category: $count" >> ws5.txt
done

