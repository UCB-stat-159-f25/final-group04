# This is a Makefile

.PHONY: env
env:
	if conda env list | grep -q "final_env"; then \
		conda env update -n final_env -f environment.yml; \
	else \
		conda env create -f environment.yml; \
	fi

.PHONY: all run-notebooks
all: run-notebooks

run-notebooks:
	jupyter nbconvert --to notebook --execute Part1-EDA/EDA.ipynb --inplace
	jupyter nbconvert --to notebook --execute Part2-Prediction/classification.ipynb --inplace

	