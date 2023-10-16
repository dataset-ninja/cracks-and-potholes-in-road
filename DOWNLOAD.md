Dataset **Cracks and Potholes in Road** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/z/U/2h/yR4tK8ep87UzaP2nHZHbaWSZqy5NyRDk3ao4cR2AOKOya3Ht8M2vORCRDxjth1KEEusuQV7aNJgI1PZNmbc1ojHK4FxvrXXT0OyKUMf0yBs3HcqpYcWTFOgveFsH.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Cracks and Potholes in Road', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://prod-dcd-datasets-cache-zipfiles.s3.eu-west-1.amazonaws.com/t576ydh9v8-4.zip).