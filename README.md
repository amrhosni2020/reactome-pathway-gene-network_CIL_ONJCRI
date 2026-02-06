# Reactome Pathway-Gene Network Visualization

An interactive bipartite network linking candidate IL‑6 trans‑signalling–associated genes from our mouse metastasis model to their curated Reactome pathways, enabling pathway–gene exploration with filtering and effect‑direction cues. The gene set is derived from mouse myeloid/macrophage differential expression after selective blockade of IL‑6 trans‑signalling (sgp130/sgp130Fc) and is cross‑referenced to human colorectal cancer liver metastasis datasets, where many of these trans‑signalling–suppressed mouse genes show increased expression relative to normal liver.

## 🔗 Live Interactive

**[Launch the Interactive Visualization](https://amrhosni2020.github.io/reactome-pathway-gene-network_CIL_ONJCRI/)**

##  Features

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

## 📁 Data & Code Structure

```
├── docs/                    # GitHub Pages root
│   ├── index.html          # Main interactive visualization (entry point)
│   ├── data/               # Data files loaded by the app
│   │   ├── Reactomegenepathwayedgekey.csv      # Gene-pathway connections
│   │   ├── Reactomepathwaynodeskey.csv         # Pathway metadata
│   │   ├── Keygenes.csv                        # Key gene list
│   │   ├── AllMacs_sgp_vs_human1.csv           # Gene expression/fold change
│   │   └── Reactome_pathways_process_multilabel.csv  # Pathway category annotations
│   └── .nojekyll           # Disable Jekyll processing
├── excel/                   # Original Excel source files (if any)
├── CITATION.cff            # Citation metadata for GitHub
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

## 👤 Maintainer / Corresponding Contact

**Amr H. Allam, DVM, MRes, PhD**  
Research Officer / Translational Cancer Researcher  
Olivia Newton-John Cancer Research Institute (ONJCRI)  
Melbourne, Victoria, Australia

[Amr.Allam@onjcri.org.au](mailto:Amr.Allam@onjcri.org.au)  
 [LinkedIn](https://linkedin.com/in/amrallam2016)

## 📖 How to Cite

### Using GitHub's Citation Feature

Click **"Cite this repository"** in the sidebar (right side of the GitHub repo page) to get a formatted citation.

### Manual Citation

```
Allam, A. H. (2026). Reactome Pathway–Gene Network Explorer [Software]. 
GitHub. https://github.com/amrhosni2020/reactome-pathway-gene-network_CIL_ONJCRI
```

### BibTeX

```bibtex
@software{Allam_Reactome_Network_2026,
  author = {Allam, Amr H.},
  title = {Reactome Pathway–Gene Network Explorer},
  year = {2026},
  url = {https://github.com/amrhosni2020/reactome-pathway-gene-network_CIL_ONJCRI},
  note = {Interactive visualization tool for pathway-gene connectivity analysis}
}
```

### DOI (Zenodo)

A permanent DOI will be assigned when this repository is archived on Zenodo. The DOI will be added here once available.

## 📄 License

### Code

**MIT License** - See [LICENSE](LICENSE) for details.

The source code (`docs/index.html` and associated scripts) is licensed under the MIT License, allowing free use, modification, and distribution with attribution.

### Data

**CC BY 4.0** - The CSV data files in `docs/data/` are derived from:

- [Reactome](https://reactome.org/) pathway database
- Project-specific gene expression analysis

Please cite the original data sources when using the data:

- Reactome: <https://reactome.org/about/cite>
- This repository (see citation above)

##  Acknowledgments

- [Reactome](https://reactome.org/) - Pathway database
- [D3.js](https://d3js.org/) - Visualization library
- Olivia Newton-John Cancer Research Institute (ONJCRI)

---

**Version:** v0.1.0 (2026-02-06)
