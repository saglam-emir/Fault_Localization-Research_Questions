# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('ElitisticListPopulation.java', 51), ('ElitisticListPopulation.java', 65)]

Ground_Truth_Answerable: True

- SBFL   ranked 534 statement(s)
- Hybrid ranked 0 statement(s)

> **WARNING**: the hybrid slice matrix's statement universe was empty for this target (every virtual column's dynamic slice was empty or test-code-only). Any rq5.csv rank_best_slice/tie_size_slice values for this bug reflect a slicing failure, not a genuine result - see step2_slicing's log and step3_matrices/slice_matrix_status.csv.

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 1 | ElitisticListPopulation.java:36 | 0.57735 | `private double elitismRate = 0.9;` |
| 2 | 7 | ElitisticListPopulation.java:50 | 0.447214 | `super(chromosomes, populationLimit);` |
| 2 | 7 | ElitisticListPopulation.java:51 | 0.447214 | `this.elitismRate = elitismRate;` |
| 2 | 7 | ListPopulation.java:50 | 0.447214 | `public ListPopulation(final List<Chromosome> chromosomes, final int populationLimit) {` |
| 2 | 7 | ListPopulation.java:51 | 0.447214 | `if (chromosomes.size() > populationLimit) {` |
| 2 | 7 | ListPopulation.java:55 | 0.447214 | `if (populationLimit <= 0) {` |
| 2 | 7 | ListPopulation.java:59 | 0.447214 | `this.chromosomes = chromosomes;` |
| 2 | 7 | ListPopulation.java:60 | 0.447214 | `this.populationLimit = populationLimit;` |
| 9 | 6 | ElitisticListPopulation.java:64 | 0.316228 | `super(populationLimit);` |
| 9 | 6 | ElitisticListPopulation.java:65 | 0.316228 | `this.elitismRate = elitismRate;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|

