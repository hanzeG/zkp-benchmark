from bokeh.plotting import figure, show
from bokeh.models.tickers import FixedTicker
from parser import noir_parser, snarkjs_parser
import os

# Construct the full path to the noir file
data_path_noir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../noir/bench/results_ave2.json')

data_path_snarkjs = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../snarkjs_bench/bench/results.json')

noir_mimc_input_length, noir_mimc_prove_times, noir_griffin_input_length,noir_griffin_prove_times,noir_poseidon_input_length, noir_poseidon_prove_times, noir_poseidon2_input_length,noir_poseidon2_prove_times = noir_parser(data_path_noir, 'prove', 'user_time')

snarkjs_mimc_input_length, snarkjs_mimc_prove_times, snarkjs_poseidon_input_length, snarkjs_poseidon_prove_times = snarkjs_parser(data_path_snarkjs, 'prove', 'user_time')

# create a new plot with a title and axis labels
p = figure(title="Proof generation runtime with different input length (MBP M1)", x_axis_label="Input length", y_axis_label="Runtime/ millisecond",width=800, height=600)

# add multiple renderers
p.scatter(noir_mimc_input_length, noir_mimc_prove_times, legend_label="mimc/ noir-bb", size=7, marker="triangle",fill_color='navy')
p.line(noir_mimc_input_length, noir_mimc_prove_times, legend_label="mimc/ noir-bb", color="navy")

p.scatter(noir_griffin_input_length, noir_griffin_prove_times, legend_label="griffin/ noir-bb", size=7, fill_color='navy')
p.line(noir_griffin_input_length, noir_griffin_prove_times, legend_label="griffin/ noir-bb", color="navy")

p.scatter(noir_poseidon_input_length, noir_poseidon_prove_times, size=7, marker="square", legend_label="poseidon/ noir-bb", fill_color="navy")
p.line(noir_poseidon_input_length, noir_poseidon_prove_times, legend_label="poseidon/ noir-bb", color="navy")

p.scatter(noir_poseidon2_input_length, noir_poseidon2_prove_times, legend_label="poseidon2/ noir-bb", size=7, marker="plus", fill_color='navy')
p.line(noir_poseidon2_input_length, noir_poseidon2_prove_times, legend_label="poseidon2/ noir-bb", color="navy")

p.scatter(snarkjs_mimc_input_length, snarkjs_mimc_prove_times, legend_label="mimc/ circom-snarkjs", size=7, marker="triangle",fill_color='lightsteelblue')
p.line(snarkjs_mimc_input_length, snarkjs_mimc_prove_times, legend_label="mimc/ circom-snarkjs", color="lightsteelblue")

p.scatter(snarkjs_poseidon_input_length, snarkjs_poseidon_prove_times, size=7, marker="square", legend_label="poseidon/ circom-snarkjs", fill_color="lightsteelblue")
p.line(snarkjs_poseidon_input_length, snarkjs_poseidon_prove_times, legend_label="poseidon/ circom-snarkjs", color="lightsteelblue")

p.legend.location = "top_left"
p.legend.title = "Hash Function/ Library"

p.xaxis.ticker = FixedTicker(ticks=[i for i in range(2, 17)])

p.output_backend = "svg"
# show the results
show(p)