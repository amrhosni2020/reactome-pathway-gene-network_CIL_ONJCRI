# Reactome Pathway-Gene Network Visualization

An interactive bipartite network visualization showing the relationships between **IL-6/STAT3 key genes** and their associated **Reactome pathways**. This tool enables exploration of pathway-gene connectivity with dynamic filtering, color-coded categories, and fold-change visualization.

## 🔗 Live Interactive

**[Launch the Interactive Visualization](https://amrhosni2020.github.io/reactome-pathway-gene-network_CIL_ONJCRI/)**

## ✨ Features

- **Interactive Network**: Drag nodes to reposition, scroll to zoom, pan to navigate
- **Category Color Coding**: Pathways colored by biological process (Metabolism, Immune, Signaling, etc.)
- **Gene Regulation Colors**: Up-regulated (red) and Down-regulated (blue) genes based on fold change
- **Dynamic Filtering**:
  - Filter by minimum pathway overlap
  - Exclude top-level generic pathways
  - Filter genes by number of pathway connections
  - Filter by specific biological categories
- **Export**: Download network as PNG image
- **Tooltips**: Detailed information on hover for pathways and genes

## 📁 Repository Structure

```
├── docs/                    # GitHub Pages root
│   ├── index.html          # Main interactive visualization
│   ├── data/               # Data files
│   │   ├── Reactomegenepathwayedgekey.csv      # Gene-pathway connections
│   │   ├── Reactomepathwaynodeskey.csv         # Pathway metadata
│   │   ├── Keygenes.csv                        # Key gene list
│   │   ├── AllMacs_sgp_vs_human1.csv           # Gene expression/fold change
│   │   └── Reactome_pathways_process_multilabel.csv  # Pathway category annotations
│   └── .nojekyll           # Disable Jekyll processing
├── excel/                   # Original Excel source files (if any)
├── README.md               # This file
└── LICENSE                 # MIT License
```

## 📊 Data Files

| File | Description |
|------|-------------|
| `Reactomegenepathwayedgekey.csv` | Edge list connecting genes to Reactome pathways |
| `Reactomepathwaynodeskey.csv` | Pathway metadata: name, size, overlap count, description |
| `Keygenes.csv` | List of key genes with regulation direction and metadata |
| `AllMacs_sgp_vs_human1.csv` | Gene expression data with fold change values |
| `Reactome_pathways_process_multilabel.csv` | Pathway biological process category annotations |

## 🔬 Research Context

This visualization was created to explore canonical pathway mapping for IL-6/STAT3 signaling genes. It represents bipartite gene↔pathway connectivity from the Reactome pathway database.

## 📖 Citation

If you use this visualization in your research, please cite:

```
Reactome Pathway-Gene Network Visualization
GitHub Repository: https://github.com/amrhosni2020/reactome-pathway-gene-network_CIL_ONJCRI
```

## 📄 License

- **Code**: MIT License (see [LICENSE](LICENSE))
- **Data**: CC BY 4.0 - Please cite the source when using the data

## 🙏 Acknowledgments

- [Reactome](https://reactome.org/) - Pathway database
- [D3.js](https://d3js.org/) - Visualization library
- Oliver Newton-John Cancer Research Institute (ONJCRI)
