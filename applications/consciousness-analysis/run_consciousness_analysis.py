import argparse
from tqdm import tqdm
import pandas as pd
from ca.analysis import postprocess_consciousness_analysis
from ca.model import process_batch

def main():
    parser = argparse.ArgumentParser(description="Run consciousness analysis on Sanskrit texts using ByT5-Sanskrit model")
    parser.add_argument("--input-file", required=True, help="Path to the input file containing Sanskrit text")
    parser.add_argument("--mode", required=True, 
                       choices=['consciousness-terms', 'consciousness-concepts', 'consciousness-states', 'consciousness-analysis'], 
                       help="Consciousness analysis mode")
    parser.add_argument("--output-mode", type=str, default="txt", choices=["txt", "tsv"], 
                       help="Output mode. TXT is default, TSV will create analysis-friendly TSV output.")
    parser.add_argument("--output-file", required=True, help="Path to the output file")
    parser.add_argument("--batch-size", type=int, default=20, help="Batch size for processing.")
    args = parser.parse_args()

    batch_size = args.batch_size    

    # Read input file
    with open(args.input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    lines = [line.strip() for line in lines if line.strip()]  # Filter empty lines
    
    print(f"Processing {len(lines)} sentences for {args.mode} analysis...")
    
    # Process batches
    results = []
    for i in tqdm(range(0, len(lines), batch_size), desc="Processing batches"):
        batch = [line.strip() for line in lines[i:i+batch_size]]
        batch_results = process_batch(batch, args.mode)
        results.extend(batch_results)
    
    # Postprocess results for consciousness analysis
    results = [postprocess_consciousness_analysis(result, mode=args.mode) for result in results]
    
    # Write results to output file
    if args.output_mode == "txt":        
        with open(args.output_file, "w", encoding="utf-8") as f:
            for result in results:
                f.write(f"{result}\n")

    elif args.output_mode == "tsv":
        segmentnr_base_name = args.input_file.split("/")[-1].split(".")[0]
        output = pd.DataFrame(columns=["segmentnr", "original", "consciousness_analysis"])
        segmentnrs = [f"{segmentnr_base_name}-{i}" for i in range(len(results))]
        output["segmentnr"] = segmentnrs
        output["original"] = lines
        output["consciousness_analysis"] = results
        output.to_csv(args.output_file, sep="\t", index=False)

    print(f"Consciousness analysis results written to {args.output_file}")
    print(f"Analysis mode: {args.mode}")
    print(f"Processed {len(results)} sentences")

if __name__ == "__main__":
    main()