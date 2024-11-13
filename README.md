## CryoET Protein Complex Detection

### 1. Overview
This project focuses on building machine learning algorithms to identify and annotate protein complexes in cryo-electron tomography (*cryoET*) tomograms, 3D images that reveal proteins in their natural cellular environment at near-atomic detail. This work is part of a contribution to a Kaggle competition : [link here](https://www.kaggle.com/competitions/czii-cryo-et-object-identification/overview)

Protein complexes like hemoglobin and keratin are essential for cellular function and critical to human health. Understanding their structure and interactions could lead to breakthroughs in disease treatment. CryoET has the potential to illuminate cellular “dark matter” by showing proteins within complex, crowded environments. However, identifying specific protein complexes in cryoET data remains challenging.

- **Develop generalizable ML models** for automated protein annotation.
- **Contribute to biological research** by identifying proteins that are hard to detect with the human eye.
- **Enable further discoveries in cellular biology** and health sciences by mining the “dark matter” of cellular structures.

### 2. Dataset

To use functionalities of this notebook, please download data by using the kaggle API command 

```shell
kaggle competitions download -c czii-cryo-et-object-identification
```

or manually on the [Dataset section of the competition](https://www.kaggle.com/competitions/czii-cryo-et-object-identification/data)

The dataset consists of cryoET tomograms, standardized and hosted on the cryoET Data Portal (cryoetdataportal.czscience.com). This data is crucial for training and validating models capable of generalizing across complex protein structures.
