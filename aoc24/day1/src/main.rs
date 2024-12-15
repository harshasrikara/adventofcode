use std::fs::File;
use std::io::{self, BufRead};
use std::path::PathBuf;
use std::env;

fn main() -> io::Result<()> {
    // Get the current working directory
    let current_dir = env::current_dir()?;
    
    // Create a path to the input file in the current directory
    let path: PathBuf = current_dir.join("src/input1.txt");

    // Open the file
    let file = File::open(&path)?;

    // Create a buffered reader
    let reader = io::BufReader::new(file);

    // Create two vectors to store the values from each column
    let mut column1: Vec<i32> = Vec::new();
    let mut column2: Vec<i32> = Vec::new();

    // Read the file line by line
    for line in reader.lines() {
        let line = line?;
        let values: Vec<&str> = line.split_whitespace().collect();
        
        if values.len() == 2 {
            // Parse and store the first value
            if let Ok(value1) = values[0].parse::<i32>() {
                column1.push(value1);
            }
            
            // Parse and store the second value
            if let Ok(value2) = values[1].parse::<i32>() {
                column2.push(value2);
            }
        }
    }

    // Sort both columns
    column1.sort();
    column2.sort();

    // Calculate and print the absolute differences
    let mut sum_of_differences: i64 = 0;
    for (_i, (&val1, &val2)) in column1.iter().zip(column2.iter()).enumerate() {
        let diff = (val1 as i64 - val2 as i64).abs();
        sum_of_differences += diff;
        // println!("Index {}: |{} - {}| = {}", i, val1, val2, diff);
    }

    let mut similarity_score: i32 = 0;
    for (_i, &val1) in column1.iter().enumerate() {
        let mut count = 0;
        for (_j, &val2) in column2.iter().enumerate() {
            if val1 == val2 {
                count+=1;
            }
        }

        similarity_score += val1*count;
    }


    // Print the sum of differences
    println!("Sum of all differences: {}", sum_of_differences);

    // Similarity score
    println!("Similarity score: {}", similarity_score);

    Ok(())
}
