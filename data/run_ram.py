from bokeh.plotting import figure, show
from bokeh.models.tickers import FixedTicker
from parser import noir_parser, snarkjs_parser
import os

# Construct the full path to the noir file
data_path_noir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../noir/bench/results_ave2.json')

data_path_snarkjs = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../snarkjs_bench/bench/results.json')

noir_mimc_input_length, noir_mimc_prove_times, noir_griffin_input_length,noir_griffin_prove_times,noir_poseidon_input_length, noir_poseidon_prove_times, noir_poseidon2_input_length,noir_poseidon2_prove_times = noir_parser(data_path_noir, 'prove', 'max_resident_size')

snarkjs_mimc_input_length, snarkjs_mimc_prove_times, snarkjs_poseidon_input_length, snarkjs_poseidon_prove_times = snarkjs_parser(data_path_snarkjs, 'prove', 'max_resident_size')

# create a new plot with a title and axis labels
p = figure(title="Proof generation max resident size with different input length (MBP M1)", x_axis_label="Input length", y_axis_label="Max resident size/ kb",width=800, height=600, y_axis_type="log", y_range=(10.0**3, 10.0**6))

kb_noir_mimc_prove_times = [int(x) / 1024 for x in noir_mimc_prove_times]
kb_noir_griffin_prove_times = [int(x) / 1024 for x in noir_griffin_prove_times]
kb_noir_poseidon_prove_times = [int(x) / 1024 for x in noir_poseidon_prove_times]
kb_noir_poseidon2_prove_times = [int(x) / 1024 for x in noir_poseidon2_prove_times]
kb_snarkjs_mimc_prove_times = [int(x) / 1024 for x in snarkjs_mimc_prove_times]
kb_snarkjs_poseidon_prove_times = [int(x) / 1024 for x in snarkjs_poseidon_prove_times]

# add multiple renderers
p.scatter(noir_mimc_input_length, kb_noir_mimc_prove_times, size=7, marker="triangle",fill_color='navy')
p.line(noir_mimc_input_length, kb_noir_mimc_prove_times, color="navy")

p.scatter(noir_griffin_input_length, kb_noir_griffin_prove_times, size=7, fill_color='navy')
p.line(noir_griffin_input_length, kb_noir_griffin_prove_times,  color="navy")

p.scatter(noir_poseidon_input_length, kb_noir_poseidon_prove_times, size=7, marker="square",  fill_color="navy")
p.line(noir_poseidon_input_length, kb_noir_poseidon_prove_times,  color="navy")

p.scatter(noir_poseidon2_input_length, kb_noir_poseidon2_prove_times, size=7, marker="plus", fill_color='navy')
p.line(noir_poseidon2_input_length, kb_noir_poseidon2_prove_times,  color="navy")

p.scatter(snarkjs_mimc_input_length, kb_snarkjs_mimc_prove_times,  size=7, marker="triangle",fill_color='lightsteelblue')
p.line(snarkjs_mimc_input_length, kb_snarkjs_mimc_prove_times, color="lightsteelblue")

p.scatter(snarkjs_poseidon_input_length, kb_snarkjs_poseidon_prove_times, size=7, marker="square",  fill_color="lightsteelblue")
p.line(snarkjs_poseidon_input_length, kb_snarkjs_poseidon_prove_times, color="lightsteelblue")

# p.legend.location = "bottom_right"
# p.legend.title = "Hash Function/ Library"

p.xaxis.ticker = FixedTicker(ticks=[i for i in range(2, 17)])

p.output_backend = "svg"
# show the results
show(p)