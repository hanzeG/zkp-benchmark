from bokeh.plotting import figure, show
from bokeh.models.tickers import FixedTicker
from parser import noir_parser
import os

# Construct the full path to the noir file
data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../noir/bench/results_ave2.json')

mimc_input_length, mimc_prove_times, griffin_input_length,griffin_prove_times,poseidon_input_length, poseidon_prove_times, poseidon2_input_length,poseidon2_prove_times = noir_parser(data_path, 'prove', 'user_time')

print(mimc_input_length, mimc_prove_times, griffin_input_length,griffin_prove_times,poseidon_input_length, poseidon_prove_times, poseidon2_input_length,poseidon2_prove_times)

# create a new plot with a title and axis labels
p = figure(title="Proof generation runtime for Noir", x_axis_label="Input length", y_axis_label="Runtime/ millisecond",width=800, height=600)

# add multiple renderers
p.scatter(mimc_input_length, mimc_prove_times, legend_label="mimc", size=7, marker="triangle",fill_color='navy')
p.line(mimc_input_length, mimc_prove_times, legend_label="mimc", color="navy")

p.scatter(griffin_input_length, griffin_prove_times, legend_label="griffin", size=7, fill_color='deepskyblue')
p.line(griffin_input_length, griffin_prove_times, legend_label="griffin", color="deepskyblue")

p.scatter(poseidon_input_length, poseidon_prove_times, size=7, marker="square", legend_label="poseidon", fill_color="powderblue")
p.line(poseidon_input_length, poseidon_prove_times, legend_label="poseidon", color="powderblue")

p.scatter(poseidon2_input_length, poseidon2_prove_times, legend_label="poseidon2", size=7, marker="plus", fill_color='lightsteelblue')
p.line(poseidon2_input_length, poseidon2_prove_times, legend_label="poseidon2", color="lightsteelblue")

p.legend.location = "top_left"
p.legend.title = "Hash Functions"

p.xaxis.ticker = FixedTicker(ticks=[i for i in range(2, 17)])

p.output_backend = "svg"
# show the results
show(p)