# Jupyter + PySpark + MongoDB

Includes example Jupyter notebook to push data to MongoDB, and a [mongo-express](https://github.com/mongo-express) admin interface. Runs a custom version of [Jupyter PySpark Notebook](https://hub.docker.com/r/jupyter/pyspark-notebook/) container.

## Instructions

1. Clone this repository and `cd` into the directory:

    `git clone https://github.com/mnassrib/online-retail-analysis-with-pyspark.git`

    `cd online-retail-analysis-with-pyspark`

2. Start the docker containers:

    `docker-compose -p jupyter up`

    **NOTE** - three connected container images will be created: `jupyter_pyspark_mongodb`, `mongo` and `mongo-express`. - there's a unique token you'll need to access the Jupyter notebook server.

    The docker-compose terminal will print out a self-authenticating URL, which looks like:

    `http://localhost:8888/?token=3ec30ff8f125a586d9ce83bc225baf1f387dadd2afb2f176`

    Opening that URL will take you to the notebook server.

## Usage

- MongoDB admin interface running at [http://localhost:8081](http://localhost:8081)

- Jupyter server running at [http://localhost:8888](http://localhost:8888)

- Run the `test_report.ipynb` file saved on Jupyter server at [http://localhost:8888/notebooks/test_report.ipynb](http://localhost:8888/notebooks/test_report.ipynb) to create the `online_retail` database in MongoDB, the `retail` collection and to use these data with PySpark 

## Notes

- This configuration has a footprint of 3.39 GB - you could substitute or change statements in `jupyter/Dockerfile`.

- You may run a command inside the `jupyter` docker container as the root user with the following command:

  `docker-compose run --user="root" jupyter pip install pandas`

## Online retail analysis with pyspark
- The `test_report` notebook gives an answer to an evaluation assignment test based on an analysis of an online retail with pyspark.

- The notebook can be viewed on nbviewer: [![nbviewer](https://img.shields.io/badge/render-nbviewer-orange.svg)](https://nbviewer.org/github/mnassrib/online-retail-analysis-with-pyspark/blob/master/jupyter/notebooks/test_report.ipynb)