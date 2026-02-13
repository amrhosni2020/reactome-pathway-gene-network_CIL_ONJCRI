import pandas as pd
import os

# Paths
base_dir = "/Users/allam/Documents/Olivia Newton-John /Papers/1-My publications/Trans-signaling manuscript/CellChat Pathways/Human CellChat/Pathway analysis/App/github-repo/docs/data"
sankey_csv = os.path.join(base_dir, "sankey_data.csv")
edge_csv = os.path.join(base_dir, "Reactomegenepathwayedgekey.csv")
process_csv = os.path.join(base_dir, "Reactome_pathways_process_multilabel.csv")

# Load data
sankey_df = pd.read_csv(sankey_csv)
edge_df = pd.read_csv(edge_csv)
process_df = pd.read_csv(process_csv)

# 1. Extract genes and their manual process from sankey_data
gene_to_manual = {}
for _, row in sankey_df.iterrows():
    manual_proc = row['Process']
    genes_str = str(row['Genes'])
    if genes_str and genes_str != 'nan':
        genes = [g.strip() for g in genes_str.split(',')]
        for g in genes:
            gene_to_manual[g] = manual_proc

# 2. Map genes to Reactome Primary Process
results = []
for gene in gene_to_manual.keys():
    # Find all term_ids for this gene
    term_ids = edge_df[edge_df['gene'] == gene]['term_id'].unique()
    
    # Find processes for these term_ids
    gene_processes = process_df[process_df['term_id'].isin(term_ids)]
    
    # Get unique primary processes
    primary_procs = gene_processes['Process_primary'].unique()
    primary_procs_list = ", ".join([str(p) for p in primary_procs if str(p) != 'nan'])
    
    # Also get specific pathway names for context (top 3)
    pathway_names = gene_processes['pathway_name'].head(3).tolist()
    pathway_names_str = ", ".join(pathway_names)

    results.append({
        "Gene": gene,
        "Manual Classification": gene_to_manual[gene],
        "Reactome Primary Process": primary_procs_list,
        "Example Reactome Pathways": pathway_names_str
    })

# Create final table
final_df = pd.DataFrame(results)

# Clean up Column Names for Markdown
final_df.columns = ["Gene", "Manual Classification (Manuscript)", "Reactome Primary Process", "Top Reactome Pathways"]

# Print as Markdown
print(final_df.to_markdown(index=False))
