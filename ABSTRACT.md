The authors of the **Cracks and Potholes in Road Images Dataset** address the significant impact of poor road conditions on traffic safety. They note the utilization of vehicles in various countries to survey road information, capturing images that inform highway intervention and maintenance strategies. While these images can identify problems on highways, they often require manual analysis by trained technicians.

They propose the use of image processing and machine learning techniques to automatically identify defects like cracks and potholes. However, to advance research in this domain, a substantial dataset is essential for algorithm training and recognition tests. To facilitate this, the authors have compiled a dataset featuring images of asphalt road defects in Brazil. This dataset serves as a foundation for studying crack and pothole detection using texture descriptors and machine learning algorithms such as Support Vector Machine, K-Nearest Neighbors, and Multi-Layer Perceptron Neural Network.

The authors sourced images from the Brazilian National Department of Transport Infrastructure (NDTI). These images pertain to highways in Espírito Santo, Rio Grande do Sul, and the Federal District. They manually selected 2235 images, applying criteria to ensure the absence of vehicles, people, and image defects. Each image in the dataset consists of three masks outlining the vehicle's path, as well as crack and pothole defects.

The authors emphasize the value of this dataset, asserting its utility in training classifiers or neural networks to identify lanes, cracks, or potholes. They propose that various classifiers could be developed to suit specific problem types, contributing to road maintenance through defect recognition. They also highlight the potential of automating the detection and classification of defects in road images, which could expedite the monitoring process and reduce costs.

The authors underscore the significance of vision-based methods, explaining that they offer a cost-effective solution for defect detection using common cameras. The dataset's focus on identifying cracks and potholes is pivotal for maintaining road safety and quality, informing intervention and maintenance strategies.

Detailing the dataset, the authors explain that it comprises images extracted from videos captured by NDTI's Highway Diagnostic Vehicle (HDV). This vehicle is equipped with high-resolution cameras, including a top-mounted camera facing the front and two video cameras. The HDV captures images with minimum resolutions of 4 megapixels every 5 meters and records videos at 30 Frames Per Second (FPS) with a resolution of at least 1280x729.

The images were provided by the NDTI on a hard disk, and with the following characteristics:

* The images were captured between 2014 and 2017; and
* They are images from highways of Espírito Santo state (BR 101, 259, 262, 393, 447, 482 and 484), Rio Grande do Sul state (BR 101, 290 and 386) and Federal District (BR 010, 020, 060, 070, 080 and 251).

The dataset was developed using only the images provided by NDTI. A total of 2235 images were selected manually, considering the following criteria:

1. To count as an image with damaged asphalt, present crack(s) and/or pothole(s);
2. Do not contain vehicles in images;
3. Do not contain people in images; and
4. No problems due to capture, such as defects in colors (colors that do not correspond to the rest of the image) and defects in the image (such as missing parts).

In essence, the authors' dataset addresses the need for comprehensive road defect detection using advanced image processing and machine learning techniques, offering valuable resources for further research and practical applications in road maintenance.
