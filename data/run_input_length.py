from bokeh.plotting import figure, show
from bokeh.models.tickers import FixedTicker
from bokeh.layouts import gridplot
from parser import noir_parser, snarkjs_parser
# from bokeh.io import export_svg
import os

# runtime plot
# Construct the full path to the noir file
data_path_noir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../noir/bench/input_length_results_ave2.json')

data_path_snarkjs = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../snarkjs_bench/bench/results_input_length.json')

noir_mimc_input_length, noir_mimc_prove_times, noir_griffin_input_length,noir_griffin_prove_times,noir_poseidon_input_length, noir_poseidon_prove_times, noir_poseidon2_input_length,noir_poseidon2_prove_times = noir_parser(data_path_noir, 'prove', 'user_time')

snarkjs_mimc_input_length, snarkjs_mimc_prove_times, snarkjs_poseidon_input_length, snarkjs_poseidon_prove_times = snarkjs_parser(data_path_snarkjs, 'prove', 'user_time')

# create a new plot with a title and axis labels
p1 = figure(title="Proof generation runtime with different input length (MBP M1)", x_axis_label="Input length", y_axis_label="Runtime/ millisecond",width=800, height=600)

# add multiple renderers
p1.scatter(noir_mimc_input_length, noir_mimc_prove_times, legend_label="mimc/ noir-bb", size=7, marker="triangle",fill_color='navy')
p1.line(noir_mimc_input_length, noir_mimc_prove_times, legend_label="mimc/ noir-bb", color="navy")

p1.scatter(noir_griffin_input_length, noir_griffin_prove_times, legend_label="griffin/ noir-bb", size=7, fill_color='navy')
p1.line(noir_griffin_input_length, noir_griffin_prove_times, legend_label="griffin/ noir-bb", color="navy")

p1.scatter(noir_poseidon_input_length, noir_poseidon_prove_times, size=7, marker="square", legend_label="poseidon/ noir-bb", fill_color="navy")
p1.line(noir_poseidon_input_length, noir_poseidon_prove_times, legend_label="poseidon/ noir-bb", color="navy")

p1.scatter(noir_poseidon2_input_length, noir_poseidon2_prove_times, legend_label="poseidon2/ noir-bb", size=7, marker="plus", fill_color='navy')
p1.line(noir_poseidon2_input_length, noir_poseidon2_prove_times, legend_label="poseidon2/ noir-bb", color="navy")

p1.scatter(snarkjs_mimc_input_length, snarkjs_mimc_prove_times, legend_label="mimc/ circom-snarkjs", size=7, marker="triangle",fill_color='lightsteelblue')
p1.line(snarkjs_mimc_input_length, snarkjs_mimc_prove_times, legend_label="mimc/ circom-snarkjs", color="lightsteelblue")

p1.scatter(snarkjs_poseidon_input_length, snarkjs_poseidon_prove_times, size=7, marker="square", legend_label="poseidon/ circom-snarkjs", fill_color="lightsteelblue")
p1.line(snarkjs_poseidon_input_length, snarkjs_poseidon_prove_times, legend_label="poseidon/ circom-snarkjs", color="lightsteelblue")

p1.legend.location = "top_left"
p1.legend.title = "Hash Function/ Library"

p1.xaxis.ticker = FixedTicker(ticks=[i for i in range(2, 17)])

# p1.output_backend = "svg"

# ram plot
# Construct the full path to the noir file
data_path_noir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../noir/bench/input_length_results_ave2.json')

data_path_snarkjs = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../snarkjs_bench/bench/results_input_length.json')

noir_mimc_input_length, noir_mimc_prove_times, noir_griffin_input_length,noir_griffin_prove_times,noir_poseidon_input_length, noir_poseidon_prove_times, noir_poseidon2_input_length,noir_poseidon2_prove_times = noir_parser(data_path_noir, 'prove', 'max_resident_size')

snarkjs_mimc_input_length, snarkjs_mimc_prove_times, snarkjs_poseidon_input_length, snarkjs_poseidon_prove_times = snarkjs_parser(data_path_snarkjs, 'prove', 'max_resident_size')

# create a new plot with a title and axis labels
p2 = figure(title="Proof generation max resident size with different input length (MBP M1)", x_axis_label="Input length", y_axis_label="Max resident size/ kb",width=800, height=600, y_axis_type="log", y_range=(10.0**3, 10.0**6))

kb_noir_mimc_prove_times = [int(x) / 1024 for x in noir_mimc_prove_times]
kb_noir_griffin_prove_times = [int(x) / 1024 for x in noir_griffin_prove_times]
kb_noir_poseidon_prove_times = [int(x) / 1024 for x in noir_poseidon_prove_times]
kb_noir_poseidon2_prove_times = [int(x) / 1024 for x in noir_poseidon2_prove_times]
kb_snarkjs_mimc_prove_times = [int(x) / 1024 for x in snarkjs_mimc_prove_times]
kb_snarkjs_poseidon_prove_times = [int(x) / 1024 for x in snarkjs_poseidon_prove_times]

# add multiple renderers
p2.scatter(noir_mimc_input_length, kb_noir_mimc_prove_times, size=7, marker="triangle",fill_color='navy')
p2.line(noir_mimc_input_length, kb_noir_mimc_prove_times, color="navy")

p2.scatter(noir_griffin_input_length, kb_noir_griffin_prove_times, size=7, fill_color='navy')
p2.line(noir_griffin_input_length, kb_noir_griffin_prove_times,  color="navy")

p2.scatter(noir_poseidon_input_length, kb_noir_poseidon_prove_times, size=7, marker="square",  fill_color="navy")
p2.line(noir_poseidon_input_length, kb_noir_poseidon_prove_times,  color="navy")

p2.scatter(noir_poseidon2_input_length, kb_noir_poseidon2_prove_times, size=7, marker="plus", fill_color='navy')
p2.line(noir_poseidon2_input_length, kb_noir_poseidon2_prove_times,  color="navy")

p2.scatter(snarkjs_mimc_input_length, kb_snarkjs_mimc_prove_times,  size=7, marker="triangle",fill_color='lightsteelblue')
p2.line(snarkjs_mimc_input_length, kb_snarkjs_mimc_prove_times, color="lightsteelblue")

p2.scatter(snarkjs_poseidon_input_length, kb_snarkjs_poseidon_prove_times, size=7, marker="square",  fill_color="lightsteelblue")
p2.line(snarkjs_poseidon_input_length, kb_snarkjs_poseidon_prove_times, color="lightsteelblue")

# p2.legend.location = "bottom_right"
# p2.legend.title = "Hash Function/ Library"

p2.xaxis.ticker = FixedTicker(ticks=[i for i in range(2, 17)])

# p2.output_backend = "svg"

# show the results
show(gridplot([p1, p2], ncols=2, width=600, height=600))