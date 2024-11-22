# Demo of SAM2 for microscopy imaging
This is a demo of how [SAM2](https://github.com/facebookresearch/sam2/) could be used to segment individual images or stacks of images.

Datasets are from the [(Broad Bioimage Benchmark Collection (BBBC)](https://data.broadinstitute.org/bbbc/). The datasets are available under the Creative Commons Attribution 3.0 license.

The extract_data.py script extracts data from an ome.zarr file and stores the result in a 3D numpy array. Please note that the ome.zarr file is not included in this repository.